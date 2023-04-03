#ifndef CGRACZ_H
#define CGRACZ_H

#include "cobiekt.h"

/** \brief Klasa gracza
 *@see CObiekt
 */
class CGracz : public CObiekt
{
public:
    /** \brief Konstruktor gracza ustawia początkowe jego koordynaty
     * @see CObiekt
     */
    CGracz(int x, int y);

    /** \brief Poruszanie graczem za pomocą klawisza, który naciśnął użytkownik
     *@param mapa możemy sprawdzić czy gracz nie wszedł na pole gdzie jest mapa i tym samym czy już nie wygrał rozgrywki
     *@param sterowanie przekazanie jaki klawisz został naciśnięty przez użytkownika i na podstawie tego następuje ruch gracza
     *@retval Nic świadczy o braku złapania gracza przez agenta
     *@retval Wygrana świadczy o pomyślnej ucieczce agenta
     */
    virtual Rezultat_Ruchu Ruch(CMapa* mapa, int sterowanie);

    /** \brief Wyświetla aktualne położenie gracza jako niebieskie koło
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    virtual void Wyswietl(QPainter& painter);

    /** \brief Określa czy obiekt może być śledzony
     *@retval True świadczy o tym,że obiekt ten może być śledzony
     */
    virtual bool czy_mozna_mnie_sledzic();

    /** \brief Określa czy można wejść w dany obiekt
     *@retval False świadczy o tym, że na tych koordynatach znajduje się obiekt w którego nie można wejść
     */
    virtual bool czy_mozna_we_mnie_wejsc();
};

#endif // CGRACZ_H
