import tkinter as tk
import tkinter.messagebox as mb


player = 1
win_game = False

 
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

    global win_game

    for i in range(3):
        if poz[i][0] == poz[i][1] == poz[i][2] != 0:
            win_game = True
            winner = mb.showinfo("Felicitari!", poz[i][0]+ " a castigat!")
            break

        elif poz[0][i] == poz[1][i] == poz[2][i] != 0:
            win_game = True
            winner = mb.showinfo("Felicitari!", poz[i][0]+ " a castigat!")
            break

    if poz[0][0] == poz[2][2] == poz[1][1] != 0:
        win_game = True
        winner = mb.showinfo("Felicitari!", poz[1][1]+ " a castigat!")
        
    elif poz[0][2] == poz[1][1] == poz[2][0] != 0:
        win_game = True
        winner = mb.showinfo("Felicitari!", poz[1][1]+ " a castigat!")
        

root = tk.Tk()
root.title("Tik Tac Toe")

b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

poz = [
     [0,0,0],
     [0,0,0],
     [0,0,0]
]

for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(
            text = " ",
            height = 10,
            width = 30,
            command = lambda x = i, y = j: click(x, y)
        )
        b[i][j].grid(row = i, column = j)

root.mainloop()