#include "cdixtra.h"
#include <climits>
#include <algorithm>

using namespace std;

CDixtra::CDixtra()
{
}

void CDixtra::Tworzaca_tablice_i_ustawiajaca_jej_poczatkowe_wartosci(int liczba_Wierszy_M, int liczba_Kolumn_M)
{
    liczba_Wierszy_Mapy = liczba_Wierszy_M;
    liczba_Kolumn_Mapy = liczba_Kolumn_M;

    tablica = new Do_Dixtra *[liczba_Wierszy_Mapy];

    for(int i = 0; i<liczba_Wierszy_Mapy; i++)
    {
        tablica[i] = new Do_Dixtra [liczba_Kolumn_Mapy];
    }

    SKoordynaty_obiektu ustalajaca_do_poprzednikow;
    ustalajaca_do_poprzednikow.R = INT_MAX;
    ustalajaca_do_poprzednikow.K = INT_MAX;

    for(int i = 0; i<liczba_Wierszy_Mapy; i++)
    {
        for(int j = 0; j<liczba_Kolumn_Mapy;j++)
        {
            tablica[i][j].koszty = INT_MAX-2;
            tablica[i][j].czy_juz_byl = false;
            tablica[i][j].poprzednik = ustalajaca_do_poprzednikow;
        }
    }
}

void CDixtra::Nanoszaca_sciany_i_mete_na_tablice(int rzad, int kolumna)
{
    tablica[rzad][kolumna].koszty = INT_MAX;
}

void CDixtra::Nanoszaca_pozostalych_agentow(int rzad, int kolumna)
{
    tablica[rzad][kolumna].koszty = INT_MAX-1;
}

void CDixtra::Oblicz(SKoordynaty_obiektu agenta)
{
    tablica[agenta.R][agenta.K].koszty = 0;

    SKoordynaty_obiektu obecnie_przeszukiwany;
    obecnie_przeszukiwany.R = INT_MAX;
    obecnie_przeszukiwany.K = INT_MAX;

    SKoordynaty_obiektu koordynaty_do_sprawdzenia;

    for(int i = 0; i < liczba_Wierszy_Mapy; i++)
    {
        for(int j = 0; j < liczba_Kolumn_Mapy; j++)
        {
            obecnie_przeszukiwany = Znajdz_najmniejszy();
            if(obecnie_przeszukiwany.R<INT_MAX&&obecnie_przeszukiwany.K<INT_MAX)
            {
                tablica[obecnie_przeszukiwany.R][obecnie_przeszukiwany.K].czy_juz_byl = true;

                for(int k = 0; k < 4; k++)
                {
                    if(k == 0)
                    {
                        koordynaty_do_sprawdzenia.R = max(obecnie_przeszukiwany.R - 1, 0);
                        koordynaty_do_sprawdzenia.K = obecnie_przeszukiwany.K;
                    }
                    else if(k == 1)
                    {
                        koordynaty_do_sprawdzenia.R = min(obecnie_przeszukiwany.R + 1,liczba_Wierszy_Mapy - 1);
                        koordynaty_do_sprawdzenia.K = obecnie_przeszukiwany.K;
                    }
                    else if(k == 2)
                    {
                        koordynaty_do_sprawdzenia.R = obecnie_przeszukiwany.R;
                        koordynaty_do_sprawdzenia.K = max(obecnie_przeszukiwany.K - 1, 0);
                    }
                    else if(k == 3)
                    {
                        koordynaty_do_sprawdzenia.R = obecnie_przeszukiwany.R;
                        koordynaty_do_sprawdzenia.K = min(obecnie_przeszukiwany.K + 1,liczba_Kolumn_Mapy - 1);
                    }

                    if((tablica[koordynaty_do_sprawdzenia.R][koordynaty_do_sprawdzenia.K].koszty>tablica[obecnie_przeszukiwany.R][obecnie_przeszukiwany.K].koszty+1)
                            &&tablica[koordynaty_do_sprawdzenia.R][koordynaty_do_sprawdzenia.K].czy_juz_byl==false&&tablica[koordynaty_do_sprawdzenia.R][koordynaty_do_sprawdzenia.K].koszty<INT_MAX-1)
                    {
                        tablica[koordynaty_do_sprawdzenia.R][koordynaty_do_sprawdzenia.K].koszty=tablica[obecnie_przeszukiwany.R][obecnie_przeszukiwany.K].koszty+1;
                        tablica[koordynaty_do_sprawdzenia.R][koordynaty_do_sprawdzenia.K].poprzednik = obecnie_przeszukiwany;
                    }
                }
            }
        }
    }
}

SKoordynaty_obiektu CDixtra::Znajdz_najmniejszy()
{
    int max = INT_MAX;
    SKoordynaty_obiektu do_wyrzucenia;
    do_wyrzucenia.R = INT_MAX;
    do_wyrzucenia.K = INT_MAX;

    for(int i = 0;i<liczba_Wierszy_Mapy;i++)
    {
        for(int j = 0;j<liczba_Kolumn_Mapy;j++)
        {
            if(tablica[i][j].koszty<max && tablica[i][j].czy_juz_byl == false)
            {
                max = tablica[i][j].koszty;
                do_wyrzucenia.R = i;
                do_wyrzucenia.K = j;
            }
        }
    }

    return do_wyrzucenia;
}

void CDixtra::Ustawiajaca_tablice()
{
    SKoordynaty_obiektu poprzednik;
    poprzednik.R = INT_MAX;
    poprzednik.K = INT_MAX;

    for(int  i = 0; i<liczba_Wierszy_Mapy; i++)
    {
        for(int j = 0; j<liczba_Kolumn_Mapy; j++)
        {
            if(tablica[i][j].koszty!=INT_MAX)
            {
                tablica[i][j].koszty = INT_MAX-2;
                tablica[i][j].czy_juz_byl = false;
                tablica[i][j].poprzednik = poprzednik;
            }
        }
    }
}

SKoordynaty_obiektu CDixtra::Get_tablica_poprzednik(SKoordynaty_obiektu obecne)
{
    return tablica[obecne.R][obecne.K].poprzednik;
}

CDixtra::~CDixtra()
{
    for(int i = 0; i<liczba_Wierszy_Mapy; i++)
    {
        delete [] tablica [i];
    }

    delete [] tablica;
}
