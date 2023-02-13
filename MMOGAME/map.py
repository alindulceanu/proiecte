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
    
    def generateTiles(self):
        for i in range(self.i):
            for j in range(self.j):
                if i % 2 == 0 and j % 2 == 0:
                    self.set_tile("L", i, j)
                elif i % 2 ==0 and j % 2 !=0 :
                    self.set_tile("D", i, j)
                elif i % 2 != 0 and j % 2 == 0:
                    self.set_tile("V", i, j)
                elif i % 2 != 0 and j % 2 != 0:
                    self.set_tile("W", i, j)
                

tiles = map(6, 6)
players_pos = map(6, 6)


