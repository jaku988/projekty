#include <iostream>
#include <string.h>
#include <cctype>

using namespace std;

class Wyraz
{
private:
    string wyrazy[9] = { "cops","cannot","catch","me","after","robbing","liquor","store","toofastforyou" };  //pula wyrazow ktory bedziemy zgadywac
    string wyraz;
    int bledy = 0;  // zapisuje ilosc bledow
    int licznik = 0; // zapisuje ile wyrazow zostalo juz odgadnietych
    bool dobrze; // sprawdza czy dany strzal byl dobry (1) czy zly (0)
    char strzal; // zapisuje strzal gracza
    char litera; // pojedyncza litera zmiennej wyraz
    int  n = 0; // rozmiar tablicy strzalow
    char *strzaly = new char[n]; // tablica w ktorej zapisywane sa strzaly gracza
    int x, y; // zmienne przy wybieraniu trudnosci (x) oraz numeru (y) wyrazu
    int dlugosc; //dlugosc wyrazu

    void licznik_bledow() //wywolywana kiedy strzal gracza bedzie niepoprawny
    {
        bledy++;
        if (bledy < 4) cout << "Sprobuj jeszcze raz. Masz jeszcze " << 3 - (bledy - 1) << " szanse" << endl;
        
        else
        {
            cout << "Wykorzystales wszystkie szanse!" << endl;
            cout << "Slowo ktore bylo do odgadniecia to: " << wyraz << endl;
            exit(0);
        }
    }

    void wygrana() //wywolywana kiedy gracz odganie wszystkie litery wyrazu
    {
        cout << endl << "Gratuluje wygranej! " << endl;
        exit(0);
    }

public:
    
    void wybor() // funkcja losujaca wyraz do odgadniecia przez gracza
    {
        cout << "Witaj w grze wisielec, mozesz popelnic 3 bledy, za 4 przegyrwasz. Zapraszam!" << endl;
        cout << "Wybierz poziom trudnosci [1] LATWY        [2] SREDNI        [3] TRUDNY" << endl;
        cin >> x;
        if (x == 1)
        {
            cout << "Wybrales wyraz LATWY     Wybierz [1] [2] [3]";
            cin >> y;
            y = y - 1;
        }
        else if (x == 2)
        {
            cout << "Wybrales wyraz SREDNI     Wybierz [1] [2] [3]";
            cin >> y;
            y = y + 2;
        }
        else if (x == 3)
        {
            cout << "Wybrales wyraz TRUDNY    Wybierz [1] [2] [3]";
            cin >> y;
            y = y + 5;
        }
        else
        {
            cout << "Zly wybor";
        }
        wyraz = wyrazy[y];
        dlugosc = wyraz.length();
    }
    
    void zgadywanie() // wlasciwa gra w wisielca
    {
        cout << "Zapraszam do zgadywania" << endl;
        while (1)
        {
            licznik = 0;
            cout << endl << "Strzelaj!  ";
            for (int i = 0; i < dlugosc; i++)   // wypisuje litery ktore zostaly juz odgadniete
            {
                dobrze = 0;
                litera = wyraz[i];
                for (int j = 0; j < 10; j++)
                {
                    if (litera == strzaly[j])    // jezeli litera zostala odgadnieta to ja wypisuje
                    {
                        cout << litera << " ";
                        licznik++;
                        dobrze = 1;
                        break;
                    }
                }
                if (dobrze != 1)       // jezeli litera nie zostala odgadnieta wpisuje "_"
                {
                    cout << " _ ";
                }
            }
            if (licznik == dlugosc)    // po odgadnieciu wszystkich liter przechodzi dalej
            {
                wygrana();
            }
            cout << "            ";
            cin >> strzal;

            for (int i = 0; i < dlugosc;i++)
            {
                litera = wyraz[i];                  //pobiera strzal od gracza i sprawdza jego poprawnosc
                if (litera == strzal)
                {
                    strzaly[n] = strzal;
                    n++;
                    break;
                }
                else if (i == dlugosc - 1)
                {
                    licznik_bledow();
                }

            }
        }
    }
};

int main()
{
    Wyraz w;
    w.wybor();
    w.zgadywanie();

    return 0;
}
