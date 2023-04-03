#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
#include <QDialog>
#include "cgra.h"

namespace Ui {
class MainWindow;
}

/** \brief Klasa głównego okna pokazująca aktualny przebieg rozgrywki
 */
class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    /** \brief Za pomocą tej metody możliwe jest rysowanie obiektów
     *@see CGra::Wyswietl_aktualna();
     */
    virtual void paintEvent(QPaintEvent *e);

    /** \brief Za pomocą tej metody możliwe jest odczytywanie klawisza, który nacisnął użytkownik. Wartość ta następnie jest zapisywana do sterowania
     *@see sterowanie
     */
    virtual void keyPressEvent(QKeyEvent *e);

    /** \brief Za pomocą tej metody możliwe jest wczytanie mapy zgodnej z poziomem trudności jaką wybrał użytkownik
     *@param level poziom trudności
     *@param wstep wskaźnik na menu gry
     *@see menu
     */
    void Graj_w_zaleznosci_od_poziomu(string ktora_mapa, int ilu_agentow, int jaka_szybkosc_agentow, QDialog *wstep);
    
private:
    /** Możliwość m.in rysowania i pisania na oknie*/
    Ui::MainWindow *ui;

    /** menu gry*/
    QDialog *menu;

    /** za pomocą tego atrybutu możemy m.in. wczytać mapę w zależnosci od wybranego poziomu trudności*/
    CGra gra;

    /** odmierza czas w którym kolejna klatka gry będzie możliwa*/
    QTimer timer;

    /** przetrzymuje wartość klawisza, który został wciśnięty przez gracza*/
    int sterowanie;

    /** \brief W tej metodzie odbywa się odczytywanie wartości koniec po każdej kolejnej klatce i jeśli otrzymamy wartość świadczącą o przegraniu lub wygraniu następuje zatrzymanie rozgrywki i pojawienie się komuniaktu dlaczego: wygrania lub przegrania
     *@see CGra::Kolejna_klatka();
     *@see CGra::SCzy_koniec;
     */
    void Kolejna_klatka();
};

#endif // MAINWINDOW_H
