#include "mainwindow.h"
#include "wstep.h"
#include <QApplication>
#include <cstdlib>
#include <ctime>

int main(int argc, char *argv[])
{
    srand(time(NULL));
    QApplication a(argc, argv);
    Wstep w;
    w.show();

    return a.exec();
}
