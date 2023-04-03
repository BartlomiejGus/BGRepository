#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QKeyEvent"
#include "Stale.h"
#include "QMessageBox"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    setWindowTitle("Mission Impossible");
    setWindowIcon(QIcon(QString("Icon.png")));

    connect(&timer, &QTimer::timeout, this, &MainWindow::Kolejna_klatka);
    timer.start(10);
}

void MainWindow::paintEvent(QPaintEvent *e)
{
    QPainter painter;
    painter.begin(this);
    gra.Wyswietl_aktualna(painter);
    painter.end();
}

void MainWindow::keyPressEvent(QKeyEvent *e)
{
    sterowanie = e->key();
}

void MainWindow::Kolejna_klatka()
{
    CGra::SCzy_koniec koniec = gra.Kolejna_klatka(sterowanie);
    if (koniec.czy_przegrales || koniec.czy_wygrales)
    {
        timer.stop();
        QMessageBox koncowa_wiadomosc;
        koncowa_wiadomosc.setWindowTitle("Report");
        koncowa_wiadomosc.setWindowIcon(QIcon(QString("Icon.png")));

        if(koniec.czy_przegrales)
        {
            koncowa_wiadomosc.setIcon(QMessageBox::Information);
            koncowa_wiadomosc.setText("Niestety, przegrałeś. Jeśli chcesz spróbować jeszcze raz naciśnij Reset!");
            koncowa_wiadomosc.setStandardButtons(QMessageBox::Ok | QMessageBox::Reset);
            koncowa_wiadomosc.setDefaultButton(QMessageBox::Reset);
            int ret = koncowa_wiadomosc.exec();

            if(ret == QMessageBox::Reset)
            {
                gra.Wczytaj_w_zaleznosci_od_poziomu(gra.Get_ktora_mapa(),gra.Get_liczba_agentow(),gra.Get_szybkosc_agentow());
                timer.start(10);
            }
            else
            {
                this->close();
                menu->show();
            }
        }

        if(koniec.czy_wygrales)
        {
            koncowa_wiadomosc.setIcon(QMessageBox::Information);
            koncowa_wiadomosc.setText("Brawo wygrałeś!");
            koncowa_wiadomosc.exec();
            this->close();
            menu->show();
        }

    }
    update();
    sterowanie = 0;
}

void MainWindow::Graj_w_zaleznosci_od_poziomu(string ktora_mapa, int ilu_agentow, int jaka_szybkosc_agentow, QDialog *wstep)
{
    menu = wstep;
    gra.Wczytaj_w_zaleznosci_od_poziomu(ktora_mapa,ilu_agentow,jaka_szybkosc_agentow);
    setFixedSize(WIELKOSC_KAFELKA*gra.Get_liczba_kolumn(),WIELKOSC_KAFELKA*gra.Get_liczba_wierszy());
}

MainWindow::~MainWindow()
{
    delete ui;
}
