#ifndef CDIXTRA_H
#define CDIXTRA_H

#include "SKoordynaty.h"

/** \brief Klasa dixtry służąca do znajdowania najkrótszej ścieżki
 *@see CObiekt
 */
class CDixtra
{
public:
    /** \brief Struktura, która jest używana do tablicy dwuwymiarowej o wymiarach mapy na podstawie, której obliczana jest najkrótsza ścieżka
     * @param Do_Dixtra::koszty koszty dojścia do konkretnej współrzędnej na mapie
     * @param Do_Dixtra::czy_juz_byl służy do sprawdzania, czy dane pole było już branę pod uwagę jako węzeł z którego sprawdzamy
     * @param Do_Dixtra::poprzednik współrzędne pola poprzedniego, które pozwalają dojść jak najkrótszą drogą do obecnego
     */
    struct Do_Dixtra
    {
        int koszty;
        bool czy_juz_byl;
        SKoordynaty_obiektu poprzednik;
    };

private:
    /** liczba wierszy mapy*/
    int liczba_Wierszy_Mapy;
    /** liczba kolumn mapy*/
    int liczba_Kolumn_Mapy;
    /** wskaźnik na tablicę dwuwymiarową, w której są przechowywane m.in. koszty dojścia do poszczególnych współrzędnych */
    Do_Dixtra **tablica;

public:
    CDixtra();

    /** \brief Tworzy tablicę dwuwymiarową i przypisuje jej początkowe wartości: kosztów, czy już był oraz koordynaty poprzednika
     * @param liczba_Wierszy_M liczba wierszy mapy
     * @param liczba_Kolumn_M liczba kolumn mapy
     * @see CDixtra::Do_Dixtra
     * @see tablica
     */
    void Tworzaca_tablice_i_ustawiajaca_jej_poczatkowe_wartosci(int liczba_Wierszy_M, int liczba_Kolumn_M);

    /** \brief Nanosi miejsca ścian i met do tablicy dwuwymiarowej w celu braku możliwości wyliczania przez nie najkrótszych ścieżek
     * @param rzad współrzędna rzędu na mapie
     * @param kolumna współrzędna kolumny na mapie
     * @see tablica
     */
    void Nanoszaca_sciany_i_mete_na_tablice(int rzad, int kolumna);

    /** \brief Nanosi obecne położenie agentów do tablicy dwuwymiarowej w celu braku możliwości wyliczania przez nich najkrótszych ścieżek. Położenia te są modyfikowane przy każdym kolejnym wyszukaniu najkrótszej drogi przez kolejnych agentów.
     * @param rzad liczba wierszy mapy
     * @param kolumna liczba kolumn mapy
     * @see tablica
     */
    void Nanoszaca_pozostalych_agentow(int rzad, int kolumna);

    /** \brief Oblicza koszty dojścia do każdego miejsca na mapie oraz przypisuje każdemu polu jego poprzednika
     * @param agenta obecne koordynaty agenta który wyszukuje najkrótszej drogi do gracza
     * @see Do_Dixtra
     * @see tablica
     */
    void Oblicz(SKoordynaty_obiektu agenta);

    /** \brief Wyszukuje pola o najmniejszym koszcie dojścia, które jeszcze nie było sprawdzane i od niego zaczyna sprawdzać koszty dojść do sąsiadujacych pól
     * @see Oblicz();
     * @see tablica
     * @return Pole obecnie najmniejszym koszcie dojścia, które jeszcze nie było sprawdzzane
     */
    SKoordynaty_obiektu Znajdz_najmniejszy();

    /** \brief Służy do odświeżenia wartości tablicy dwuwymiarowej, aby następny agent mógł obliczyć najkrótszą ścieżkę. Nie odświeża pozycji ścian i mety.
     * @see tablica
     */
    void Ustawiajaca_tablice();

    /** \brief Wzraca współrzędne poprzednich koordynatów dla obecnych koordynatów
     * @param obecne współrzędne dla których poszukujemy koordynatów poprzednika
     * @return Współrzędne poprzednich koordynatów
     * @see tablica
     */
    SKoordynaty_obiektu Get_tablica_poprzednik(SKoordynaty_obiektu obecne);

    /** \brief Destruktor dixtry w której kasowana jest tablica składająca się z elementów Do_Dixtry
     */
    ~CDixtra();

};

#endif // CDIXTRA_H
