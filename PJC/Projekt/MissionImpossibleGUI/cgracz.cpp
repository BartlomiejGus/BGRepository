#include "cgracz.h"
#include "cmapa.h"
#include "Stale.h"

CGracz::CGracz(int x, int y): CObiekt (x,y)
{
}

void CGracz::Wyswietl(QPainter& painter)
{
    SKoordynaty_obiektu koordynaty = Get_koordynaty();
    QPoint p = {koordynaty.K * WIELKOSC_KAFELKA + WIELKOSC_KAFELKA / 2, koordynaty.R * WIELKOSC_KAFELKA + WIELKOSC_KAFELKA / 2};
    QBrush brush(QColor(0,0,255));
    painter.setBrush(brush);
    painter.drawEllipse(p, WIELKOSC_KAFELKA / 2, WIELKOSC_KAFELKA / 2);
}

bool CGracz::czy_mozna_mnie_sledzic()
{
    return true;
}

bool CGracz::czy_mozna_we_mnie_wejsc()
{
    return false;
}

Rezultat_Ruchu CGracz::Ruch(CMapa *mapa, int sterowanie)
{
    SKoordynaty_obiektu aktualne = Get_koordynaty();

    switch(sterowanie)
    {
        case 87:
            aktualne.R--;
            break;

        case 83:
            aktualne.R++;
            break;

        case 68:
            aktualne.K++;
            break;

        case 65:
            aktualne.K--;
            break;

    }

    CObiekt *pom = mapa->Get_co_jest_na_mapie(aktualne.R,aktualne.K);
    Set_koordynaty(aktualne);

    if(pom!=NULL&&pom->czy_za_pomoca_mnie_mozna_wygrac())
    {
        return Wygrana;
    }

    return Nic;
}
