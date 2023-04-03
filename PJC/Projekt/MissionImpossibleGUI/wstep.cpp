#include "wstep.h"
#include "ui_wstep.h"

Wstep::Wstep(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Wstep)
{
    ui->setupUi(this);
    setWindowTitle("Mission Impossible");
    setWindowIcon(QIcon(QString("Icon.png")));
    setFixedSize(300,350);

    zasady_gry = new QPushButton("Naciśnij mnie, aby przeczytać zasady gry",this);
    zasady_gry->setGeometry(QRect(QPoint(40,270),QSize(220,40)));
    connect(zasady_gry,&QPushButton::pressed,this,&Wstep::Pressed_zasady);

    QFont f("Arial",15);
    przywitanie = new QLabel("Witaj w Mission Impossible!",this);
    przywitanie->setGeometry(QRect(QPoint(30,1),QSize(250,50)));
    przywitanie->setFont(f);

    f.setPointSize(12);
    wybor_poziomu = new QLabel("Wybierz ustawienia gry:",this);
    wybor_poziomu->setGeometry(QRect(QPoint(80,40),QSize(200,50)));
    wybor_poziomu->setFont(f);

    f.setPointSize(10);
    kto_wykonal = new QLabel("Wykonał: Bartłomiej Guś gr.IPAUT-161",this);
    kto_wykonal->setGeometry(QRect(QPoint(1,310),QSize(300,50)));
    kto_wykonal->setFont(f);

}

void Wstep::Pressed_zasady()
{
    help = new Help();
    help->show();
}

Wstep::~Wstep()
{
    delete ui;
}


void Wstep::on_pushButton_clicked()
{
    bool czy_sie_udalo = true;

    string jaka_mapa = ui->comboBox->currentText().toStdString();
    int ilu_graczy = ui->comboBox_2->currentText().toInt(&czy_sie_udalo);
    int jaka_szybkosc = ui->lineEdit->text().toInt(&czy_sie_udalo);

    if(czy_sie_udalo == true && jaka_szybkosc >= 1 && jaka_szybkosc <= 1000)
    {
        this->hide();
        glowne_okno = new MainWindow();
        glowne_okno->Graj_w_zaleznosci_od_poziomu(jaka_mapa,ilu_graczy,jaka_szybkosc,this);
        glowne_okno->show();
    }
    else if (jaka_szybkosc < 1 || jaka_szybkosc > 1000)
    {
        QMessageBox niepoprawna_szybkosc;
        niepoprawna_szybkosc.setWindowTitle("Report");
        niepoprawna_szybkosc.setWindowIcon(QIcon(QString("Icon.png")));
        niepoprawna_szybkosc.setIcon(QMessageBox::Information);
        niepoprawna_szybkosc.setText("Proszę podać szybkość agentów z przedziału od 1 do 1000.");
        niepoprawna_szybkosc.exec();
    }
}
