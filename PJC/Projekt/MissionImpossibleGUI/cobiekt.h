#ifndef COBIEKT_H
#define COBIEKT_H

#include "SKoordynaty.h"
#include <QPainter>

using namespace std;

/** \brief Pozwala na określenie podczas ruchu agenta, czy doszło już może do wygrania albo do przegrania
 * @param Nic świadczy o tym, że rozgrywka toczy się dalej
 * @param Przegrana świadczy o tym, że rozgrywka zakończy się przegraną
 * @param Wygrana świadczy o tym, że rozgrywka zakończy się wygraną
 */
enum Rezultat_Ruchu
{
    Nic,
    Przegrana,
    Wygrana
};

class CMapa;

/** \brief Klasa obiektów mapy
 */
class CObiekt
{

private:
    /** Koordynaty obietku*/
    SKoordynaty_obiektu koordynaty;

public:
    /** \brief Konstruktor obiektu ustawia początkowe jego koordynaty
     * @see koordynaty
     */
    CObiekt(int x, int y);

    /** \brief Zwraca koordynaty obiektu zapisane w nim
     * @see koordynaty
     * @return zwraca koordynaty obiektu, które są w nim zapisane
     */
    SKoordynaty_obiektu Get_koordynaty();

    /** \brief Ustawia koordyanty obiektu
     * @param wspolrzedne na które ma zostać przeniesiony obiekt
     * @see koordynaty
     */
    void Set_koordynaty(SKoordynaty_obiektu wspolrzedne);

    /** \brief Funkcja umożliwiająca ruch dla wszystkich obiektów oprócz gracza
     *@param mapa możemy sprawdzić m.in. czy agent już nie złapał gracza, bo zanajduje się za blisko niego
     *@retval Nic świadczy o braku złapania gracz
     *@retval Przegrana świadczy o złapaniu gracza
     */
    virtual Rezultat_Ruchu Ruch(CMapa *mapa, int sterowaie);

    /** \brief Rysuje odpowiedni kształt na koordynatach obiektu
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    virtual void Wyswietl(QPainter& painter)=0;

    /** \brief Określa czy za pomocą tego obiektu można wygrać
     *@retval True świadczy o tym, że na tych koordynatach znajduje się obiekt za pomocą którego można wygrać
     *@retval False świadczy o tym, że na tych koordynaatch znajduje się obiekt za pomocą którego nie mozna wygrać
     */
    virtual bool czy_za_pomoca_mnie_mozna_wygrac();

    /** \brief Określa czy można wejść w dany obiekt
     *@retval True świadczy o tym, że na tych koordynatach znajduje się obiekt w który można wejść
     *@retval False świadczy o tym, że na tych koordynatach znajduje się obiekt w którego nie można wejść
     */
    virtual bool czy_mozna_we_mnie_wejsc();

    /** \brief Określa czy obiekt może być śledzony
     *@retval True świadczy o tym, że obiekt ten może być śledzony
     *@retval False świadczy o tym, że obiekt ten nie może być śledzony
     */
    virtual bool czy_mozna_mnie_sledzic();

    /** \brief Określa czy dany obiekt powoduje zakończenie rozgrywki przegraniem
     *@retval True świadczy o tym, że na tych koordynatach znajduje się obiekt, który powoduje przegranie
     *@retval False świadczy o tym, że na tych koordynatach znajduje się obiekt, który nie powoduje przegrania
     */
    virtual bool czy_mozna_za_pomoca_mnie_przegrac();
};

#endif // COBIEKT_H
