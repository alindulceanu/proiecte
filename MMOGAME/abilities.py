class abillity:
    def __init__(self, lvl, enemy):
        self.modDMG = 0




class fireblast(abillity):
    
    def __init__(self, lvl, enemy):

        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy
        self.rawDMG = 350
        self.DMG_GROWTH = 50

        self.rawDMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 0.8

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 0.9

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 1.05

        self.modDMG = round(self.modDMG)
        
class backstab(abillity):

    def __init__(self, lvl, enemy):
        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy
        self.rawDMG = 200
        self.DMG_GROWTH = 20

        self.rawDMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 0.9

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 1.25

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 1.25
        
        self.modDMG = round(self.modDMG)

class paralysis(abillity):

    def __init__(self, lvl, enemy):
        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy
        self.rawDMG = 40
        self.DMG_GROWTH = 10

        self.rawDMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 0.9

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 1.25

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 1.25
            
        
        self.modDMG = round(self.modDMG)
        enemy.DoTDamage = self.modDMG
        enemy.DoTCount = 3

class execute(abillity):

    def __init__(self, lvl, enemy):

        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy
        self.rawDMG = 200
        self.DMG_GROWTH = 30
        self.execGrowth = 0.20 + self.lvl / 100
        self.rawDMG += self.DMG_GROWTH * self.lvl

        if self.execGrowth > 0.4:
            self.execGrowth = 0.4

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 1.15

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 1.10

        elif self.enemy.char == "W":
            
            self.modDMG = self.rawDMG * 0.8
        
        self.modDMG = round(self.modDMG)
        

        if enemy.MAX_HP * self.execGrowth >= enemy.currentHP:
            self.modDMG = enemy.currentHP

class ignite(abillity):

    def __init__(self, lvl, enemy):

        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy

        self.rawDMG = 150
        self.DMG_GROWTH = 20
        self.DoT = 50
        self.DoTGrowth = 30

        self.rawDMG += self.DMG_GROWTH * self.lvl
        self.DoT += self.DoTGrowth * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 0.8
            self.DoT *= 0.8

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 1.2
            self.DoT *= 1.2

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 0.9
            self.DoT *= 0.9

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 1.05
            self.DoT *= 1.05
        
        self.modDMG = round(self.modDMG)
        self.DoT = round(self.DoT)

        enemy.DoTDamage = self.DoT
        enemy.DoTCount = 2

class slam(abillity):
    
    def __init__(self, lvl, enemy):
        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy

        self.rawDMG = 100
        self.DMG_GROWTH = 40

        self.rawDMG += self.DMG_GROWTH * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 0.8

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 0.9

        elif self.enemy.char == "W":
            
            self.modDMG = self.rawDMG * 1.05

        self.modDMG = round(self.modDMG)

class drain(abillity):
    
    def __init__(self, lvl, enemy):
        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy

        self.rawDMG = 0.2
        self.DMGGrowth = 0.05

        self.rawDMG += self.DMGGrowth * self.lvl

        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 0.8

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 0.9

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 1.05


        self.modDMG = self.modDMG * min(0.3 * enemy.MAX_HP, enemy.currentHP)
        self.modDMG = round(self.modDMG)

class deflect(abillity):
    
    def __init__(self, lvl, enemy):

        super().__init__(lvl, enemy)
        self.lvl = lvl
        self.enemy = enemy

        self.rawDMG = 0.35
        self.DMGGrowth = 0.02

        self.rawDMG += self.DMGGrowth * self.lvl

        if self.rawDMG > 0.7:
            self.rawDMG = 0.7
        
        self.rawDMG = (enemy.A1.rawDMG + enemy.A2.rawDMG) * self.rawDMG
        
        if self.enemy.char == "R":
            self.modDMG = self.rawDMG * 1.2

        elif self.enemy.char == "K":
            self.modDMG = self.rawDMG * 1.4

        elif self.enemy.char == "P":
            self.modDMG = self.rawDMG * 1.3

        elif self.enemy.char == "W":
            self.modDMG = self.rawDMG * 0

        self.modDMG = round(self.modDMG)