from tkinter import *

def press_button(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text

    try:
        equation_text = str(eval(equation_text))
        equation_label.set(equation_text)
    except ZeroDivisionError:
        equation_label.set("ZeroDivisionError")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Wrong Syntax")
        equation_text = ""

def clear():
    global equation_text

    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.title("Kalkulator")
window.config(bg='#27025e')

equation_text = ""
equation_label = StringVar()

frame = Frame(window, bg='#27025e')
frame.pack()

label = Label(frame, textvariable=equation_label, width=17, height=2, bg='#FFFFFF', font=('Consolas', 25))
label.grid(row=0, column=0, columnspan=4)

button1 = Button(frame, text=1, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(1))
button1.grid(row=1, column=0)

button2 = Button(frame, text=2, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button(0))
button0.grid(row=4, column=0)

decimal = Button(frame, text='.', font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button('.'))
decimal.grid(row=4, column=1)

equal = Button(frame, text='=', font='SelawikSemibold', width=8, height=4, bg='#999999', command=equal)
equal.grid(row=4, column=2)

plus = Button(frame, text='+', font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button('+'))
plus.grid(row=1, column=3)

minus = Button(frame, text='-', font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button('-'))
minus.grid(row=2, column=3)

multiply = Button(frame, text='*', font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button('*'))
multiply.grid(row=3, column=3)

divide = Button(frame, text='/', font='SelawikSemibold', width=8, height=4, bg='#999999', command=lambda: press_button('/'))
divide.grid(row=4, column=3)

clear = Button(frame, text='Clear', font='SelawikSemibold', width=12, height=4, bg='#999999', command=clear)
clear.grid(row=5, column=1, columnspan=2)

window.mainloop()
