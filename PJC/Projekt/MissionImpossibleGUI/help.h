#ifndef HELP_H
#define HELP_H

#include <QDialog>

namespace Ui {
class Help;
}

/** \brief Klasa okna zasady gry
 */
class Help : public QDialog
{
    Q_OBJECT
    
public:
    explicit Help(QWidget *parent = 0);
    ~Help();
    
private:
    /** Możliwość m.in rysowania i pisania na oknie*/
    Ui::Help *ui;
};

#endif // HELP_H
