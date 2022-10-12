#include <iostream>

using namespace std;

void pobierz(int n, int * tab);
void wypisz(int n, int * tab);
void zamien_kolejnosc(int n, int * tab);
void wypisz_mniejsze(int n, int * tab, int d);
void wypisz_mniejsze_srednie(int n, int * tab, int g);
void wypisz_parzyste(int n ,int * tab);
bool czyFibPodobna(int n, int * tab);
bool czyPierwsza(int n);
int zliczPierwsze(int n, int * tab);

int main()
{
    int x;
    cout << "Podaj dlugosc tablicy: ";
    cin >> x;
    
    int * tab = new int[x];
    pobierz(x, tab);
    wypisz(x, tab);
    cout << endl;
    zamien_kolejnosc(x, tab);
    wypisz(x, tab);
    cout << endl;
    wypisz_parzyste(x, tab);
    cout << endl;
    cout << "W tablicy znajduje sie " << zliczPierwsze(x, tab) << " liczb pierwszych" << endl;
    
    return 0;
}

void pobierz(int n, int * tab)
{
    for(int i=0; i<n; i++)
    {
        cout << "Podaj liczbe calkowita: ";
        cin >> tab[i];
    }
}

void wypisz(int n, int * tab)
{
    for(int i=0; i<n; i++)
    {
        cout << tab[i] << " ";
    }
}

void zamien_kolejnosc(int n, int * tab)
{
    int temp[n];
    for(int i=0; i<n; i++)
    {
        temp[i] = tab[(n-1)-i];
    }
    
    for(int i=0; i<n; i++)
    {
        tab[i] = temp[i];
    }
}

void wypisz_mniejsze(int n, int * tab, int d)
{
    for(int i=0; i<n; i++)
    {
        if(tab[i] < d) cout << tab[i] << " ";
    }
}

void wypisz_mniejsze_srednie(int n, int * tab, int g)
{
    float srednia, suma = 0;
    
    for(int i=0; i<n; i++)
    {
        suma += tab[i];
    }
    
    srednia = suma / float(n);
    for(int i=0; i<n; i++)
    {
        if(tab[i] < srednia) cout << tab[i] << " ";
    }
}

void wypisz_parzyste(int n, int * tab)
{
    for(int i=0; i<n; i++)
    {
        if(tab[i]%2 == 0) cout << tab[i] << " ";
    }
}

bool czyFibPodobna(int n, int * tab)
{
    for(int i=2; i<n; i++)
    {
        if(tab[i] != tab[i-1] + tab[i-2]) return 0;
    }
    return 1;
}

bool czyPierwsza(int n)
{
    for(int i=2; i<n; i++)
    {
        if(n%i == 0) return 0;
    }
    return 1;
}

int zliczPierwsze(int n, int * tab)
{
    int licznik = 0;
    for(int i=0; i<n; i++)
    {
        if(czyPierwsza(tab[i]) == 1) licznik++;
    }
    return licznik;
}


