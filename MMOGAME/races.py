from map import players_pos
from abilities import *

class race:
    def __init__(self,  X_start, Y_start):
        
        self.X_start = X_start
        self.Y_start = Y_start
        self.X_now = X_start
        self.Y_now = Y_start
        self.lvl = 0
        self.XP_levelUp = 250 + self.lvl * 50
        self.XP = 0
        players_pos.set_tile(self.char , X_start, Y_start)
        self.damageTaken = 0
        self.currentHP = self.MAX_HP
        self.isDead = False
        self.isStun = False
        self.DoTCount = 0
        self.stunCount = 0
        self.DoTDamage = 0
        
    def xp(self, XP):
        self.XP += XP
        while self.XP > self.XP_levelUp: 
            self.lvl += 1
            self.XP -= self.XP_levelUp
            self.XP_levelUp = 250 + self.lvl * 50
            self.levelUp()

    def levelUp(self):
        self.MAX_HP += self.HP_GROWTH
        self.currentHP = self.MAX_HP

    def showStats(self):
        print(self.lvl, "\n", str(self.currentHP) + "/" + str(self.MAX_HP))

    def move(self, dir):


        if dir == "D":
            self.X_now += 1
            players_pos.set_tile(self.char, self.X_now, self.Y_now)
            players_pos.set_tile(0, self.X_now - 1, self.Y_now)

        elif dir == "U":
            self.X_now -= 1
            players_pos.set_tile(self.char, self.X_now, self.Y_now)
            players_pos.set_tile(0, self.X_now + 1, self.Y_now)

        elif dir == "R":
            self.Y_now += 1
            players_pos.set_tile(self.char, self.X_now, self.Y_now)
            players_pos.set_tile(0, self.X_now, self.Y_now - 1)

        elif dir == "L":
            self.Y_now -= 1
            players_pos.set_tile(self.char, self.X_now, self.Y_now)
            players_pos.set_tile(0, self.X_now, self.Y_now + 1)

        elif dir == "_":
            players_pos.set_tile(self.char, self.X_now, self.Y_now)

    def dmgCount(self, damage):
        self.damageTaken += damage  

    def takeDmg(self, DoT = 0):
        self.currentHP -= self.damageTaken + DoT
        if self.currentHP <= 0:
            self.death()
        self.damageTaken = 0

    def dotted(self):
        self.DoTCount -= 1
        self.takeDmg(self.DoTDamage)

    def death(self):
        players_pos.set_tile(0, self.X_now, self.Y_now)
        self.isDead = True

    def playerPosition(self):
        return (self.X_now, self.Y_now)

    def attack(self, target):
        target.dmgCount(self.A1.DMG)
        target.dmgCount(self.A2.DMG)

    def calcAbilities(self, enemy):
        if self.a1 == "fireblast":
            self.A1 = fireblast(self.lvl, enemy)

        elif self.a1 == "backstab":
            self.A1 = backstab(self.lvl, enemy)

        elif self.a1 == "execute":
            self.A1 = execute(self.lvl, enemy)

        elif self.a1 == "drain":
            self.A1 = drain(self.lvl, enemy)

        if self.a2 == "ignite":
            self.A2 = ignite(self.lvl, enemy)

        elif self.a2 == "paralysis":
            self.A2 = paralysis(self.lvl, enemy)
        
        elif self.a2 == "deflect":
            self.A2 = deflect(self.lvl, enemy)
        
        elif self.a2 == "slam":
            self.A2 = slam(self.lvl, enemy)
    
class pyromancer(race):
    char = "P"
    MAX_HP = 500
    HP_GROWTH = 50
    

    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.a1 = "fireblast"
        self.a2 =  "ignite"
        self.char = "P"
        
class knight(race):
    MAX_HP = 900
    HP_GROWTH = 80 
    char = "K"
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.a1 = "execute"
        self.a2 =  "slam"
        self.char = "K"
               
class wizard(race):
    char = "W"
    MAX_HP = 400
    HP_GROWTH = 30
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.a1 = "drain"
        self.a2 =  "deflect"
        self.char = "w"
        
class rogue(race):
    char = "R"
    MAX_HP = 600
    HP_GROWTH = 40
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.a1 = "backstab"
        self.a2 = "paralysis"
        self.char = "R"