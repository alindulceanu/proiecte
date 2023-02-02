from abilities import *
from map import *
from races import *



players_pos = map(6, 6)
tiles = map(6, 6)
p1 = wizard(2, 2)
p2 = knight(2, 2)

r = 3

players = (p1, p2)

while r != 0:
    
    for p in range(len(players)):
        if players[p].DoTCount != 0:
            players[p].dotted()

    p1.move("_")
    p2.move("_")
        
    if p1.playerPosition() == p2.playerPosition():
        
        
        p2.calcAbilities(p1)
        p1.calcAbilities(p2)
        p1.attack(p2)
        p2.attack(p1)
        p1.takeDmg()
        p2.takeDmg()

    r -= 1
    

p1.showStats()
p2.showStats()


players_pos.i