import tkinter as tk

player = 1
win_game = False
Scor1 = 0
Scor2 = 0
moreThanOneWindowOpen = False

def click(x, y):

    global player
    global win_game

    if  player == 1 and poz[x][y] == 0 and win_game == False:
        b[x][y].configure(text = "X", fg = "red")
        poz[x][y] = "X"
        player = 0

    if player == 0 and poz[x][y] == 0 and win_game == False:
        b[x][y].configure(text = "O", fg = "blue")
        poz[x][y] = "O"
        player = 1
    win()

def win():
    
    global win_game
    global winner
    global Scor1
    global Scor2
    nrPozFol = 0
    notTie = False

    for i in range(3):
        for j in range(3):
            if poz[i][j] != 0:
                nrPozFol += 1
            else:
                notTie = True
                break
        if notTie == True:
            break

    for i in range(3):
        if poz[i][0] == poz[i][1] == poz[i][2] != 0 and win_game == False:
            win_game = True
            if poz[i][1] == "X":
                winner.configure(text = nameOne + " a castigat")
                Scor1 += 1
            elif poz[i][1] == "O":
                winner.configure(text = nameTwo + " a castigat")
                Scor2 += 1
            
            break

        elif poz[0][i] == poz[1][i] == poz[2][i] != 0 and win_game == False:
            win_game = True
            if poz[1][i] == "X":
                winner.configure(text = nameOne + " a castigat")
                Scor1 += 1
            elif poz[1][i] == "O":
                winner.configure(text = nameTwo + " a castigat")
                Scor2 += 1
            
            break

        elif poz[0][0] == poz[2][2] == poz[1][1] != 0 and win_game == False:
            win_game = True
            if poz[1][1] == "X":
                    winner.configure(text = nameOne + " a castigat")
                    Scor1 += 1
            elif poz[1][1] == "O":
                    winner.configure(text = nameTwo + " a castigat")
                    Scor2 += 1
            
            
        elif poz[0][2] == poz[1][1] == poz[2][0] != 0 and win_game == False:
            win_game = True
            if poz[1][1] == "X":
                    winner.configure(text = nameOne + " a castigat")
                    Scor1 += 1
            elif poz[1][1] == "O":
                    winner.configure(text = nameTwo + " a castigat")
                    Scor2 += 1
            

        elif nrPozFol == 9:
            winner.configure(text = "Egalitate")

        

    scor.configure(text = str(Scor1) + "-" + str(Scor2))
    if Scor1 > Scor2:
        scor.configure(fg = "red")
    elif Scor1 < Scor2:
        scor.configure(fg = "blue")
    else:
        scor.configure(fg = "black")

    
def joc():
    global matrix
    global winner
    global root
    global scor
    root = tk.Tk()
    root.title("Tik Tac Toe")
    root.resizable(False,False)

    
    def matrix():
    
        for i in range(3):
            for j in range(3):
                b[i][j] = tk.Button(
                    root,
                    height = 10,
                    width = 30,
                    command = lambda x = i, y = j: click(x, y),
                    font = ("times", 15)
                )
                b[i][j].grid(row = i, column = j)
    
    def reset():
        global poz
        global player
        global win_game
        
        poz = [
        [0 ,0 ,0],
        [0 ,0 ,0],
        [0 ,0 ,0]]
        
        winner.configure(text = "")
        player = 1
        win_game = False
        matrix()
        

    matrix()

    reset = tk.Button(
    root,
    text = "Next",
    command = reset,
    font = ("times", 15)
    )

    reset.grid(row = 3, column = 0)

    winner = tk.Label(root, fg = "darkred", font = ("times", 15))
    winner.grid(row = 4, column = 1)

    name1 = tk.Label(
        root,
        text = nameOne,
        fg = "red",
        font = ("times", 15)
    )
    name1.grid(row = 3, column = 1)

    name2 = tk.Label(
        root,
        text = nameTwo,
        fg = "blue",
        font = ("times", 15)
    )
    name2.grid(row = 3, column = 2)

    scor = tk.Label(
        root,
        text = str(Scor1) + "-" + str(Scor2),
        font = ("times", 15)
    )
    scor.grid(row = 4, column = 2)

    root.mainloop()

def ok():
    global moreThanOneWindowOpen
    terror.destroy()
    moreThanOneWindowOpen = False

def check():
    global nameOne
    global nameTwo
    global name1
    global name2

    nameOne = name1.get()
    nameTwo = name2.get()

    if nameOne == "" or nameTwo == "":
        error()
    else:
        play()

def play():
    
    init.destroy()
    joc()

def error():
    global moreThanOneWindowOpen
    if moreThanOneWindowOpen == False:
        moreThanOneWindowOpen = True
        global terror
        terror = tk.Tk()
        terror.title("Error")
        msg = tk.Label(terror, text = "Va rugam inserati numele!", font = ("times", 15))
        msg.grid(row = 0, column = 1)
        button = tk.Button(terror, text = "Ok", command = ok)
        button.grid(row = 1, column = 1)
        terror.resizable(False,False)
        terror.mainloop()

    else:
        print("no")

def firstWindow():
    global name1
    global name2
    global init
    init = tk.Tk()
    init.title("Tic Tac Toe")
    init.resizable(False,False)

    name1 = tk.Entry(
        init, 
        font = ("times", 20),
        fg = "red"
    )
    name1.grid(row = 1, column = 1)

    name2 = tk.Entry(
        init, 
        font = ("times", 20),
        fg = "blue"
    )
    name2.grid(row = 1, column = 2)

    name1_text = tk.Label(
        init,
        text = "Jucatorul 1",
        font = ("times", 20)
    )
    name1_text.grid(row = 0, column = 1)

    name2_text = tk.Label(
        init,
        text = "Jucatorul 2",
        font = ("times", 20)
    )
    name2_text.grid(row = 0, column = 2)



    playButton = tk.Button(
        init,
        text = "PLAY",
        command = check,
        font = ("times", 20)
    )

    playButton.grid(row = 0, column = 0)
    init.mainloop()

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

firstWindow()