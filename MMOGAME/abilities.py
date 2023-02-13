from races import *

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
            self.factor = 1.05
            self.percent *= self.factor

        self.DMG = round(self.DMG)
        
class backstab():

    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy
        self.DMG = 200
        self.DMG_GROWTH = 20

        self.DMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.DMG *= 1.2

        elif self.enemy.char == "K":
            self.DMG *= 0.9

        elif self.enemy.char == "P":
            self.DMG *= 1.25

        elif self.enemy.char == "W":
            self.factor = 1.25
            self.percent *= self.factor
        
        self.DMG = round(self.DMG)

class paralysis():

    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy
        self.DMG = 40
        self.DMG_GROWTH = 10

        self.DMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.DMG *= 1.2

        elif self.enemy.char == "K":
            self.DMG *= 0.9

        elif self.enemy.char == "P":
            self.DMG *= 1.25

        elif self.enemy.char == "W":
            self.factor = 1.25
            self.percent *= self.factor
        
        self.DMG = round(self.DMG)
        enemy.DoTDamage = self.DMG
        enemy.DoTCount = 3

        enemy.isStun = True
        enemy.stunCount = 3

class execute():

    def __init__(self, lvl, enemy):
        
        self.lvl = lvl
        self.enemy = enemy
        self.DMG = 200
        self.DMG_GROWTH = 30
        self.execGrowth = 0.20 + self.lvl / 100
        self.factor = 0.8
        self.DMG += self.DMG_GROWTH * self.lvl

        if self.execGrowth > 0.4:
            self.execGrowth = 0.4

        if self.enemy.char == "R":
            self.DMG *= 1.15

        elif self.enemy.char == "P":
            self.DMG *= 1.10

        elif self.enemy.char == "W":
            
            self.percent *= self.factor
        
        self.DMG = round(self.DMG)
        

        if enemy.MAX_HP * self.execGrowth >= enemy.currentHP:
            self.DMG = enemy.currentHP

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
            self.factor = 1.05
            self.percent *= self.factor
            self.DoT *= self.factor
        
        self.DMG = round(self.DMG)
        self.DoT = round(self.DoT)

        enemy.DoTDamage = self.DoT
        enemy.DoTCount = 2

class slam():
    
    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy

        self.DMG = 100
        self.DMG_GROWTH = 40
        self.factor = 1.05

        self.DMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.DMG *= 0.8

        elif self.enemy.char == "K":
            self.DMG *= 1.2

        elif self.enemy.char == "P":
            self.DMG *= 0.9

        elif self.enemy.char == "W":
            
            self.percent *= self.factor

        self.DMG = round(self.DMG)

        enemy.isStun = True
        enemy.stunCount = 1

class drain():
    
    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy

        self.percent = 0.2
        self.percentGrowth = 0.05

        self.percent += self.percentGrowth * self.lvl

        if self.enemy.char == "R":
            self.percent *= 0.8

        elif self.enemy.char == "K":
            self.percent *= 1.2

        elif self.enemy.char == "P":
            self.percent *= 0.9

        elif self.enemy.char == "W":
            self.factor = 1.05
            self.percent *= self.factor


        self.DMG = self.percent * min(0.3 * enemy.MAX_HP, enemy.currentHP)
        self.DMG = round(self.DMG)

class deflect():
    
    def __init__(self, lvl, enemy):
        self.lvl = lvl
        self.enemy = enemy

        self.percent = 0.35
        self.percentGrowth = 0.02

        self.percent += self.percentGrowth * self.lvl

        if self.percent > 0.7:
            self.percent = 0.7

        self.DMG = (enemy.A1.DMG / enemy.A1.factor + enemy.A2.DMG / enemy.A2.factor) * self.percent

        if self.enemy.char == "R":
            self.DMG *= 1.2

        elif self.enemy.char == "K":
            self.DMG *= 1.4

        elif self.enemy.char == "P":
            self.DMG *= 1.3

        elif self.enemy.char == "W":
            self.DMG *= 0

        self.DMG = round(self.DMG)