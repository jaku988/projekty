from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def openFile():
    answer = messagebox.askokcancel(title='Uwaga',
                                    message='Czy chcesz wczytać plik?\nUsunie to zawartość pola tekstowego',
                                    icon='warning')
    if answer:
        filepath = filedialog.askopenfilename(title="Podaj plik do edycji",
                                              initialdir="C:\\Users\\Jaku\\PycharmProjects\\pythonProject2",
                                              filetype=(("Text Files", ".txt"), ("All Files", "*.*")))
        if filepath != None:
            file = open(filepath, "r")
            filetext = file.read()
            bufor.delete(1.0, END)
            bufor.insert(1.0, filetext)
            file.close()
    else:
        return

def saveFile():
    file = filedialog.asksaveasfile(title="Podaj plik do edycji",
                                    initialdir="C:\\Users\\Jaku\\PycharmProjects\\pythonProject2",
                                    filetype=(("Text Files", ".txt"), ("All Files", "*.*")))
    if file != None:
        filetext = bufor.get(1.0, END)
        file.write(filetext)
        file.close()

def exit():
    quit()
    

window = Tk()
window.title("Pierwsze zajecia z Pythona")
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

bufor = Text(window, font=("Arial", 15))
bufor.pack()

window.mainloop()
