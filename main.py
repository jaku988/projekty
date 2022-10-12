from tkinter import *
import random


def next_turn(num):
    global player
    global buttons

    if buttons[num].cget("text") == "":
        if player == 'x':
            buttons[num].config(text='x')
            label.config(text="{}'s Turn".format(players[1]))
        elif player == 'o':
            buttons[num].config(text='o')
            label.config(text="{}'s Turn".format(players[0]))

    if check_winner() != True and check_winner() != "Tie":
        if player == 'x':
            player = 'o'
        elif player == 'o':
            player = 'x'

    if check_winner() == True or check_winner() == "Tie":
        end()


def check_winner():
    if buttons[0].cget("text") == str(players[0]) and buttons[1].cget("text") == str(players[0]) and buttons[2].cget("text") == str(players[0]):
        color(0, 1, 2)
        return True
    elif buttons[0].cget("text") == str(players[1]) and buttons[1].cget("text") == str(players[1]) and buttons[2].cget("text") == str(players[1]):
        color(0, 1, 2)
        return True
    elif buttons[3].cget("text") == str(players[0]) and buttons[4].cget("text") == str(players[0]) and buttons[5].cget("text") == str(players[0]):
        color(3, 4, 5)
        return True
    elif buttons[3].cget("text") == str(players[1]) and buttons[4].cget("text") == str(players[1]) and buttons[5].cget("text") == str(players[1]):
        color(3, 4, 5)
        return True
    elif buttons[6].cget("text") == str(players[0]) and buttons[7].cget("text") == str(players[0]) and buttons[8].cget("text") == str(players[0]):
        color(6, 7, 8)
        return True
    elif buttons[6].cget("text") == str(players[1]) and buttons[7].cget("text") == str(players[1]) and buttons[8].cget("text") == str(players[1]):
        color(6, 7, 8)
        return True

    if buttons[0].cget("text") == str(players[0]) and buttons[3].cget("text") == str(players[0]) and buttons[6].cget("text") == str(players[0]):
        color(0, 3, 6)
        return True
    elif buttons[0].cget("text") == str(players[1]) and buttons[3].cget("text") == str(players[1]) and buttons[6].cget("text") == str(players[1]):
        color(0, 3, 6)
        return True
    elif buttons[1].cget("text") == str(players[0]) and buttons[4].cget("text") == str(players[0]) and buttons[7].cget("text") == str(players[0]):
        color(1, 4, 7)
        return True
    elif buttons[1].cget("text") == str(players[1]) and buttons[4].cget("text") == str(players[1]) and buttons[7].cget("text") == str(players[1]):
        color(1, 4, 7)
        return True
    elif buttons[2].cget("text") == str(players[0]) and buttons[5].cget("text") == str(players[0]) and buttons[8].cget("text") == str(players[0]):
        color(2, 5, 8)
        return True
    elif buttons[2].cget("text") == str(players[1]) and buttons[5].cget("text") == str(players[1]) and buttons[5].cget("text") == str(players[1]):
        color(2, 5, 8)
        return True

    if buttons[0].cget("text") == str(players[0]) and buttons[4].cget("text") == str(players[0]) and buttons[8].cget("text") == str(players[0]):
        color(0, 4, 8)
        return True
    elif buttons[0].cget("text") == str(players[1]) and buttons[4].cget("text") == str(players[1]) and buttons[8].cget("text") == str(players[1]):
        color(0, 4, 8)
        return True
    elif buttons[2].cget("text") == str(players[0]) and buttons[4].cget("text") == str(players[0]) and buttons[6].cget("text") == str(players[0]):
        color(2, 4, 6)
        return True
    elif buttons[2].cget("text") == str(players[1]) and buttons[4].cget("text") == str(players[1]) and buttons[6].cget("text") == str(players[1]):
        color(2, 4, 6)
        return True

    temp = 0
    for i in range(9):
        if buttons[i].cget("text") != "":
            temp += 1
    if temp == 9:
        return "Tie"


def end():
    if check_winner() != "Tie":
        label.config(text="{} Wins!".format(player), bg='green')
    else:
        label.config(text="Tie!")
        for i in range(9):
            buttons[i].config(bg='yellow')

    for i in range(9):
        buttons[i].config(state=DISABLED)


def color(x, y, z):
    global buttons

    for i in range(9):
        if i == x or i == y or i == z:
            buttons[i].config(bg='green')
    else:
        buttons[i].config(state=DISABLED)


window = Tk()
window.title("Tic Tac Toe")
window.config(bg='blue')
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

players = ['x', 'o']
player = random.choice(players)

label = Label(window, text="{}'s Turn".format(player), bg='#999999', fg='black',
              font=("Consolas", 30), width=13, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = list()

buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(0)))
buttons[0].grid(row=0, column=0)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(1)))
buttons[1].grid(row=0, column=1)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(2)))
buttons[2].grid(row=0, column=2)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(3)))
buttons[3].grid(row=1, column=0)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(4)))
buttons[4].grid(row=1, column=1)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(5)))
buttons[5].grid(row=1, column=2)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(6)))
buttons[6].grid(row=2, column=0)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(7)))
buttons[7].grid(row=2, column=1)
buttons.append(Button(frame, height=4, width=12, bg='#FFFFFF', fg='black',
                    command=lambda: next_turn(8)))
buttons[8].grid(row=2, column=2)

window.mainloop()