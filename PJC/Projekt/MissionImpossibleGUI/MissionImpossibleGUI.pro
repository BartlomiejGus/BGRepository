#-------------------------------------------------
#
# Project created by QtCreator 2021-04-26T19:31:18
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = MissionImpossibleGraphical
TEMPLATE = app
CONFIG += c++11

SOURCES += \
    mainwindow.cpp \
    main.cpp \
    help.cpp \
    czarzadca_agentow.cpp \
    csciana.cpp \
    cobiekt.cpp \
    cmeta.cpp \
    cmapa.cpp \
    cgracz.cpp \
    cgra.cpp \
    cdixtra.cpp \
    cagent.cpp \
    wstep.cpp

HEADERS  += \
    mainwindow.h \
    help.h \
    czarzadca_agentow.h \
    csciana.h \
    cobiekt.h \
    cmeta.h \
    cmapa.h \
    cgracz.h \
    cgra.h \
    cdixtra.h \
    cagent.h \
    wstep.h \
    Stale.h \
    SKoordynaty.h

FORMS    += \
    mainwindow.ui \
    help.ui \
    wstep.ui

RESOURCES += \
    grafika.qrc
