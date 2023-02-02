class map:
    def __init__(self, i, j):
        self.i = i
        self.j = j 
        self.matrix = [[0 for col in range(self.j)] for row in range(self.i)]
        
    def print_map(self):
        for i in range(self.i):
            print(self.matrix[i], "\n")

    def set_tile(self, type, pos_x, pos_y):
         self.matrix[pos_x][pos_y] = type

    def playerPosition(self, player):
        return (player.X_now, player.Y_now)

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

        if self.a2 == "ignite":
            self.A2 = ignite(self.lvl, enemy)
        
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
               
class wizard(race):
    char = "W"
    MAX_HP = 400
    HP_GROWTH = 30
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        
class rogue(race):
    char = "R"
    MAX_HP = 600
    HP_GROWTH = 40
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.a1 = "backstab"
        self.a2 = "paralysis"
        self.char = "R"
        
class fireblast():
    
    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy

        self.DMG = 350
        self.DMG_GROWTH = 50

        self.DMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.DMG *= 0.8

        elif self.enemy.char == "K":
            self.DMG *= 1.2

        elif self.enemy.char == "P":
            self.DMG *= 0.9

        elif self.enemy.char == "W":
            self.DMG *= 1.05

        self.DMG = round(self.DMG)
        
class backstab():

    DMG = 200
    DMG_GROWTH = 20

class ignite():
    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy

        self.DMG = 150
        self.DMG_GROWTH = 20
        self.DoT = 50
        self.DoTGrowth = 30

        self.DMG += self.DMG_GROWTH * self.lvl
        self.DoT += self.DoTGrowth * self.lvl

        if self.enemy.char == "R":
            self.DMG *= 0.8
            self.DoT *= 0.8

        elif self.enemy.char == "K":
            self.DMG *= 1.2
            self.DoT *= 1.2

        elif self.enemy.char == "P":
            self.DMG *= 0.9
            self.DoT *= 0.9

        elif self.enemy.char == "W":
            self.DMG *= 1.05
            self.DoT *= 1.05
        
        self.DMG = round(self.DMG)
        self.DoT = round(self.DoT)

        enemy.DoTDamage = self.DoT
        enemy.DoTCount = 2


    


players_pos = map(6, 6)
tiles = map(6, 6)
p1 = pyromancer(2, 2)
p2 = knight(2, 2)



r = 3

players = (p1, p2)

while r != 0:
    
    for p in range(len(players)):
        if players[p].DoTCount != 0:
            players[p].dotted()

    if r < 3:
        p2.move("D")

    if p1.playerPosition() == p2.playerPosition():
        
        p1.calcAbilities(p2)
        
        p1.attack(p2)
        
        p1.takeDmg()
        p2.takeDmg()

    r -= 1
    

p1.showStats()
p2.showStats()


