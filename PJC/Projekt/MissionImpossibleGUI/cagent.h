#ifndef CAGENT_H
#define CAGENT_H

#include "cobiekt.h"
#include "czarzadca_agentow.h"
#include <chrono>

using namespace std::chrono;

/** \brief Klasa agentów
 *@see CObiekt
 */
class CAgent : public CObiekt
{
private:
    /** czas co jaki każdy z agentów będzie się poruszał*/
    system_clock::duration krok;
    /** zmienna za pomocą, której sprawdzam czy odpowiedni czas już minął @see krok*/
    system_clock::time_point czas;

    /** orientacja poruszania się gracza: pionowa czy pozioma*/
    bool orientacja;
    /** w ktorą stronę aktualnie się porusza gracz dla pionowej orientacji: czy w górę, czy w dół dla poziomej orientacji: czy w prawo, czy w lewo @see orientacja*/
    bool w_ktora_strone;
    /** numer agenta*/
    int ktory_agent;
    /** jak wielki obszar jest przeszukiwany przez agenta */
    int wielkosc_obszaru_poszukiwan;

public:
    /** \brief Konstruktor agenta w którym przypisywana jest jego początkowe położenie, orientacja, w ktorą stronę się zacznie poruszać, który agent oraz krok
     * @param x współrzędna odpowiadająca rzędowi
     * @param y współrzędna odpowiadająca kolumnie
     * @param orientation orientacja
     * @param krok_agenta co jaki czas agent może się poruszyć
     */
    CAgent(int x, int y, bool orientation, int krok_agenta);

    /** \brief Do momentu braku znalezienia gracza przez jednego z agentów, agent porusza się po linii prostej pionowo albo poziomo w przypadku znalezienia gracza agenta porusza się do niego za pomocą alogrytmu Dixtra
     *@param mapa możemy sprawdzić m.in. czy agent już nie złapał gracza, bo znajduje się za blisko niego
     *@retval Nic świadczy o braku złapania gracz
     *@retval Przegrana świadczy o złapaniu gracza
     *@see CZarzadca_Agentow::czy_wiemy_gdzie_jest_gracz
     *@see CDixtra
     */
    virtual Rezultat_Ruchu Ruch(CMapa *mapa, int sterowanie);

    /** \brief Wyświetla aktualne położenie agent jako czerwone koło
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    virtual void Wyswietl(QPainter& painter);

    /** \brief Określa czy dany obiekt powoduje zakończenie rozgrywki przegraniem
     *@retval True świadczy o tym, że na tych koordynatach znajduje się obiekt, który powoduje przegranie
     */
    virtual bool czy_mozna_za_pomoca_mnie_przegrac();

    /** \brief Określa czy można wejść w dany obiekt
     *@retval False świadczy o tym, że na tych koordynatach znajduje się obiekt w którego nie można wejść
     */
    virtual bool czy_mozna_we_mnie_wejsc();

    /** \brief Określa jednego zarządce dla wszystkich agentów, który m.in. sprawdza czy gracz został zauważony przez jakiegoś agenta i czy nadal go widzimy
     *@see CZarzadca_Agentow::czy_wiemy_gdzie_jest_gracz
     */
    static CZarzadca_Agentow zarzadca;


    /** \brief Powoduje ruch agentów pionowych i zmienia ich kierunek na przeciwny gdy napotka ścianę.
     * @see SKoordynaty_obiektu
     * @return Przyszłe koordynaty agenta
     */
    SKoordynaty_obiektu do_Ruchu_dla_pionowych(CMapa* mapa);

    /** \brief Powoduje ruch agentów poziomych i zmienia ich kierunek na przeciwny gdy napotka ścianę.
     * @see SKoordynaty_obiektu
     * @return Przyszłe koordynaty agenta
     */
    SKoordynaty_obiektu do_Ruchu_dla_poziomych(CMapa* mapa);
};

#endif // CAGENT_H


//orientacja = false - oznacza, że agent ma się poruszać pionowo
//orientacja = true - oznacza, że agent ma się poruszać poziomo
// jeśli w_ktora_strone jest true to odejmuje do współrzednej
// jeśli w_ktora_strone jest false to dodaje od współrzędnej
