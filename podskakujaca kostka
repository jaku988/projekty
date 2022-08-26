from tkinter import *
import time

SPEED = 10
JUMPSPEED = 10
FALLVELOCITY = -10

def jump(event):

    yVelocity = 10
    fallVelocity = -10

    while True:
        x = label.winfo_x()
        y = label.winfo_y()
        coordinates = [x, y]
        label.place(x=x, y=(y-yVelocity))

        if yVelocity > fallVelocity:
            yVelocity = yVelocity - 0.5
        if yVelocity == fallVelocity:
            break

        print(yVelocity)
        print(coordinates)
        time.sleep(0.001)
        window.update()

def go_up(event):
    label.place(x=label.winfo_x(), y=(label.winfo_y() - SPEED))

def go_down(event):
    label.place(x=label.winfo_x(), y=(label.winfo_y() + SPEED))

def go_left(event):
    label.place(x=(label.winfo_x() - SPEED), y=label.winfo_y())

def go_right(event):
    label.place(x=(label.winfo_x() + SPEED), y=label.winfo_y())

window = Tk()
window.title("Test")
window.geometry("500x500")

label = Label(window, bg='red', width=10, height=5)
label.place(x=200, y=200)

window.bind("<space>", jump)
window.bind("<w>", go_up)
window.bind("<a>", go_left)
window.bind("<s>", go_down)
window.bind("<d>", go_right)

window.mainloop()
