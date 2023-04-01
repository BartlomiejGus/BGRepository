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
    setWindowTitle("Konwerter z IEEE 754 do kodu wewnętrznego");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_konwertuj_pushButton_clicked()
{
    QString ieee754bin_string = ui->ieee754bin_lineEdit->text();
    bool czyWchodzic = true;
    bool czySameZera = true;
    for(int i = 0 ; i<32 ; i++)
    {
        if(!(ieee754bin_string[i] == '1' || ieee754bin_string[i] == '0'))
        {
            czyWchodzic = false;
        }
        if(ieee754bin_string[i] == '1')
        {
            czySameZera = false;
        }
    }
    if(ieee754bin_string.size() == 32 && czyWchodzic == true)
    {

        if(czySameZera == false)
        {
            bitset<32> set2(ieee754bin_string.toStdString());

            stringstream ss2;

            ss2 << hex << set2.to_ulong();

            ui->ieee754hex_lineEdit->setText(QString::fromStdString(ss2.str()));
            QList <QChar> ieee754Lista;
            for(int i = 0; i< 32; i++)
            {
                ieee754Lista.append(ieee754bin_string[i]);
            }
            int miejsceOstatniego0 = 99;

            for(int i = 1 ; i<9 ; i++)
            {
                if(ieee754Lista[i] == '0')
                {
                    miejsceOstatniego0 = i;
                }
            }
            if(miejsceOstatniego0 != 99)
            {
                ieee754Lista[miejsceOstatniego0] = '1';
                for(int i = miejsceOstatniego0 + 1 ; i<9 ; i++)
                {
                    ieee754Lista[i] = '0';

                }
            }
            ieee754Lista.insert(9,ieee754Lista[0]);
            ieee754Lista.removeFirst();

            QString wewbin;
            for(int i = 0; i< 32; i++)
            {
                wewbin[i] = ieee754Lista[i];
            }
            ui->wewbin_lineEdit->setText(wewbin);

            bitset<32> set(wewbin.toStdString());

            stringstream ss;

            ss << hex << set.to_ulong();

            ui->wewhex_lineEdit->setText(QString::fromStdString(ss.str()));
        }
        else if(czySameZera == true)
        {
            ui->ieee754hex_lineEdit->setText("00000000");
            ui->wewbin_lineEdit->setText(ieee754bin_string);
            ui->wewhex_lineEdit->setText("00000000");
        }
    }
    else if(ieee754bin_string.size() != 32)
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
