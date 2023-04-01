from cmath import inf
from Projekt_297415_CGraf import *

#Implementacja algorytmu A*
class CA_star:
    
    graf = ""
    lista_rozpatrywanych = []
    trasa = []

    def __init__(self,sciezka):

        self.graf = CGraf(sciezka)

        # print(self.graf.macierz_grafu)

        #Wyszukuje wierzholek startowy
        wierzholek_startowy = self.graf.macierz_grafu[self.graf.macierz_grafu['jaki_to_punkt']=='startowy'].index.values[0]

        #Dodaje wierzholek startowy do listy rozpatrywanych
        self.lista_rozpatrywanych.append(wierzholek_startowy)

        #Algorytm A*
        self.fA_star()

        #print(self.graf.macierz_grafu)

        #Drukuje trase od punktu poczatkowego do koncowego albo brak sciezki
        print(' '.join(str(element) for element in self.trasa))

    def fA_star(self):

        wierzcholek_koncowy = self.graf.macierz_grafu[self.graf.macierz_grafu['jaki_to_punkt']=='koncowy'].index.values[0]

        while len(self.lista_rozpatrywanych)!=0:
            
            wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych = self.fsprawdz_ktory_ma_najmniejsza_wartosc()

            if wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych == wierzcholek_koncowy:
                self.fzrekonstruuj_trase(wierzcholek_koncowy)
                return
            
            #Wyszukuje wierzcholek o najmniejszym f
            index_rozpatrywanego = self.lista_rozpatrywanych.index(wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych)

            #Usuwam z listy rozpatrywanej
            del self.lista_rozpatrywanych[index_rozpatrywanego]

            macierz_kosztu_dla_rozpatrywanego = self.graf.macierz_grafu.loc[wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych,'macierz_kosztu']

            #Iterator zgodny z wierzcholkami, szukam nowych wierzcholkow o mniejszej koszcie niz dotychczas jak i dodaje je do listy rozpatrywanych jesli jeszcze nie ma go
            for iterator in range(1,self.graf.liczba_wierzcholkow+1):
                

                if macierz_kosztu_dla_rozpatrywanego[iterator-1] > 0:
                    tymczasowe_g = self.graf.macierz_grafu.loc[wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych,'g'] + macierz_kosztu_dla_rozpatrywanego[iterator-1]
                    
                    if tymczasowe_g < self.graf.macierz_grafu.loc[iterator,'g']:
                        self.graf.macierz_grafu.loc[iterator,'przyszedl_z'] = wierzcholek_najmniejszej_wartosci_z_lista_rozpatrywanych
                        self.graf.macierz_grafu.loc[iterator,'g'] = tymczasowe_g
                        self.graf.macierz_grafu.loc[iterator,'f'] = self.graf.macierz_grafu.loc[iterator,'g'] + self.graf.macierz_grafu.loc[iterator,'h']

                        czy_jest_w_rozpatrywanych = iterator in self.lista_rozpatrywanych
                        
                        if czy_jest_w_rozpatrywanych == False:
                            self.lista_rozpatrywanych.append(iterator)
        
        self.trasa.append("Brak trasy")


    def fsprawdz_ktory_ma_najmniejsza_wartosc(self):

        wierzcholek_o_najmniejszej_wartosci = 0
        najmniejsza_wartosc = float(inf)

        for element in self.lista_rozpatrywanych:

            wartosc_f_elemnetu = self.graf.macierz_grafu.loc[element,'f']

            if wartosc_f_elemnetu < najmniejsza_wartosc:
                najmniejsza_wartosc = wartosc_f_elemnetu
                wierzcholek_o_najmniejszej_wartosci = element

        return(wierzcholek_o_najmniejszej_wartosci)


    def fzrekonstruuj_trase(self,wierzcholek_koncowy):

        wierzcholek_poczatkowy = self.graf.macierz_grafu[self.graf.macierz_grafu['jaki_to_punkt']=='startowy'].index.values[0]

        punkt_do = wierzcholek_koncowy

        self.trasa.append(wierzcholek_koncowy)

        while True:

            punkt_z = punkt_do
            punkt_do = self.graf.macierz_grafu.loc[punkt_z,'przyszedl_z']

            self.trasa.append(int(punkt_do))

            if punkt_do == wierzcholek_poczatkowy:
                self.trasa.reverse()
                break



