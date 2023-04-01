#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <bitset>
#include <QMessageBox>
#include <sstream>

using namespace std;


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setFixedSize(440,350);
    setWindowTitle("Konwerter z kodu wewnętrznego do IEEE 754");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_konwertuj_pushButton_clicked()
{
    QString wew = ui->wew_lineEdit->text();
    bool czyWchodzic = true;
    bool czySameZera = true;
    for(int i = 0 ; i<32 ; i++)
    {
        if(!(wew[i] == '1' || wew[i] == '0'))
        {
            czyWchodzic = false;
        }
        if(wew[i] == '1')
        {
            czySameZera = false;
        }
    }

    if(wew.size() == 32 && czyWchodzic == true)
    {
        if(czySameZera == false)
        {
            bitset<32> set2(wew.toStdString());

            stringstream ss2;

            ss2 << hex << set2.to_ulong();

            ui->wewhex_lineEdit->setText(QString::fromStdString(ss2.str()));
            QList <QChar> wewlista;
            for(int i = 0; i< 32; i++)
            {
                wewlista.append(wew[i]);
            }
            wewlista.prepend(wewlista[8]);
            wewlista.removeAt(9);

            int miejsceOstatniej1 = 99;
            bool czySameJedynkiwWykladniku = true;

            for(int i = 1 ; i<9 ; i++)
            {
                if(wewlista[i] == '1')
                {
                    miejsceOstatniej1 = i;
                }
                if(wewlista[i] == '0')
                {
                    czySameJedynkiwWykladniku = false;
                }
            }
            if(czySameJedynkiwWykladniku == false)
            {
                if(miejsceOstatniej1 != 99)
                {
                    wewlista[miejsceOstatniej1] = '0';
                }
                for(int i = miejsceOstatniej1 + 1 ; i<9 ; i++)
                {
                    wewlista[i] = '1';
                }
            }
            QString ieee754;
            for(int i = 0; i< 32; i++)
            {
                ieee754[i] = wewlista[i];
            }
            ui->ieee754_lineEdit->setText(ieee754);

            bitset<32> set(ieee754.toStdString());

            stringstream ss;

            ss << hex << set.to_ulong();

            ui->ieee754hex_lineEdit->setText(QString::fromStdString(ss.str()));

        }
        else if(czySameZera == true)
        {
            ui->ieee754hex_lineEdit->setText("00000000");
            ui->ieee754_lineEdit->setText(wew);
            ui->wewhex_lineEdit->setText("00000000");
        }

    }
    else if(wew.size() != 32)
    {
        QMessageBox informacja;
        informacja.setIcon(QMessageBox::Information);
        informacja.setWindowTitle("Komunikat");
        informacja.setText("Niewłaściwa długość. Powinno być 32 bity.");
        informacja.exec();
    }
    else if(czyWchodzic == false)
    {
        QMessageBox informacja;
        informacja.setIcon(QMessageBox::Information);
        informacja.setWindowTitle("Komunikat");
        informacja.setText("Binarny składa się tylko z 0 i 1.");
        informacja.exec();
    }
}
