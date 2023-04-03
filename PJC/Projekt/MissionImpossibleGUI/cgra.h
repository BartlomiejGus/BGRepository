#ifndef CGRA_H
#define CGRA_H

#include "cmapa.h"
#include "cobiekt.h"
#include <QWidget>

/** \brief Klasa koordynująca przebieg gry
 */
class CGra
{
public:
    /** \brief Struktura, która jest używana do sprawdzenia, czy gracz już wygrał a może przegrał
     * @param SCzy_koniec::czy_wygrales przechowuje wartość logiczną true jeśli gracz wygrał, nominalnie przechowuje wartość false
     * @param SCzy_koniec::czy_przegrales przechowuje wartość logiczna true jeśli gracz przegrał, nominalnie przechowuje warość false
     * @see Kolejna_klatka()
     */
    struct SCzy_koniec
    {
        bool czy_wygrales;
        bool czy_przegrales;
    };

private:
    /** przechowuje wartość, która świadczy o zakończeniu rozgrywki albo wygrania albo przegrania*/
    SCzy_koniec koniec;

    /** przechowuje wartość o nazwie mapy*/
    string ktora_mapa;

    /** przechowuje wartość o liczbie agentow*/
    int liczba_agentow;

    /** przechowuje wartość o predkosci ruchu*/
    int jak_szybko_agenci_sie_ruszaja;

    /** mapa rozgrywki*/
    CMapa map;

    /** \brief Powoduje ruch wszystkich obiektów na mapie
     * @param sterowanie służy do poruszania samym graczem
     * @see Kolejna_klatka()
     */
    void Ruch_obiektow(int &sterowanie);

    /** \brief Powoduje ustawianie wszystkich obiektów na kolejnych koordynatach zgodnie z funkcją Ruch_obiektow
     * @see Kolejna_klatka();
     * @see Ruch_obiektow();
     */
    void Ustawienie_obiektow();

public:
    /** \brief Ustawia początkowe wartości czy wygrałeś - 0, czy przegrałeś - 0
     * @see SCzy_koniec::czy_wygrales
     * @see SCzy_koniec::czy_przegrales
     */
    CGra();

    /** \brief Umożliwia ruch obiektów jak i ich późniejsze ustawienie na nowych koordynatach
     * @param control służy do poruszania samym graczem
     * @see Kolejna_klatka();
     * @see Ruch_obiektow();
     */
    SCzy_koniec Kolejna_klatka(int &control);

    /** \brief Wyswietla aktualną mapę/
     * @param painter pozwala na rysowanie dowolnego kształtu
     * @see CMapa::Wyswietl();
     */
    void Wyswietl_aktualna(QPainter &painter);

    /** \brief Wczytuje mapę w zależności od poziomu.
     * @param level poziom trudności rozgrywki
     * @see Kolejna_klatka();
     * @see Ruch_obiektow();
     */
    void Wczytaj_w_zaleznosci_od_poziomu(string jaka_mapa, int ilu_agentow, int jak_szybko_sie_poruszaja);

    /** \brief Zwraca nazwe mapy
     * @return nazwa mapy
     * @see ktora_mapa
     */
    string Get_ktora_mapa();

    /** \brief Zwraca liczbe agentow
     * @return nazwa mapy
     * @see liczba_agentow
     */
    int Get_liczba_agentow();

    /** \brief Zwraca szybkosc agentow
     * @return nazwa mapy
     * @see jak_szybko_agenci_sie_ruszaja
     */
    int Get_szybkosc_agentow();

    /** \brief Zwraca liczbę wierszy mapy
     * @return liczba wierszy mapy
     * @see CMapa::liczba_Wierszy
     */
    int Get_liczba_wierszy();
    /** \brief Zwraca liczbę kolumn mapy
     * @return liczba kolumn mapy
     * @see CMapa::liczba_Kolumn
     */
    int Get_liczba_kolumn();
};

#endif // CGRA_H

