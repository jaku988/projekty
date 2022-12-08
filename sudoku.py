from tkinter import *


def bottom_click(num):
    global clicked

    bottom_buttons[num].config(bg="blue")
    if clicked != -1:
        bottom_buttons[clicked].config(bg="white")
    clicked = num


window = Tk()
window.title("Sudoku")
window.config(bg='black')
window.resizable(False, False)

main_frame = Frame(window)
main_frame.pack()
frames = list()
for i in range(3):
    for j in range(3):
        x = Frame(main_frame)
        frames.append(x)
        x.grid(row=i, column=j, padx=2, pady=2)

text = StringVar()
board_buttons = list()
for i in range(9):
    for x in range(3):
        for y in range(3):
            button = Button(frames[i], width=5, height=2, text="")
            button.grid(row=x, column=y)
            board_buttons.append(x)

bottom_frame = Frame(window)
bottom_frame.pack()
bottom_buttons = list()
clicked = -1

button1 = Button(bottom_frame, width=5, height=2, text='1', bg="white", command=lambda: bottom_click(0))
button1.grid(row=0, column=0, padx=5)
bottom_buttons.append(button1)

button2 = Button(bottom_frame, width=5, height=2, text='2', bg="white", command=lambda: bottom_click(1))
button2.grid(row=0, column=1, padx=5)
bottom_buttons.append(button2)

button3 = Button(bottom_frame, width=5, height=2, text='3', bg="white", command=lambda: bottom_click(2))
button3.grid(row=0, column=2, padx=5)
bottom_buttons.append(button3)

button4 = Button(bottom_frame, width=5, height=2, text='4', bg="white", command=lambda: bottom_click(3))
button4.grid(row=0, column=3, padx=5)
bottom_buttons.append(button4)

button5 = Button(bottom_frame, width=5, height=2, text='5', bg="white", command=lambda: bottom_click(4))
button5.grid(row=0, column=4, padx=5)
bottom_buttons.append(button5)

button6 = Button(bottom_frame, width=5, height=2, text='6', bg="white", command=lambda: bottom_click(5))
button6.grid(row=0, column=5, padx=5)
bottom_buttons.append(button6)

button7 = Button(bottom_frame, width=5, height=2, text='7', bg="white", command=lambda: bottom_click(6))
button7.grid(row=0, column=6, padx=5)
bottom_buttons.append(button7)

button8 = Button(bottom_frame, width=5, height=2, text='8', bg="white", command=lambda: bottom_click(7))
button8.grid(row=0, column=7, padx=5)
bottom_buttons.append(button8)

button9 = Button(bottom_frame, width=5, height=2, text='9', bg="white", command=lambda: bottom_click(8))
button9.grid(row=0, column=8, padx=5)
bottom_buttons.append(button9)

print(bottom_buttons)

window.mainloop()
