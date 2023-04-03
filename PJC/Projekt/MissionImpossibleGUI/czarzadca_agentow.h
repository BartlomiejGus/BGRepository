#ifndef CZARZADCA_AGENTOW_H
#define CZARZADCA_AGENTOW_H

#include "SKoordynaty.h"

/** \brief Struktura używana do listy w celu weryfikacji czy gracz jest nadal widoczny
 * @param SLista_Agentow::czy_wiem_gdzie_jest_gracz przechowuje informacje czy dany agent wie gdzie jest gracz
 * @param SLista_Agentow::ktorym_agentem_jestem przechowuje informacje który to agent
 * @param SLista_Agentow::next wskaźnik na nastąpną pozycje listy
 */
struct SLista_Agentow
{
    bool czy_wiem_gdzie_jest_gracz;
    int ktorym_agentem_jestem;
    SLista_Agentow *next;
};

class CMapa;

/** \brief Klasa koordynująca zachowanie agentów
 */
class CZarzadca_Agentow
{
private:
    /** wskaźnik przechowujący adres początku listy*/
    SLista_Agentow *head;

public:
    /** \brief Konstruktor zarzadcy agentów, w którym ustawiana jest wartość iniciajlizacyjna adresu początku listy na NULL
     * @see head
     */
    CZarzadca_Agentow();

    /** \brief Przechowuje wartość ilości agentów
     */
    static int ile_agentow;

    /** \brief Przechowuje wartość czy gracz został zauważony przez któregoś z agentów
     */
    static bool czy_wiemy_gdzie_jest_gracz;

    /** \brief Przechowuje wartość aktualnego położenia agentów, jeśli nie został on jeszcze zauważony albo został jego ślad zgubiony to otrzymuje wartości INT_MAX
     */
    static SKoordynaty_obiektu wspolrzedne_gracza;

    /** \brief Dodaje kolejenego agenta do listy
     *@param ktory wartość który agent
     *@see SLista_Agentow
     */
    void Dodaj_kolejnego_agenta(int ktory);

    /** \brief Dodaje do konkretnego agenta, że zobaczył gracza
     *@param ktory wartość który agent
     *@see SLista_Agentow
     */
    void Dodaj_ze_zobaczylem_gracza(int ktory);

    /** \brief Jeśli gracz nie znajduje się w polu widzenia agenta ustawia w liście na jego pozycji wartość czy_wiem_gdzie_jest_gracz równym false
     *@param ktory wartość który agent
     *@see SLista_Agentow
     */
    void Zmien_ze_nie_widze_gracza(int ktory);

    /** \brief Sprawdza czy nadal jest widoczny gracz przez któregoś z agentów
     */
    void Aktualizujaca_czy_na_pewno_nadal_widze_gracza();

    /** \brief Sprawdza czy gracz znajduje się w polu widzenia agenta
     *@param mapa za pomocą tej zmiennej możemy badać czy gracz jest w polu widzenia agenta
     *@param wielkosc_obszaru jak duzy jest przeszukiwany teren w celu znalezienia gracza
     *@param aktualne becne współrzędne agenta
     *@param orientacja w jaki sposób porusza się agent: czy pionowo czy poziomo
     *@param w_ktora_strone porusza się agent
     *@param ktory numer agenta jaki jest teraz sprawdzany
     *@see czy_wiemy_gdzie_jest_gracz
     *@see wspolrzedne_gracza
     */
    void Sprawdzajaca_czy_wiemy_gdzie_jest_gracz(CMapa *mapa, int wielkosc_obszaru, SKoordynaty_obiektu aktualne, bool orientacja, bool w_ktora_strone, int ktory);

    /** \brief Ustawia teren poszukiwań agenta w danej chwili od wartości orentacji i również w którą stronę się porusza agent tak, aby nie widział obszaru za swoimi "plecami". Pomijana w przypadku znalezienia gracza przez agenta
     *@param kl jak daleko widzi agent w lewo
     *@param kp jak daleko widzi agent w prawo
     *@param rg jak daleko widzi agent w górę
     *@param rd jak daleko widzi agent w dół
     *@param orientacja w jaki sposób porusza się agent: czy pionowo czy poziomo
     *@param w_ktora_strone porusza się agent
     *@see Sprawdzajaca_czy_wiemy_gdzie_jest_gracz();
     */
    void Ustawiajaca_do_kazdego_agenta_widocznosc(int &kl, int &kp, int &rg, int &rd, bool orientacja, bool w_ktora_strone);

    /** \brief Usuwana jest w nim lista agentów
     *@see head
     */
    ~CZarzadca_Agentow();
};

#endif // CZARZADCA_AGENTOW_H


//orientacja = false - oznacza, że agent ma się poruszać pionowo
//orientacja = true - oznacza, że agent ma się poruszać poziomo
// jeśli w_ktora_strone jest true to odejmuje do współrzednej
// jeśli w_ktora_strone jest false to dodaje od współrzędnej
