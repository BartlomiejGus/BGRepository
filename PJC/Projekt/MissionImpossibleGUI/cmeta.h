#ifndef CMETA_H
#define CMETA_H

#include "cobiekt.h"

/** \brief Klasa mety
 *@see CObiekt
 */
class CMeta : public CObiekt
{
public:
    /** \brief Konstruktor miejsc gdzie jest meta ustawia początkowe jej koordynaty
     * @see CObiekt
     */
    CMeta(int x,int y);

    /** \brief Nadpisanie funkcji wirtualnej Rezultat_Ruchu, która zwraca cały czas Nic
     *@param mapa
     *@retval Nic świadczy o braku wygrania i przegrania
     */
    virtual Rezultat_Ruchu Ruch(CMapa* mapa, int sterowanie);

    /** \brief Wyświetla położenie mety jako zielony kwadrat
     *@param painter pozwala na rysowanie dowolnego kształtu
     */
    virtual void Wyswietl(QPainter& painter);

    /** \brief Określa czy za pomocą tego obiektu można wygrać
     *@retval True świadczy o tym, że na tych koordynatach znajduje się obiekt za pomocą którego można wygrać
     */
    virtual bool czy_za_pomoca_mnie_mozna_wygrac();
};

#endif // CMETA_H
