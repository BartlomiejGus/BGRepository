#ifndef CMAPA_H
#define CMAPA_H

#include <fstream>
#include "cobiekt.h"
#include "cgracz.h"
#include "cagent.h"
#include "csciana.h"
#include "cmeta.h"
#include "cdixtra.h"
#include <QPainter>

using namespace std;

/** \brief Służy do przechowywania liczby wierszy i kolumn mapy
 *@param SWielkosc_mapy::ile_Linijek wartość liczby wierszy mapy
 *@param SWielkosc_mapy::ile_Kolumn wartość liczby kolumn mapy
 */
struct SWielkosc_mapy
{
    int ile_Linijek;
    int ile_Kolumn;
};

/** \brief Klasa mapy, która m.in. wyświetla aktualną mapę
 */
class CMapa
{
private:
    /** Przechowuje wartość świadczącą o liczbie wierszy mapy*/
    int liczba_Wierszy;
    /** Przechowuje wartość świadczącą o liczbie kolumn mapy*/
    int liczba_Kolumn;
    /** Przechowuje wartość tablicy dwuwymiarowej wskaźników obiektów, na której będą tworzone obiekty*/
    CObiekt ***mapa;

    /** \brief Sprawdza jak duża jest mapa wczytywana z pliku
     *@param nazwa pliku w którym zapisana jest mapa
     */
    SWielkosc_mapy Sprawdz_jak_duza(string nazwa);

    /** \brief Wczytuje mape do atrybutu ***mapa
     *@param nazwa pliku w którym zapisana jest mapa
     *@param szybkosc_agenta czas co ile agent może wykonać ruch
     *@see mapa
     *@see CAgent::CAgent
     */
    CObiekt ***Wczytaj_mape(string nazwa, int szybkosc_agenta, int ilu_agentow);

    /** Za pomocą tego atrybuty jest możliwość wyszukiwania najkrótszej ścieżki*/
    CDixtra dixtra;

public:
    CMapa();

    /** \brief Zwraca liczbę wierszy mapy
     * @return liczba wierszy mapy
     * @see liczba_Wierszy
     */
    int Get_liczba_Wierszy();
    /** \brief Zwraca liczbę kolumn mapy
     * @return liczba kolumn mapy
     * @see liczba_Kolumn
     */
    int Get_liczba_Kolumn();

    /** \brief Zwraca wskaźnik na jaki obiekt znajduje się na koordynatach
     * @param x współrzędna rzędu
     * @param y współrzędna kolumny
     * @return wskaźnik na obiekt
     * @see mapa
     */
    CObiekt *Get_co_jest_na_mapie(int x, int y);

    /** \brief Ustawia obiekt na mapie na konkretnych koordynatach
     * @param polozenie koordynaty, na których ma być
     * @param obj jaki obiekt ma być ustawiony na tych koordynaatch
     * @see mapa
     */
    void Set_na_mape(SKoordynaty_obiektu polozenie, CObiekt *obj);

    /** \brief Wczytuje mapę w zależności od poziomu trudności
     * @param jaki_poziom świadczy o poziomie trudności rozgrywki
     * @see Wczytaj_mape();
     */
    void Wczytaj_w_zaleznosci_do_pozimou_trudnosci(string ktora_mapa, int liczba_agentow, int jak_szybko_poruszaja_sie);


    /** \brief Wyświetla całą mapę obiektów
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    void Wyswietl(QPainter& painter);

    /** \brief Wyszukuje najkrótszą drogę do gracza i na tej podstawie zwraca kolejne koordynaty agenta
     *@param agenta aktualne koordynaty agenta
     *@param gracza aktualne koordynaty gracza
     *@see CAgent
     *@see CGracz
     *@see CDixtra
     */
    SKoordynaty_obiektu Znajdz_najkrotsza_do_gracza(SKoordynaty_obiektu agenta, SKoordynaty_obiektu gracza);

    /** \brief Nanosi obecne pozycje pozostałych agentów do tablicy w atrybucie dixtra, w celu braku możliwości poprowadzenia przez nich najkrótszej drogi
     *@param obecnego aktualne koordynaty agenta, który poszukuje
     *@see CDixtra
     */
    void Sprawdzajaca_gdzie_sa_pozostali_agenci(SKoordynaty_obiektu obecnego);

    /** \brief Destruktor mapy w którym kasowana jest mapa z obiektami
     */
    ~CMapa();
};

#endif // CMAPA_H
