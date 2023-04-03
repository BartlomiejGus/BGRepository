#include "help.h"
#include "ui_help.h"

Help::Help(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Help)
{
    ui->setupUi(this);
    setWindowTitle("Zasady gry");
    setWindowIcon(QIcon(QString("Icon_zasady_gry.png")));
    setStyleSheet("background-color:white;");
    setFixedSize(740,180);
}

Help::~Help()
{
    delete ui;
}
