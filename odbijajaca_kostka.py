from tkinter import *
import time

HEIGHT, WIDTH = 900, 900
xVelocity = 8
yVelocity = 0

def jump(event):
    global yVelocity
    yVelocity = -10

window = Tk()

canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg='#FFFFFF')
canvas.pack()
cube = canvas.create_rectangle(0, HEIGHT/3, 50, (HEIGHT/3)+50, fill='black')
canvas.bind("<Button-1>", jump)
cubeWidth = canvas.bbox(cube)[2] - 1
cubeHeight = cubeWidth

while (canvas.coords(cube)[3] < HEIGHT and canvas.coords(cube)[1] >= 0):

    if canvas.coords(cube)[2] >= WIDTH or canvas.coords(cube)[0] < 0:
        xVelocity = -xVelocity

    if yVelocity < 20:
        yVelocity = yVelocity + 0.3
        print(yVelocity)

    canvas.move(cube, xVelocity, yVelocity)
    window.update()
    time.sleep(0.00001)


window.mainloop()
