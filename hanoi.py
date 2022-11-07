def main():
    n = -1
    while n <=0 or n > 12:
        n = int(input("Podaj ilość krążków: ")) #wprowadzamy ilość krążków
    k = 3 # ilość wież
    wynik = str(n) + "\n" + str(k) + "\n"

    A = list() #[]
    B = list() #[]
    C = list() #[]
    if n % 2 == 1:
        A.append(int(n/2 + 1))
    for i in reversed(range(int(n/2))):
        A.append(i+1)
        A.append(i+1)
    print(A, B, C)
    #A = [1, 2, ..., n]
    #B = []
    #C = []

    while len(A) != 1:
        for i in range(2):
            if len(B) % 2 != 0 or len(B) == 0:
                if (len(B) == 0 or B[-1] >= A[-1]) and len(A) != 0:
                    B.append(A[-1])
                    A.pop()
                    wynik += "1 2\n"
                    print(A, B, C)
                elif A[-1] >= B[-1] and len(B) != 0:
                    A.append(B[-1])
                    B.pop()
                    wynik += "2 1\n"
                    print(A, B, C)
            if len(C) % 2 != 0 or len(C) == 0:
                if (len(C) == 0 or C[-1] >= A[-1]) and len(A) != 0:
                    C.append(A[-1])
                    A.pop()
                    wynik += "1 3\n"
                    print(A, B, C)
                elif A[-1] >= C[-1] and len(C) != 0:
                    A.append(C[-1])
                    C.pop()
                    wynik += "3 1\n"
                    print(A, B, C)
            if len(C) % 2 != 0 or len(C) == 0:
                if C[-1] >= B[-1] and len(B) != 0:
                    C.append(B[-1])
                    B.pop()
                    wynik += "2 3\n"
                    print(A, B, C)
                elif B[-1] >= C[-1] and len(C) != 0:
                    B.append(C[-1])
                    C.pop()
                    wynik += "3 2\n"
                    print(A, B, C)

    print()
    print(wynik)
    plik = open("wynik.txt", "w")
    plik.write(wynik)
    plik.close()


if __name__ == "__main__":
    main()


