from tkinter import *
from tkinter import messagebox
from sys import setrecursionlimit
import random
import time

setrecursionlimit(5000)


#element osiowy skrajny
def partition(tab, p, r):
    pivot = tab[r]
    i = p - 1

    for j in range(p, r):
        if tab[j] <= pivot:
            i = i + 1
            (tab[i], tab[j]) = (tab[j], tab[i])

    (tab[i + 1], tab[r]) = (tab[r], tab[i + 1])

    return i + 1


def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)

#element osiowy pseudolosowy
def randomized_partition(tab, p, r):
    i = random.randint(p, r)
    (tab[r], tab[i]) = (tab[i], tab[r])
    return partition(tab, p, r)


def randomized_quicksort(tab, p, r):
    if p < r:
        q = randomized_partition(tab, p, r)
        randomized_quicksort(tab, p, q-1)
        randomized_quicksort(tab, q+1, r)

#funkcja zwracajaca medianę
def median_of_three(tab, p, r):
    q = (p+r-1)//2
    a = tab[p]
    b = tab[q]
    c = tab[r-1]
    if a <= b <= c:
        return b, q
    if c <= b <= a:
        return b, q
    if a <= c <= b:
        return c, r-1
    if b <= c <= a:
        return c, r-1
    return a, p

#element osiowy bedacy mediana z 3
def median_partition(tab, p, r, ascending = True):
    result = 0
    pivot, pidx = median_of_three(tab, p, r)
    tab[p], tab[pidx] = tab[pidx], tab[p]
    i = p + 1
    for j in range(p + 1, r, 1):
        result += 1
        if (ascending and tab[j] < pivot) or (not ascending and tab[j] > pivot):
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    tab[p], tab[i - 1] = tab[i - 1], tab[p]
    return i - 1, result


def median_quicksort(tab, p, r, ascending = True):
    result = 0
    if p < r:
        q, result = median_partition(tab, p, r, ascending)
        result += median_quicksort(tab, p, q, ascending)
        result += median_quicksort(tab, q + 1, r, ascending)
    return result


def click():
    global result_text
    result_text = ""
    tab = list()

    if len(getN.get()) == 0:
        messagebox.showerror(title='Błąd', message='Proszę wprowadzić rozmiar tablicy!')
        result_text = "Blad! Proszę wpisać poprawny rozmiar tablicy!"
        result_label = result_text
        result.config(text=result_label)
    else:
        if int(getN.get()) <= 0:
            messagebox.showerror(title='Błąd', message='Rozmiar tablicy jest nieprawidłowy!')
            result_text = "Blad! Proszę wpisać poprawny rozmiar tablicy!"
            result_label = result_text
            result.config(text=result_label)
        else:
            n = int(getN.get())
            print(n)
            if x.get() == 0:
                tab = [random.randint(100000, 1000000) for i in range(n)]
                print(tab)
            elif x.get() == 1:
                tab = [random.randint(0, 99) for i in range(n)]
                print(tab)
            elif x.get() == 2:
                tab = [1]
                for i in range(1, n):
                    roznica = random.randint(0, 1000)
                    tab.append(tab[i-1] + roznica)
                print(tab)
            tab_edge = tab
            tab_random = tab
            tab_median = tab

            start = time.time()
            quicksort(tab_edge, 0, n - 1)
            czas = time.time() - start
            result_text += "Ilość elementów: " + str(n) + ", metoda: quicksort, czas wykonania: " + str(czas) + "\n"

            start = time.time()
            randomized_quicksort(tab_random, 0, n - 1)
            czas = time.time() - start
            result_text += "Ilość elementów: " + str(n) + ", metoda: randomizowany quicksort, czas wykonania: " + str(czas) + "\n"

            start = time.time()
            median_quicksort(tab_median, 0, n - 1)
            czas = time.time() - start
            result_text += "Ilość elementów: " + str(n) + ", metoda: quicksort z medianą z 3, czas wykonania: " + str(czas) + "\n\n"

            result_label = result_text
            result.config(text=result_label)
    result.pack()
    print(f'Tablica posortowana: {tab_edge}')


window = Tk()
window.title("Quicksort - porównanie")
window.resizable(False, False)
window.config(bg='#9ca2d9')
frame = Frame(window)
frame.pack()

wyborR = Label(frame, bg='white', width=20, height=2, fg='black', text="wybierz rozmiar tablicy:")
wyborR.pack()

getN = Entry(frame, width=20, font=('Arial', 10))
getN.pack()

result_text = ""
result_label = StringVar()
x = IntVar()
wypelnienie = ["Pseudolosowe z zakresu przekraczającego rozmiar tablicy", "Pseudolosowe z zakresu 0-99", "Uporządkowane niemalejąco"]

wyborM = Label(frame, width=20, height=2, fg='black', text="wybierz metodę:", padx=0)
wyborM.pack(anchor=W)

for i in range(len(wypelnienie)):
    radiobutton = Radiobutton(frame, text=wypelnienie[i], variable=x, value=i)
    radiobutton.pack(anchor=W)

submit = Button(frame, text="Sortuj", bg='lightblue', command=click)
submit.pack()

result = Label(frame, bg='white', text="")

window.mainloop()
