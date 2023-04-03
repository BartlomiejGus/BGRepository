#include "cobiekt.h"

CObiekt::CObiekt(int x, int y)
{
    koordynaty.R=x;
    koordynaty.K=y;
}

SKoordynaty_obiektu CObiekt::Get_koordynaty()
{
    return koordynaty;
}

void CObiekt::Set_koordynaty(SKoordynaty_obiektu wspolrzedne)
{
    koordynaty=wspolrzedne;
}

Rezultat_Ruchu CObiekt::Ruch(CMapa *mapa, int sterowaie)
{
    return Nic;
}


bool CObiekt::czy_za_pomoca_mnie_mozna_wygrac()
{
    return false;
}

bool CObiekt::czy_mozna_we_mnie_wejsc()
{
    return true;
}

bool CObiekt::czy_mozna_mnie_sledzic()
{
    return false;
}

bool CObiekt::czy_mozna_za_pomoca_mnie_przegrac()
{
    return false;
}
