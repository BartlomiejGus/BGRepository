#ifndef CSCIANA_H
#define CSCIANA_H

#include "cobiekt.h"

/** \brief Klasa ścian
 *@see CObiekt
 */
class CSciana : public CObiekt
{
public:
    /** \brief Konstruktor ściany ustawia początkowe jego koordynaty
     * @see CObiekt
     */
    CSciana(int x, int y);

    /** \brief Nadpisanie funkcji wirtualnej Rezultat_Ruchu, która zwraca cały czas Nic
     *@param mapa
     *@retval Nic świadczy o braku wygrania i przegrania
     */
    virtual Rezultat_Ruchu Ruch(CMapa* mapa, int sterowanie);

    /** \brief Wyświetla całą mapę obiektów
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    virtual void Wyswietl(QPainter& painter);

    /** \brief Określa czy można wejść w dany obiekt
     *@retval False świadczy o tym, że na tych koordynatach znajduje się obiekt w którego nie można wejść
     */
    virtual bool czy_mozna_we_mnie_wejsc();
};


#endif // CSCIANA_H
