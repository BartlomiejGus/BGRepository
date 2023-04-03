#ifndef WSTEP_H
#define WSTEP_H

#include <QDialog>
#include <QPushButton>
#include <QLabel>
#include <QMessageBox>

#include "mainwindow.h"
#include "help.h"

namespace Ui {
class Wstep;
}

/** \brief Klasa okna menu
 */
class Wstep : public QDialog
{
    Q_OBJECT
    
public:
    explicit Wstep(QWidget *parent = 0);
    ~Wstep();
    
private slots:
    void on_pushButton_clicked();

private:
    /** Możliwość m.in rysowania i pisania na oknie*/
    Ui::Wstep *ui;

    /** Główne okno programu, w którym następuje rozgrywka */
    MainWindow *glowne_okno;

    /** Okno w którym wyświetlane są zasady gry */
    Help *help;


    /** Przycisk, który uruchamia pokazanie zasad gry rozgrywki */
    QPushButton *zasady_gry;

    /** Napis przywitania w rozgrywce*/
    QLabel *przywitanie;
    /** Napis nad przyciskiami wyboru poziomu trudności*/
    QLabel *wybor_poziomu;
    /** Napis świadczący o tym kto wykonał projekt*/
    QLabel *kto_wykonal;

    /** \brief Metoda, która wyzwala wyświetlenie zasad gry
     *@see zasady_gry
     */
    void Pressed_zasady();
};

#endif // WSTEP_H
