from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        x = str(eval(equation_text))
        equation_label.set(str(eval(equation_text)))

        equation_text = str(eval(equation_text))
    except ZeroDivisionError:
        equation_label.set("Imbecil")
    except SyntaxError:
        equation_label.set("Wrong Syntax")

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.title("Kalkulator")
window.config(bg='#DDDDDD')

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, bg='#FFFFFF', fg='black', width=30, height=4)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, width=5, height=5, text=1, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, width=5, height=5, text=2, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, width=5, height=5, text=3, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, width=5, height=5, text=4, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, width=5, height=5, text=5, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, width=5, height=5, text=6, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, width=5, height=5, text=7, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, width=5, height=5, text=8, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, width=5, height=5, text=9, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, width=5, height=5, text=0, command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, width=5, height=5, text='+', command=lambda: button_press('+'))
plus.grid(row=3, column=1)

minus = Button(frame, width=5, height=5, text='-', command=lambda: button_press('-'))
minus.grid(row=3, column=2)

equal = Button(frame, width=5, height=5, text='=', command=equal)
equal.grid(row=3, column=3)

decimal = Button(frame, width=5, height=5, text='.', command=lambda: button_press('.'))
decimal.grid(row=0, column=3)

multiply = Button(frame, width=5, height=5, text='*', command=lambda: button_press('*'))
multiply.grid(row=1, column=3)

divide = Button(frame, width=5, height=5, text='/', command=lambda: button_press('/'))
divide.grid(row=2, column=3)

clear = Button(frame, width=10, height=5, text="Clear", command=clear)
clear.grid(row=4, column=1, columnspan=2)

window.mainloop()