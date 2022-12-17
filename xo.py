import tkinter as tk
import tkinter.messagebox as mb
import time
from datetime import datetime

player = 1
win_game = False
g = True


def matrix():
    
    for i in range(3):
        for j in range(3):
            b[i][j] = tk.Button(
                height = 10,
                width = 30,
                command = lambda x = i, y = j: click(x, y)
            )
            b[i][j].grid(row = i, column = j)

def click(x, y):

    global player
    

    if  player == 1 and poz[x][y] == 0 and win_game == False:
        b[x][y].configure(text = "X")
        poz[x][y] = "X"
        player = 0

    if player == 0 and poz[x][y] == 0 and win_game == False:
        b[x][y].configure(text = "O")
        poz[x][y] = "O"
        player = 1
    win()

def win():
    global g
    global win_game
    global winner
    for i in range(3):
        if poz[i][0] == poz[i][1] == poz[i][2] != 0:
            win_game = True
            winner.configure(text = poz[i][1] + " a castigat")
            g = False
            break

        elif poz[0][i] == poz[1][i] == poz[2][i] != 0:
            win_game = True
            winner.configure(text = poz[1][i] + " a castigat")
            g = False
            break

    if poz[0][0] == poz[2][2] == poz[1][1] != 0:
        win_game = True
        winner.configure(text = poz[1][1] + " a castigat")
        g = False
        
    elif poz[0][2] == poz[1][1] == poz[2][0] != 0:
        win_game = True
        winner.configure(text = poz[1][1] + " a castigat")
        g = False
        
def reset():
    global poz
    global player
    global win_game
    global g
    global start_time
    poz = [
     [0 ,0 ,0],
     [0 ,0 ,0],
     [0 ,0 ,0]]
    
    winner.configure(text = "win")
    player = 1
    win_game = False
    matrix()
    g = True
    

root = tk.Tk()
root.title("Tik Tac Toe")

b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

poz = [
     [0 ,0 ,0],
     [0 ,0 ,0],
     [0 ,0 ,0]
]

matrix()

reset = tk.Button(
    text = "Reset",
    command = reset
)
reset.grid(row = 3, column = 0)
winner = tk.Label(text = "win")
winner.grid(row = 3, column = 1)
root.mainloop()