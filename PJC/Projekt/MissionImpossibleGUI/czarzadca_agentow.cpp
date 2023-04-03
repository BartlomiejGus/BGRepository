#include "czarzadca_agentow.h"
#include "cmapa.h"

int CZarzadca_Agentow::ile_agentow = 0;
bool CZarzadca_Agentow::czy_wiemy_gdzie_jest_gracz = false;
SKoordynaty_obiektu CZarzadca_Agentow::wspolrzedne_gracza = {INT_MAX,INT_MAX};

CZarzadca_Agentow::CZarzadca_Agentow()
{
    head = NULL;
}

void CZarzadca_Agentow::Dodaj_kolejnego_agenta(int ktory)
{
    SLista_Agentow *aktualny = NULL;

    if(head==NULL)
    {
        head = new SLista_Agentow;
        aktualny = head;
    }
    else
    {
        aktualny = head;
        while(aktualny->next!=NULL)
        {
            aktualny = aktualny->next;
        }
        aktualny->next = new SLista_Agentow;
        aktualny = aktualny->next;
    }

    aktualny->czy_wiem_gdzie_jest_gracz = false;
    aktualny->ktorym_agentem_jestem = ktory;

    aktualny->next = NULL;
}

void CZarzadca_Agentow::Dodaj_ze_zobaczylem_gracza(int ktory)
{
    SLista_Agentow *aktualny = head;

    while(aktualny->ktorym_agentem_jestem!=ktory)
    {
        aktualny = aktualny->next;
    }

    aktualny->czy_wiem_gdzie_jest_gracz = true;
}

void CZarzadca_Agentow::Zmien_ze_nie_widze_gracza(int ktory)
{
    SLista_Agentow *aktualny = head;

    while(aktualny->ktorym_agentem_jestem!=ktory)
    {
        aktualny = aktualny->next;
    }

    aktualny->czy_wiem_gdzie_jest_gracz = false;
}

void CZarzadca_Agentow::Aktualizujaca_czy_na_pewno_nadal_widze_gracza()
{
    SLista_Agentow *aktualny = head;

    while(aktualny!=NULL)
    {
        if(aktualny->czy_wiem_gdzie_jest_gracz == true)
        {
            return;
        }

        aktualny = aktualny->next;
    }

    czy_wiemy_gdzie_jest_gracz = false;
    wspolrzedne_gracza.R = INT_MAX;
    wspolrzedne_gracza.K = INT_MAX;
}

void CZarzadca_Agentow::Sprawdzajaca_czy_wiemy_gdzie_jest_gracz(CMapa *mapa, int wielkosc_obszaru, SKoordynaty_obiektu aktualne, bool orientacja, bool w_ktora_strone, int ktory)
{
    int ktory_rzad = INT_MAX;
    int ktora_kolumna = INT_MAX;
    int klewo = wielkosc_obszaru;
    int kprawo = wielkosc_obszaru;
    int rgora = wielkosc_obszaru;
    int rdol = wielkosc_obszaru;

    if(czy_wiemy_gdzie_jest_gracz == false)
    {
        Ustawiajaca_do_kazdego_agenta_widocznosc(klewo,kprawo,rgora,rdol,orientacja, w_ktora_strone);
    }

    for(int i = aktualne.R-rgora;i<=aktualne.R+rdol;i++)
    {
        for(int j = aktualne.K-klewo;j<=aktualne.K+kprawo;j++)
        {
            if(i<mapa->Get_liczba_Wierszy()&&i>=0)
            {
                ktory_rzad = i;
            }
            else
            {
                if(i<0)
                {
                    ktory_rzad = 0;
                }
                else if(i>=mapa->Get_liczba_Wierszy())
                {
                    ktory_rzad = mapa->Get_liczba_Wierszy()-1;
                }
            }

            if(j<mapa->Get_liczba_Kolumn()&&j>=0)
            {
                ktora_kolumna = j;
            }
            else
            {
                if(j<0)
                {
                    ktora_kolumna = 0;
                }
                else if(j>=mapa->Get_liczba_Kolumn())
                {
                    ktora_kolumna = mapa->Get_liczba_Kolumn()-1;
                }
            }

            CObiekt *pom = mapa->Get_co_jest_na_mapie(ktory_rzad,ktora_kolumna);

            if(pom!=NULL&&pom->czy_mozna_mnie_sledzic())
            {
                czy_wiemy_gdzie_jest_gracz = true;
                wspolrzedne_gracza.R = ktory_rzad;
                wspolrzedne_gracza.K = ktora_kolumna;
                Dodaj_ze_zobaczylem_gracza(ktory);
                return;
            }
        }
    }

    Zmien_ze_nie_widze_gracza(ktory);
}

void CZarzadca_Agentow::Ustawiajaca_do_kazdego_agenta_widocznosc(int &kl, int &kp, int &rg, int &rd, bool orientacja, bool w_ktora_strone)
{
    if(orientacja==false&&w_ktora_strone==false)// ide w dol
    {
       rg = 0;
    }

    if(orientacja==false&&w_ktora_strone==true)// ide w gore
    {
        rd = 0;
    }

    if(orientacja==true&&w_ktora_strone==false)// ide w prawo
    {
        kl = 0;
    }

    if(orientacja==true&&w_ktora_strone==true)// ide w lewo
    {
        kp = 0;
    }
}

CZarzadca_Agentow::~CZarzadca_Agentow()
{
    SLista_Agentow *aktualny = head;

    while(aktualny!=0)
    {
        head=aktualny->next;
        delete aktualny;
        aktualny = head;
    }
}
