from string import ascii_uppercase


class Board:
    def __init__(self):
        self.matrix = [[0 for x in range(8)] for y in range(8)]


    def genSquares(self):
        for lin in range(8):
            for col in range(8):
                self.matrix[col][lin] = str(ascii_uppercase[lin]) + str(8 - col)

    def showBoard(self):
        for x in range(8):
            print(self.matrix[x], "\n")

    def returnPosition(self, coordinates):
        for lin in range(8):
            for col in range(8):
                if self.matrix[lin][col] == coordinates:
                    return lin, col


    def move(self, initial, destination):
        xi, yi = coords.returnPosition(initial)
        xd, yd = coords.returnPosition(destination)
        piecePos.matrix[xd][yd] = piecePos.matrix[xi][yi]
        piecePos.matrix[xi][yi] = 0

    def addPiece(self, char, coordinates):
        x, y = coords.returnPosition(coordinates)
        piecePos.matrix[x][y] = char

    def checkSquare(self, coordinates):
        x, y = coords.returnPosition(coordinates)
        if piecePos.matrix[x][y] != 0:
            return True
        else:
            return False




coords = Board()
coords.genSquares()
piecePos = Board()

