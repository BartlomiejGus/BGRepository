import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Przyjete skroty:
#BU - bardzo ujemne
#U - ujemne
#Z - zerowe
#D - dodatnie
#BD - bardzo dodatnie
#

#Koncept zapisu wartosci
#[x_mniejszy,x_wiekszy,wartosc_stala] - dla funkcji o stalej wartosci
#[x_mniejszy,x_wiekszy,y_mniejszy,y_wiekszy] - dla funkcji liniowych
#

przedzialy_dla_polozenia = { 'U':[[[-100,-70,1],'stala',[-70,70,1,0],'liniowa',[70,100,0],'stala'],0],
'D':[[[-100,-70,0],'stala',[-70,70,0,1],'liniowa',[70,100,1],'stala'],0],
}

przedzialy_dla_kata = { 'U':[[[-3.5,-0.2,1],'stala',[-0.2,0.2,1,0],'liniowa',[0.2,3.5,0],'stala'],0],
'D':[[[-3.5,-0.2,0],'stala',[-0.2,0.2,0,1],'liniowa',[0.2,3.5,1],'stala'],0],
}

przedzialy_dla_zmiany_polozenia = { 'U':[[[-20,-18,1],'stala',[-18,18,1,0],'liniowa',[18,20,0],'stala'],0],
'D':[[[-20,-18,0],'stala',[-18,18,0,1],'liniowa',[18,20,1],'stala'],0]
}

przedzialy_dla_zmiany_kata = { 'U':[[[-20,-0.1,1],'stala',[-0.1,0.1,1,0],'liniowa',[0.1,20,0],'stala'],0],
'D':[[[-20,-0.1,0],'stala',[-0.1,0.1,0,1],'liniowa',[0.1,20,1],'stala'],0],
}

#Koncept zapisu dla singletonów
#[wartosc sily,[kolejne wartosci na jaka "odpalila dana regula"]]

wyjscie_jako_singletony = {'BBU':[-960,[]],
'BU':[-440,[]],
'U':[-260,[]],
'D':[260,[]],
'BD':[440,[]],
'BBD':[960,[]],
}

#zapis do wykresu 1, przedstawiajace maksymalne położenie dla położenia dodatniego i ujemnego
wykres_1 = { 'D':[[0,0]],
'U':[[0,0]]
} 


class Regulator_rozmyty:

    def __init__(self):
        self.do_pokazania_wykresow = 1

        self.funkcja_rozmyta_dla_polozenia = pd.DataFrame(przedzialy_dla_polozenia)
        self.funkcja_rozmyta_dla_polozenia.index = ['przedzialy','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_polozenia = self.funkcja_rozmyta_dla_polozenia.T
        self.fnarysuj_wykresy(self.funkcja_rozmyta_dla_polozenia,"Rozmycie wejścia x",0.005)

        self.funkcja_rozmyta_dla_zmiany_polozenia = pd.DataFrame(przedzialy_dla_zmiany_polozenia)
        self.funkcja_rozmyta_dla_zmiany_polozenia.index = ['przedzialy','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_zmiany_polozenia = self.funkcja_rozmyta_dla_zmiany_polozenia.T
        self.fnarysuj_wykresy(self.funkcja_rozmyta_dla_zmiany_polozenia,"Rozmycie wejścia dx",0.005)

        self.funkcja_rozmyta_dla_kata = pd.DataFrame(przedzialy_dla_kata)
        self.funkcja_rozmyta_dla_kata.index = ['przedzialy','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_kata = self.funkcja_rozmyta_dla_kata.T
        self.fnarysuj_wykresy(self.funkcja_rozmyta_dla_kata,"Rozmycie wejścia theta",0.005)

        self.funkcja_rozmyta_dla_zmiany_kata = pd.DataFrame(przedzialy_dla_zmiany_kata)
        self.funkcja_rozmyta_dla_zmiany_kata.index = ['przedzialy','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_zmiany_kata = self.funkcja_rozmyta_dla_zmiany_kata.T
        self.fnarysuj_wykresy(self.funkcja_rozmyta_dla_zmiany_kata,"Rozmycie wejścia dtheta",0.005)

        self.funkcja_rozmyta_dla_wyjscia = pd.DataFrame(wyjscie_jako_singletony)
        self.funkcja_rozmyta_dla_wyjscia.index = ['wartosc','odczyty_wartosci_funkcji']
        self.funkcja_rozmyta_dla_wyjscia = self.funkcja_rozmyta_dla_wyjscia.T
    
        #Odkomentowany sluzy do pokazania wejsciowych funkcji rozmytych i zatrzymania programu na nich
        #plt.show()

        #Zmienne do pierwszego ciekawego wykresu
        self.czas_regulacji = 0
        self.poprzednie_polozenie = 0
        self.poprzednia_predkosc = 0
        self.czy_przekroczylem_zero = 0

        self.macierz_do_pierwszego_wykresu = pd.DataFrame(wykres_1)
        self.macierz_do_pierwszego_wykresu.index = ['1']
        self.macierz_do_pierwszego_wykresu = self.macierz_do_pierwszego_wykresu.T

        self.fig_pierwszy_ciekawy,self.axs_pierwszy_ciekawy = plt.subplots(2)
        self.fig_pierwszy_ciekawy.suptitle('Pierwszy ciekawy wykres: położenie maksymalne po stronie dodanej i ujemnej, konwencja punktów: (położenie, czas osiągnięcia w min)')
        self.fig_pierwszy_ciekawy.tight_layout(pad = 1.5)

        #Zmienne do drugiego ciekawego wykresu
        self.macierz_do_drugiego_ciekawego_wykresu_label = []
        self.macierz_do_drugiego_ciekawego_wykresu_wartosci = []

        self.fig_drugi_ciekawy,self.axs_drugi_ciekawy = plt.subplots()

        self.axs_drugi_ciekawy.tick_params(axis = 'y', labelsize = 9)

        #Opis osi y do drugiego ciekawego wykresu

        #Odnośnie kąta
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('1:IF U-kąt i U-dkąt to BBD-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('2:IF D-kąt i D-dkąt to BBU-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('3:IF D-kąt i U-dkąt to BU-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('4:IF U-kąt i D-dkąt to BD-F')

        #Odnośnie położenia
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('5:IF U-położenie to U-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('6:IF D-położenie to D-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('7:IF U-dpołożenie to U-F')
        self.macierz_do_drugiego_ciekawego_wykresu_label.append('8:IF D-dpołożenia to D-F')

        plt.ion()


    #Sluzy do obliczenia wyjscia regulatora
    def foblicz_wyjscie_regulatora(self,x,theta,dx,dtheta):

        #Rozmyj wejscia
        self.funkcja_rozmyta_dla_polozenia = self.frozmyj_wejscia(x,self.funkcja_rozmyta_dla_polozenia)
        self.funkcja_rozmyta_dla_kata = self.frozmyj_wejscia(theta,self.funkcja_rozmyta_dla_kata)
        self.funkcja_rozmyta_dla_zmiany_polozenia = self.frozmyj_wejscia(dx,self.funkcja_rozmyta_dla_zmiany_polozenia)
        self.funkcja_rozmyta_dla_zmiany_kata = self.frozmyj_wejscia(dtheta,self.funkcja_rozmyta_dla_zmiany_kata)
        # print('--polozenie--')
        # print(self.funkcja_rozmyta_dla_polozenia)
        # print('--kat--')
        # print(self.funkcja_rozmyta_dla_kata)
        # print('--zmiany kat--')
        # print(self.funkcja_rozmyta_dla_zmiany_kata)
        # print('--zmiany polozenia--')
        # print(self.funkcja_rozmyta_dla_zmiany_polozenia)

        #Wnioskowanie
        self.fwnioskowanie()
        #print(self.funkcja_rozmyta_dla_wyjscia)

        #Defuzzyfikacja wyjscia
        defuzzyfikacja_wyjscia = self.fdefuzyfikacja()
        self.fwyczysc_funkcje_rozmyta_wyjsciowa()
        #print(self.funkcja_rozmyta_dla_wyjscia)
        #print(defuzzyfikacja_wyjscia)

        ###Ponizej dotyczy pierwszego ciekawgo wykresu###
        
        self.fsprawdz_czy_przekroczyl_zero(x=x)

        #Przyjety czas probkowania obiektu i tym samym regulatora
        dt = 0.001
        self.czas_regulacji = self.czas_regulacji + dt
        #Dodawanie najdalszych położeń po dodaniej jak i ujemnej stronie
        czy_dodalem_nowy_punkt = self.fdodaj_punkty_do_pierwszego_wykresu(x,dx,self.czas_regulacji)

        #Aktualizacja poprzedniego polozenia i predkosci
        self.poprzednie_polozenie = x
        self.poprzednia_predkosc = dx

        if czy_dodalem_nowy_punkt == 1:
            self.fnarysuj_pierwszy_ciekawy_wykres()

        #print(self.macierz_do_pierwszego_wykresu)
        #print(self.czy_przekroczylem_zero)

        ##Ponizej dotyczy drugiego ciekawgo wykresu###
        if int(self.czas_regulacji*1000) % 2000 == 1:
            self.fnarysuj_drugi_ciekawy_wykres()
        
        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.clear()

        return defuzzyfikacja_wyjscia


    #Słuzy do rozmywania wejscia
    def frozmyj_wejscia(self,zmienna,aktualna_macierz):

        czy_wystepuje_w_danej_funkcji = 0

        for i in range(aktualna_macierz.shape[0]):

            aktualny_wiersz = aktualna_macierz['przedzialy'].loc[aktualna_macierz.index[i]]

            for j in range(0,len(aktualny_wiersz),2):

                aktualny_przedzial = aktualny_wiersz[j]

                if zmienna>aktualny_przedzial[0] and zmienna<=aktualny_przedzial[1]:
                    czy_wystepuje_w_danej_funkcji = 1
                    jaka_to_funkcja = aktualny_wiersz[j+1]
                    wartosc_funkcji =  self.foblicz_wartosc_funkcji(zmienna,jaka_to_funkcja,aktualny_przedzial)
                    break

            if czy_wystepuje_w_danej_funkcji == 1:
                aktualna_macierz['wartosc_rozmyta'].loc[aktualna_macierz.index[i]] = wartosc_funkcji
            else:
                aktualna_macierz['wartosc_rozmyta'].loc[aktualna_macierz.index[i]] = 0

            czy_wystepuje_w_danej_funkcji = 0

        return aktualna_macierz


    #Sluzy do przeprowadzenia wnioskowania
    def fwnioskowanie(self):

        #Dotyczy kata

        #Jezeli (U_kat i U_dkat) to BBD_F
        wartosc_reguly = self.f_and([self.funkcja_rozmyta_dla_kata.loc['U','wartosc_rozmyta'],self.funkcja_rozmyta_dla_zmiany_kata.loc['U','wartosc_rozmyta']])
        self.funkcja_rozmyta_dla_wyjscia.loc['BBD','odczyty_wartosci_funkcji'].append(wartosc_reguly)
        
        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli (D_kat i D_dkat) to BBU_F
        wartosc_reguly = self.f_and([self.funkcja_rozmyta_dla_kata.loc['D','wartosc_rozmyta'],self.funkcja_rozmyta_dla_zmiany_kata.loc['D','wartosc_rozmyta']])
        self.funkcja_rozmyta_dla_wyjscia.loc['BBU','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli (D_kat i U_dkat) to BU_F
        wartosc_reguly = self.f_and([self.funkcja_rozmyta_dla_kata.loc['D','wartosc_rozmyta'],self.funkcja_rozmyta_dla_zmiany_kata.loc['U','wartosc_rozmyta']])
        self.funkcja_rozmyta_dla_wyjscia.loc['BU','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli (U_kat i D_dkat) to BD_F
        wartosc_reguly = self.f_and([self.funkcja_rozmyta_dla_kata.loc['U','wartosc_rozmyta'],self.funkcja_rozmyta_dla_zmiany_kata.loc['D','wartosc_rozmyta']])
        self.funkcja_rozmyta_dla_wyjscia.loc['BD','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Dotyczy polozenia

        #Jezeli U_x to U_F
        wartosc_reguly = self.funkcja_rozmyta_dla_polozenia.loc['U','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_wyjscia.loc['U','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli D_x to D_F
        wartosc_reguly = self.funkcja_rozmyta_dla_polozenia.loc['D','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_wyjscia.loc['D','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli U_dx to U_F
        wartosc_reguly = self.funkcja_rozmyta_dla_zmiany_polozenia.loc['U','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_wyjscia.loc['U','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)

        #Jezeli D_dx to D_F
        wartosc_reguly = self.funkcja_rozmyta_dla_zmiany_polozenia.loc['D','wartosc_rozmyta']
        self.funkcja_rozmyta_dla_wyjscia.loc['D','odczyty_wartosci_funkcji'].append(wartosc_reguly)

        self.macierz_do_drugiego_ciekawego_wykresu_wartosci.append(wartosc_reguly)


    #Sluzy do obliczenia sumy, ktora jest wyznaczana jako minimum
    def f_or(self,lista_wartosci_rozmytych):

        wartosc_fsuma = max(lista_wartosci_rozmytych)
        return wartosc_fsuma


    #Sluzy do obliczenia przeciecia
    def f_and(self,lista_wartosci_rozmytych):

        wartosc_fprzeciecia = min(lista_wartosci_rozmytych)
        return wartosc_fprzeciecia


    #Sluzy do obliczenia dopelnienia
    def f_dop(self,wartosc_przynaleznosci):

        wartosc_dop = 1 - wartosc_przynaleznosci
        return wartosc_dop


    #Sluzy do obliczenia wyjscia z regulatora
    def fdefuzyfikacja(self):

        licznik_dla_singletonu = 0
        mianownik_dla_singletonu = 0

        for i in range(self.funkcja_rozmyta_dla_wyjscia.shape[0]):

            if len(self.funkcja_rozmyta_dla_wyjscia['odczyty_wartosci_funkcji'].loc[self.funkcja_rozmyta_dla_wyjscia.index[i]]) != 0:

                licznik_dla_singletonu = licznik_dla_singletonu + self.funkcja_rozmyta_dla_wyjscia['wartosc'].loc[self.funkcja_rozmyta_dla_wyjscia.index[i]]*self.f_or(self.funkcja_rozmyta_dla_wyjscia['odczyty_wartosci_funkcji'].loc[self.funkcja_rozmyta_dla_wyjscia.index[i]])
                mianownik_dla_singletonu = mianownik_dla_singletonu + self.f_or(self.funkcja_rozmyta_dla_wyjscia['odczyty_wartosci_funkcji'].loc[self.funkcja_rozmyta_dla_wyjscia.index[i]])

        defuzzyfikacja_wyjscia = licznik_dla_singletonu/mianownik_dla_singletonu
        return defuzzyfikacja_wyjscia


    #Sluzy do wyczyszczenia funkcji rozmytej
    def fwyczysc_funkcje_rozmyta_wyjsciowa(self):

        for i in range(self.funkcja_rozmyta_dla_wyjscia.shape[0]):

            self.funkcja_rozmyta_dla_wyjscia['odczyty_wartosci_funkcji'].loc[self.funkcja_rozmyta_dla_wyjscia.index[i]].clear()


    #Sluzy do obliczenia wartosci rozmycia
    def foblicz_wartosc_funkcji(self,x,jaka_to_funkcja,wartosci_funkcji):

        wartosc_funkcji = 0

        if jaka_to_funkcja == 'stala':
            wartosc_funkcji = wartosci_funkcji[2]
        elif jaka_to_funkcja == 'liniowa':
            x_mniejsza = wartosci_funkcji[0]
            x_wieksza = wartosci_funkcji[1]
            y_mniejsza = wartosci_funkcji[2]
            y_wiekszy = wartosci_funkcji[3]

            wspolczynnik_a = (y_mniejsza-y_wiekszy)/(x_mniejsza-x_wieksza)
            wspolczynnik_b = y_mniejsza - wspolczynnik_a*x_mniejsza

            wartosc_funkcji = wspolczynnik_a*x + wspolczynnik_b

        return wartosc_funkcji

    ##########################################################################
    ############## Poniżej część kodu odpowiedzialna za wykresy ##############
    ##########################################################################

    #Wykorzystywana do narysowania wykresow rozmytych wejsc
    def fnarysuj_wykresy(self,aktualna_macierz,tytul,krok):

        x = []
        y = []

        nazwy_kategorii = list(aktualna_macierz.index)

        for i in range(aktualna_macierz.shape[0]):

            aktualny_wiersz = aktualna_macierz['przedzialy'].loc[aktualna_macierz.index[i]]

            for j in range(0,len(aktualny_wiersz),2):

                aktualny_przedzial = aktualny_wiersz[j]
                jaka_to_funkcja = aktualny_wiersz[j+1]

                aktualny_x = np.arange(aktualny_przedzial[0],aktualny_przedzial[1]+krok,krok)

                x.extend(aktualny_x)

                for z in aktualny_x:
                    aktualny_y = self.foblicz_wartosc_funkcji(z,jaka_to_funkcja,aktualny_przedzial)
                    y.append(aktualny_y)

            plt.figure(self.do_pokazania_wykresow)
            plt.plot(x,y)

            x = []
            y = []

        self.do_pokazania_wykresow = self.do_pokazania_wykresow + 1

        plt.title(tytul)

        plt.legend(nazwy_kategorii)
        plt.draw()
        plt.show(block=False)


    #Sluzy do dodania punktow do wykresu pierwszego ciekawego wykresu
    def fdodaj_punkty_do_pierwszego_wykresu(self,x,dx,czas):

        czy_dodalem_nowy_punkt = 0
        
        kolejny_punkt_do_dodania = [0,0]
        if x>0 and dx<0 and self.poprzednia_predkosc>0:
            #print("Jestem")
            kolejny_punkt_do_dodania = [x,czas]

            jaka_ostatnia_komorka = (list(self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))])==[0,0])

            if  ((self.czy_przekroczylem_zero == 0 and abs(self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))][0]) < abs(x))):
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
            elif (self.czy_przekroczylem_zero == 1 and (not jaka_ostatnia_komorka)):
                self.macierz_do_pierwszego_wykresu[str(len(self.macierz_do_pierwszego_wykresu.columns)+1)] = [[0,0],[0,0]]
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
                self.czy_przekroczylem_zero = 0
            elif (self.czy_przekroczylem_zero == 1 and jaka_ostatnia_komorka):
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['D',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
                self.czy_przekroczylem_zero = 0

            czy_dodalem_nowy_punkt = 1

        elif x<0 and dx>0 and self.poprzednia_predkosc<0:
            #print("Jestem")
            kolejny_punkt_do_dodania = [x,czas]

            jaka_ostatnia_komorka = (list(self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))])==[0,0])

            if  ((self.czy_przekroczylem_zero == 0 and abs(self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))][0]) < abs(x))):
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
            elif (self.czy_przekroczylem_zero == 1 and (not jaka_ostatnia_komorka)):
                self.macierz_do_pierwszego_wykresu[str(len(self.macierz_do_pierwszego_wykresu.columns)+1)] = [[0,0],[0,0]]
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
                self.czy_przekroczylem_zero = 0
            elif (self.czy_przekroczylem_zero == 1 and jaka_ostatnia_komorka):
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].clear()
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[0])
                self.macierz_do_pierwszego_wykresu.loc['U',str(len(self.macierz_do_pierwszego_wykresu.columns))].append(kolejny_punkt_do_dodania[1])
                self.czy_przekroczylem_zero = 0

            czy_dodalem_nowy_punkt = 1

        return czy_dodalem_nowy_punkt


    #Sprawdza czy wahadlo przekroczylo zero
    def fsprawdz_czy_przekroczyl_zero(self,x):
        if (x > 0 and self.poprzednie_polozenie < 0) or (x < 0 and self.poprzednie_polozenie > 0):
            self.czy_przekroczylem_zero = 1


    #Rysuje pierwszy ciekawy wykres
    def fnarysuj_pierwszy_ciekawy_wykres(self):

        self.axs_pierwszy_ciekawy[0].clear()
        self.axs_pierwszy_ciekawy[1].clear()

        maksymalnie_dodany = len(self.macierz_do_pierwszego_wykresu.columns)
        x = np.arange(1,maksymalnie_dodany+1)

        y_1_polozenie = np.empty(0)
        y_2_polozenie = np.empty(0)

        y_1_czas = np.empty(0)
        y_2_czas = np.empty(0)

        ile_krokow_dla_1 = 0
        ile_krokow_dla_2 = 0

        for idx in range(0,maksymalnie_dodany):

            if self.macierz_do_pierwszego_wykresu.loc['D',str(idx+1)][0] != 0:
                y_1_polozenie = np.append(y_1_polozenie,round(self.macierz_do_pierwszego_wykresu.loc['D',str(idx+1)][0],2))
                y_1_czas = np.append(y_1_czas,round(self.macierz_do_pierwszego_wykresu.loc['D',str(idx+1)][1]/60,2))
                ile_krokow_dla_1 = ile_krokow_dla_1 + 1

        for idx in range(0,maksymalnie_dodany):

            if self.macierz_do_pierwszego_wykresu.loc['U',str(idx+1)][0] != 0:
                y_2_polozenie = np.append(y_2_polozenie,round(self.macierz_do_pierwszego_wykresu.loc['U',str(idx+1)][0],2))
                y_2_czas = np.append(y_2_czas,round(self.macierz_do_pierwszego_wykresu.loc['U',str(idx+1)][1]/60,2))
                ile_krokow_dla_2 = ile_krokow_dla_2 + 1

        x_1 = np.arange(1,ile_krokow_dla_1+1)
        x_2 = np.arange(1,ile_krokow_dla_2+1)

        self.axs_pierwszy_ciekawy[0].plot(x_1,y_1_polozenie,'go--')
        self.axs_pierwszy_ciekawy[0].grid()
        self.axs_pierwszy_ciekawy[0].set_title("Maksymalne położenia po stronie dodatniej")
        self.axs_pierwszy_ciekawy[0].set_ylabel("Położenie")
        self.axs_pierwszy_ciekawy[0].set_xlabel("Które następne maksymalne wychylenie po stronie dodatniej")
        self.axs_pierwszy_ciekawy[1].plot(x_2,y_2_polozenie,'ro--')
        self.axs_pierwszy_ciekawy[1].grid()
        self.axs_pierwszy_ciekawy[1].set_title("Maksymalne położenia po stronie ujemnej")
        self.axs_pierwszy_ciekawy[1].set_ylabel("Położenie")
        self.axs_pierwszy_ciekawy[1].set_xlabel("Które następne maksymalne wychylenie po stronie ujemnej")

        #Do opisywania punktów 
        for i,j in zip(x_1,y_1_polozenie):
            self.axs_pierwszy_ciekawy[0].annotate(str(j) + ',' + str(y_1_czas[i-1]) ,xy=(i,j+0.001))
    
        for i,j in zip(x_2,y_2_polozenie):
            self.axs_pierwszy_ciekawy[1].annotate(str(j) + ',' + str(y_2_czas[i-1]) ,xy=(i,j-0.001))

        plt.draw()
        plt.show()
        

    #Sluzy do narysowania drugiego ciekawego wykresu
    def fnarysuj_drugi_ciekawy_wykres(self):

        self.axs_drugi_ciekawy.clear()

        ile_regul = np.arange(len(self.macierz_do_drugiego_ciekawego_wykresu_label))

        self.axs_drugi_ciekawy.barh(ile_regul,self.macierz_do_drugiego_ciekawego_wykresu_wartosci)

        self.axs_drugi_ciekawy.set_xlabel('W jakim stopniu "odpaliła" dana reguła?')
        self.axs_drugi_ciekawy.set_title("Drugi ciekawy wykres: pokazujący jak bardzo odpaliła dana reguła")
        self.axs_drugi_ciekawy.set_yticks(ile_regul, labels = self.macierz_do_drugiego_ciekawego_wykresu_label)
        self.axs_drugi_ciekawy.invert_yaxis()

        plt.draw()
        plt.show()
