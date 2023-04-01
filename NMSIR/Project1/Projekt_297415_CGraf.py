import pandas as pd
import math 
import numpy as np

# Zawarty w niej jest graf na podstawie, ktorego klasa A* bedzie szukac najkrotszej trasy
class CGraf:
    sciezka_do_pliku = ""
    plik = ""
    linijki_z_pliku = ""
    liczba_wierzcholkow = 0

    data = {'wierzcholek':[],
    'wspolrzedna_X':[],
    'wspolrzedna_Y':[],
    'jaki_to_punkt':[],
    'przyszedl_z':[],
    'g':[],
    'h':[],
    'f':[]
    }

    #Macierz grafu posiada pola data, ktora sa jego wierzcholkami
    macierz_grafu = pd.DataFrame(data)

    def __init__(self,sciezka):

        #Wprowadzenie sciezki do pola sciezka_do_pliku
        self.fwprowadz_sciezke_do_pliku(sciezka)

        #Otwarcie pliku z sciezka i przczytanie kolejnych linijek
        self.fotworz_plik()

        #Zamkniecie pliku
        self.fzamknij_plik()

        #Obliczenie liczby wierzcholkow
        self.liczba_wierzcholkow = len(self.linijki_z_pliku) - 2

        #Uzupelnieni macierzy grafu
        self.fprzygotuj_do_A_star()

    def fwprowadz_sciezke_do_pliku(self,sciezka):
        self.sciezka_do_pliku = sciezka


    def fotworz_plik(self):
        self.plik = open(self.sciezka_do_pliku,"r")
        self.linijki_z_pliku=self.plik.readlines()


    def fzamknij_plik(self):
        self.plik.close()


    def fprzygotuj_do_A_star(self):
    
        iterator = 0
        uproszczona_linia = ""

        #Wczytuje kolejne linie z pliku i usuwa znaki ENTER
        for linijka in self.linijki_z_pliku:
            uproszczona_linia = linijka.replace('\n',"")
            self.linijki_z_pliku[iterator] = uproszczona_linia
            iterator = iterator + 1
        
        self.fuzupelnij_macierz_grafu()

    def fuzupelnij_macierz_grafu(self):

        #Dodanie pustych wartości jak i numerów wierzchołków
        for iterator in range(0,self.liczba_wierzcholkow):
            self.macierz_grafu.loc[self.macierz_grafu.shape[0]] = [iterator+1,None,None,None,None,None,None,None]

        self.macierz_grafu = self.macierz_grafu.astype({'wierzcholek':'int'})

        #Uzupełnia wspolrzedne punktow w macierzy grafu
        self.fuzupelnij_wspolrzedne_punktow()

        #Ustawia indexy DataFrame na kolumne wierzcholek, czyli kolumne unikalna
        self.macierz_grafu.set_index('wierzcholek',inplace=True)

        #Uzupelnia jaki to punkt czy to startowy, czy to koncowy w macierzy grafu
        self.fuzupelnij_jaki_to_punkt()

        #Uzupelnia kolumne v wartosciami inf i przypisuje punktowi startowemu wartosc 0
        self.fuzupelnij_v()

        #Uzupelnienie kolmuny h
        self.fuzupelnij_h()

        #Uzupelnienie kolumny f
        self.fuzupelnij_f()

        #Wpisz koszty polaczenia danego wierzcholkami z innymi
        self.fuzupelnij_macierz_kosztu()


    def fuzupelnij_wspolrzedne_punktow(self):

        #Oczyszczenie 1 - linijki wartosci czyli zawierajacej wspolrzedne aby wpisac do ogolnej macierzy
        linia_z_wartosciami_wspolrzednych = self.linijki_z_pliku[0]
        linia_z_wartosciami_wspolrzednych = linia_z_wartosciami_wspolrzednych.replace("(","")
        linia_z_wartosciami_wspolrzednych = linia_z_wartosciami_wspolrzednych.replace(")","")
        linia_z_wartosciami_wspolrzednych = linia_z_wartosciami_wspolrzednych.replace(",","")
        lista_z_wspolrzednymi = linia_z_wartosciami_wspolrzednych.split(" ")

        #Wpisywanie wspolrzednych do ogolnej macierzy
        iterator_do_listy = 0

        for iterator_wierszy in range(0,self.liczba_wierzcholkow):
            for iterator_XY in range(0,2):

                if iterator_XY == 0:
                    self.macierz_grafu.at[iterator_wierszy,'wspolrzedna_X'] = lista_z_wspolrzednymi[iterator_do_listy]

                if iterator_XY == 1:
                    self.macierz_grafu.at[iterator_wierszy,'wspolrzedna_Y'] = lista_z_wspolrzednymi[iterator_do_listy]

                iterator_do_listy = iterator_do_listy + 1
            
            iterator_wierszy = iterator_wierszy + 1

        self.macierz_grafu = self.macierz_grafu.astype({'wspolrzedna_X':'int'})
        self.macierz_grafu = self.macierz_grafu.astype({'wspolrzedna_Y':'int'})


    def fuzupelnij_jaki_to_punkt(self):

        #Pobiera linie z wartosciami jaki to punkt
        linia_z_wartosciami_jaki_to_punkty = self.linijki_z_pliku[1]
        lista_z_jakimi_punktami = linia_z_wartosciami_jaki_to_punkty.split(" ")

        self.macierz_grafu = self.macierz_grafu.astype({'jaki_to_punkt':'string'})

        #Dodanie punktow 'startowy' i 'koncowy' do w kolumnie 'jaki_to_punkt'
        self.macierz_grafu.loc[int(lista_z_jakimi_punktami[0]) ,'jaki_to_punkt'] = 'startowy'
        self.macierz_grafu.loc[int(lista_z_jakimi_punktami[1]) ,'jaki_to_punkt'] = 'koncowy'


    def fuzupelnij_v(self):

        #Dodanie wszystkim wartosciom inf
        self.macierz_grafu['g'] = float('inf')

        #Wyszukuje punkt startowy
        wierzcholek_startowy = self.macierz_grafu[self.macierz_grafu['jaki_to_punkt']=='startowy'].index.values

        #Wpisanie wartosci dla punktu startowego
        self.macierz_grafu.loc[wierzcholek_startowy,'g'] = 0
    

    def fuzupelnij_h(self):

        #Wyszukanie punktu startowego - jego wiersza
        wiersz_punktu_startowego = self.macierz_grafu[self.macierz_grafu['jaki_to_punkt']=='koncowy'].index.values

        #Pobranie koordynatów punktu startowego, ktore zostana wykorzystane do obliczania heurestyki
        wspolrzedna_X_punktu_startowego = self.macierz_grafu.loc[wiersz_punktu_startowego[0],'wspolrzedna_X']
        wspolrzedna_Y_punktu_startowego = self.macierz_grafu.loc[wiersz_punktu_startowego[0],'wspolrzedna_Y']

        #Wpisanie wartosci heurestyki do grafu
        for iterator in range(1,self.liczba_wierzcholkow+1):

            wspolrzedna_X_punktu_analizowanego = self.macierz_grafu.loc[iterator,'wspolrzedna_X']
            wspolrzedna_Y_punktu_analizowanego = self.macierz_grafu.loc[iterator,'wspolrzedna_Y']

            odleglosc_eukledisowa = math.sqrt((wspolrzedna_X_punktu_analizowanego - wspolrzedna_X_punktu_startowego)**2 + (wspolrzedna_Y_punktu_analizowanego - wspolrzedna_Y_punktu_startowego)**2)

            self.macierz_grafu.loc[iterator,'h'] = odleglosc_eukledisowa
            # self.macierz_grafu.loc[iterator, 'h'] = 0

    def fuzupelnij_f(self):

        #Dodanie wszystkim wartosciom inf
        self.macierz_grafu['f'] = float('inf')

        #Wyszukuje punkt startowy
        wierzcholek_startowy = self.macierz_grafu[self.macierz_grafu['jaki_to_punkt']=='startowy'].index.values

        #Wpisanie wartosci dla punktu startowego
        self.macierz_grafu.loc[wierzcholek_startowy,'f'] = self.macierz_grafu.loc[wierzcholek_startowy,'h']


    def fuzupelnij_macierz_kosztu(self):

        cala_linia = []

        #Wpisanie do kazdego wierzcholka jego macierzy polaczen
        for iterator in range(1,self.liczba_wierzcholkow+1):

            lista_wartosci = self.linijki_z_pliku[iterator+1].split(" ")
            
            #Usuwam puste elementy listy_wartosci jesli takowe istnieja
            czy_jest_w_rozpatrywanych = '' in lista_wartosci
            if czy_jest_w_rozpatrywanych == True:
                lista_wartosci.remove('')

            linijka_z_floatami = np.asarray([float(e) for e in lista_wartosci],dtype = object)

            cala_linia.append(linijka_z_floatami)

        self.macierz_grafu['macierz_kosztu'] = cala_linia

