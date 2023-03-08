from abilities import *
from map import *
from races import *

def fight(player1, player2):
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

def checkWiz(playerList):
    for i in range(len(playerList)):
        if playerList[i].char == "W":
            for k in range(len(playerList)):
                if k != i:
                    playerList[k].calcAbilities(playerList[i])

def checkDebuff(playerList):
    for p in range(len(playerList)):
        playerList[p].stunCount -= 1

        if playerList[p].DoTCount != 0:
            playerList[p].dotted()

        if playerList[p].stunCount == 0:
            playerList[p].isStun = False


            

tiles.generate()

p2 = pyromancer(2, 0)
p1 = wizard(2, 2)
p3 = knight(3, 0)
p4 = rogue(3, 0)

r = 1

players = [p1, p2, p3, p4]

while r != 0:
    
    
    checkDebuff(players)

    checkWiz(players)



    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            if players[i].playerPosition() == players[j].playerPosition():
                if players[i].isDead == False and players[j].isDead == False:
                    fight(players[i], players[j])
        

    r -= 1


p1.showStats()
p2.showStats()
p3.showStats()
p4.showStats()




