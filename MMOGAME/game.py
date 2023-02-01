from numpy import *



class map:
    def __init__(self, i, j):
        self.i = i
        self.j = j 
        self.matrix = [[0 for col in range(self.j)] for row in range(self.i)]
        
    def print_map(self):
        for i in range(self.i):
            print(self.matrix[i], "\n")

    def set_tile(self, type, poz_x, poz_y):
         self.matrix[poz_x][poz_y] = type

    def transfer_char(self, i, j):
        return self.matrix[i][j]


class race:
    def __init__(self,  X_start, Y_start):
        
        self.X_start = X_start
        self.Y_start = Y_start
        self.X_now = X_start
        self.Y_now = Y_start
        self.lvl = 0
        self.XP_level_up = 250 + self.lvl * 50
        self.XP = 0
        players_poz.set_tile(self.char , X_start, Y_start)
        


    def xp(self, XP):
        self.XP += XP
        while self.XP > self.XP_level_up: 
            self.lvl += 1
            self.XP -= self.XP_level_up
            self.XP_level_up = 250 + self.lvl * 50
            self.level_up()

    def level_up(self):
        self.MAX_HP += self.HP_GROWTH

    def show_stats(self):
        print(self.lvl, "\n", self.MAX_HP)

      
    def move(self, dir):


        if dir == "D":
            self.X_now += 1
            players_poz.set_tile(self.char, self.X_now, self.Y_now)
            players_poz.set_tile(0, self.X_now - 1, self.Y_now)

        elif dir == "U":
            self.X_now -= 1
            players_poz.set_tile(self.char, self.X_now, self.Y_now)
            players_poz.set_tile(0, self.X_now + 1, self.Y_now)

        elif dir == "R":
            self.Y_now += 1
            players_poz.set_tile(self.char, self.X_now, self.Y_now)
            players_poz.set_tile(0, self.X_now, self.Y_now - 1)

        elif dir == "L":
            self.Y_now -= 1
            players_poz.set_tile(self.char, self.X_now, self.Y_now)
            players_poz.set_tile(0, self.X_now, self.Y_now + 1)

        elif dir == "_":
            players_poz.set_tile(self.char, self.X_now, self.Y_now)

class pyromancer(race):
    char = "P"
    def __init__(self, X_start, Y_start):
        super().__init__(X_start, Y_start)
        self.MAX_HP = 500
        self.HP_GROWTH = 50
        
        




players_poz = map(6,6)

tiles = map(6,6)

p1 = pyromancer(3, 2)

p1.xp(1000)

p1.show_stats()



players_poz.print_map()







