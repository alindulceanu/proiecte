from abilities import *
from map import *
from races import *


def fight(player1, player2, pos):

    if tiles.matrix[pos[0]][pos[1]] == "L":
        if player1.char == "K":
            player1.multiplier = 1.15
        if player2.char == "K":
            player2.multiplier = 1.15

    if tiles.matrix[pos[0]][pos[1]] == "V":
        if player1.char == "P":
            player1.multiplier = 1.25
        if player2.char == "P":
            player2.multiplier = 1.25

    if tiles.matrix[pos[0]][pos[1]] == "D":
        if player1.char == "W":
            player1.multiplier = 1.1
        if player2.char == "W":
            player2.multiplier = 1.1

    if tiles.matrix[pos[0]][pos[1]] == "W":
        if player1.char == "R":
            player1.multiplier = 1.15
        if player2.char == "R":
            player2.multiplier = 1.15

    if player1.char == "W" and player2.char == "W":
        player1.WW == True
        player2.WW == True
    elif player1.char == "W":
        p = player1
        player1 = player2
        player2 = p


    player1.calcAbilities(player2)
    player2.calcAbilities(player1)
    player1.attack(player2)
    player2.attack(player1)
    player1.takeDmg()
    player2.takeDmg()

    if player2.isDead == True:
        player1.xp(player2.lvl)

    if player1.isDead == True:
        player2.xp(player1.lvl)

p1 = wizard(3, 2)
p2 = pyromancer(2, 1)
p3 = knight(2, 0)
p4 = rogue(2, 5)

r = 1

players = (p1, p2, p3, p4)


while r != 0:
    
    p2.move("L")


    for p in range(len(players)):
        if players[p].DoTCount != 0:
            players[p].dotted()
        if players[p].isStun == True and players[p].stunCount == 0:
            players[p].stunCount -= 1
        else:
            players[p].isStun = False 
    
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            if players[i].playerPosition() == players[j].playerPosition():
                if players[i].isDead == False and players[j].isDead == False:
                    
                    fight(players[i], players[j], players[i].playerPosition)

                

    r -= 1


p1.showStats()
p2.showStats()
p3.showStats()
p4.showStats()

print(p2.isDead)
tiles.generateTiles()
tiles.print_map()