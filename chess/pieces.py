import board
from string import ascii_uppercase

class piece:
    def __init__(self, team, position):
        self.team = team
        self.pos = position
        self.firstMove = True
        self.posList = []
        board.piecePos.addPiece(self.char, self.pos)

    

    def move(self, target, victim):
        global x
        x = 0
        moves = self.validMoves()
        for x in range(len(moves)):
            if target == moves[x]:
                x = 1
                
                board.piecePos.move(self.pos, target)
                self.pos = target
                if self.firstMove == True:
                    self.firstMove = False

                break

        if x != 1:
            print('Invalid move!')   

    # trebuie terminata functia capture

    def showPosList(self):
        print(self.posList)



#pawn

'''
class pawn(piece):
    def __init__(self, team, position):
        super().__init__(team, position)
        self.char = "P"

    def checkSquare(self, square):
        if self.team == "W":

    def move(self, target):

'''

class rook(piece):

    char = 'R'

    def __init__(self, team, position):
        super().__init__(team, position)
        

    def validMoves(self):

        posList = []

        for dir in range(4):
            
            if dir == 0:
                for squares in range(8 - int(self.pos[1])):
                        
                        if self.pos == (self.pos[0] + str(int(self.pos[1]) + squares + 1)):
                            continue

                        posList.append(self.pos[0] + str(int(self.pos[1]) + squares + 1))

                        if board.piecePos.checkSquare(self.pos[0] + str(int(self.pos[1]) + squares + 1)) == True:
                            break
            
            elif dir == 1:
                for squares in range(int(self.pos[1])):

                    if self.pos == (self.pos[0] + str(int(self.pos[1]) - squares )):
                        continue

                    posList.append(self.pos[0] + str(int(self.pos[1]) - squares ))

                    if board.piecePos.checkSquare(self.pos[0] + str(int(self.pos[1]) - squares )) == True:
                        break

            elif dir == 2:
                for squares in range(ascii_uppercase.find(self.pos[0])):

                    if self.pos == (ascii_uppercase[ascii_uppercase.find(self.pos[0]) - squares - 1] + str(self.pos[1])):
                        continue

                    posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - squares - 1] + str(self.pos[1]))

                    if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - squares - 1] + str(self.pos[1])) == True:
                        break


            elif dir == 3:
                for squares in range(8 - ascii_uppercase.find(self.pos[0])):

                    if self.pos == (ascii_uppercase[ascii_uppercase.find(self.pos[0]) + squares] + str(self.pos[1])):
                        continue

                    posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + squares] + str(self.pos[1]))

                    if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + squares] + str(self.pos[1])) == True:
                        break
                
        return posList             
            

class bishop(piece):
    char = "B"

    def __init__(self, team, position):
        super().__init__(team, position)


    def validMoves(self):
        self.posList = []

        for dir in range(4):

            
            if dir == 0:
                found = False
                for row in range(int(self.pos[1])):
                    for col in range(8 - ascii_uppercase.find(self.pos[0])):

                        if row == col:
                            print('bruh')
                            if self.pos == ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) - row):
                                continue
                                
                            self.posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) - row))
                            if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) - row)) == True:
                                found = True
                                break
                    if found == True:
                        break
            
            if dir == 1:
                found = False
                for row in range(9 - int(self.pos[1])):
                    for col in range(8 - ascii_uppercase.find(self.pos[0])):

                        if (row == col):
                            if self.pos == (ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) + row)):
                                continue
                            self.posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) + row))
                            if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) + row] + str(int(self.pos[1]) + row)) == True:
                                found = True
                                break
                    if found == True:
                        break

            if dir == 2:
                found = False
                for row in range(int(self.pos[1])):
                    for col in range(ascii_uppercase.find(self.pos[0]) + 1):
                        if row == col:
                            if self.pos == (ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) - row)):
                                continue
                            self.posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) - row))
                            if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) - row)) == True:
                                found = True
                                break
                    if found == True:
                        break

            if dir == 3:
                found = False
                for row in range(9 - int(self.pos[1])):
                    for col in range(ascii_uppercase.find(self.pos[0]) + 1):
                        if row == col:
                            if self.pos == (ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) + row)):
                                continue
                            self.posList.append(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) + row))
                            if board.piecePos.checkSquare(ascii_uppercase[ascii_uppercase.find(self.pos[0]) - row]+str(int(self.pos[1]) + row)) == True:
                                found = True
                                break
                    if found == True:
                        break


b1 =  bishop('W', 'D5')
b2 = rook('W', 'F3')
b1.validMoves()
board.piecePos.showBoard()

print(b1.showPosList())




