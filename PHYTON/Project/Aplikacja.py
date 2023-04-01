from cmath import exp
import tkinter as tk
from tkinter import Image, ttk
from tkinter import filedialog as fd
import SieciNeuronowe
from PIL import ImageTk,Image
from sys import exit
from os import listdir



czcionka = "TkDefaultFont"

#Klasa odpowiedzialna za aplikację okienkową
class GUI:

    #Stworzenie głównego okna aplikacji okienkowej
    def __init__(self):

        self.okno = tk.Tk()
        self.okno.geometry("700x420")
        self.okno.title("Projekt PYTHON, wykonali: Piotr Wyrzyk, Bartłomiej Guś")

        self.main()
        
        self.okno.mainloop()

    #Główna funkcja w programie
    def main(self):
        self.ustawienia_wygladu_poczatkowe()

    #Ustawienie początkowego wyglądu aplikacji, które obejmuje m.in. dodanie labeli oraz buttonów za pomocą których możemy podać lokalizacje zdjęć
    def ustawienia_wygladu_poczatkowe(self):

        self.czy_juz_wczytalem_z_debu = False
        self.czy_juz_wczytalem_z_sosny = False

        # utworzenie ramka
        self.ramka_glowna = tk.Frame(self.okno)
        self.ramka_glowna.pack()

        # utworzenie labelu i trzech pól do wybrania podziału na zbiór uczący, walidujący i testowy

        self.label_poczatkowy = tk.Label(self.ramka_glowna, text = "Program służy do nauki sieci neuronowych", font= (czcionka, 22))
        self.label_poczatkowy.pack()

        self.ramka = tk.Frame(self.ramka_glowna)
        self.ramka.pack()

        self.label_wybierz_gdzie_dab = tk.Label(self.ramka,compound=tk.CENTER , text = "Podaj gdzie znajdują się zdjęcia dębu:", pady=15, font=(czcionka,12))
        self.label_wybierz_gdzie_dab.grid(row = 0, column= 0)
        self.button_wybierz_gdzie_dab = tk.Button(self.ramka, text = "Wybierz dąb", command=self.zapisz_lokalizacje_debu)
        self.button_wybierz_gdzie_dab.grid(row = 0, column = 1)

        self.label_wybierz_gdzie_sosna = tk.Label(self.ramka,compound=tk.CENTER , text = "Podaj gdzie znajdują się zdjęcia sosny:", pady=4, font=(czcionka,12))
        self.label_wybierz_gdzie_sosna.grid(row = 1, column= 0)
        self.button_wybierz_gdzie_sosna = tk.Button(self.ramka, text = "Wybierz sosna", command = self.zapisz_lokalizacje_sosny)
        self.button_wybierz_gdzie_sosna.grid(row = 1, column = 1)

        self.ramka2 = tk.Frame(self.ramka_glowna)
        self.ramka2.pack()

        self.ramka2_podramka = tk.Frame(self.ramka2)
        self.ramka2_podramka.pack()

        self.label_podaj_podzial = tk.Label(self.ramka2_podramka,compound=tk.CENTER , text = "Podaj jaki podział na zbiór uczący, walidujący i testowy w %:", pady=4, font=(czcionka,14))
        self.label_podaj_podzial.pack()

        self.ramka2_podramka2 = tk.Frame(self.ramka2)
        self.ramka2_podramka2.pack()

        self.label_zbior_uczacy = tk.Label(self.ramka2_podramka2, text = "Zbiór uczący:", pady=4, font=(czcionka,8))
        self.label_zbior_uczacy.grid(row = 0, column= 0)
        self.entry_zbior_uczacy = tk.Entry(self.ramka2_podramka2, width = 7,state='disabled')
        self.entry_zbior_uczacy.grid(row = 0, column= 1)

        self.label_zbior_walidujacy = tk.Label(self.ramka2_podramka2, text = "Zbiór walidujący:", pady=4, font=(czcionka,8))
        self.label_zbior_walidujacy.grid(row = 0, column= 2)
        self.entry_zbior_walidujacy = tk.Entry(self.ramka2_podramka2, width= 7,state='disabled')
        self.entry_zbior_walidujacy.grid(row = 0, column= 3)

        self.label_zbior_testowy = tk.Label(self.ramka2_podramka2, text = "Zbiór testowy:", pady=4, font=(czcionka,8))
        self.label_zbior_testowy.grid(row = 0, column= 4)
        self.entry_zbior_testowy = tk.Entry(self.ramka2_podramka2, width = 7,state='disabled')
        self.entry_zbior_testowy.grid(row = 0, column= 5)

        self.button_zatwierdzajacy = tk.Button(self.ramka_glowna, text = "Zatwierdź ustawienia", font = (czcionka,10), command=self.zatwierdz_ustawienia,state='disabled')
        self.button_zatwierdzajacy.pack()

    #Wywoływana przy naciśnięciu przycisku Wybierz dąb za pomocą niego mozemy wskazać lokalizacje zdjęć
    def zapisz_lokalizacje_debu(self):
        self.lokalizacja_debu = fd.askdirectory() # wywołanie okna dialogowego, aby znalezc folder z debami

        if self.czy_juz_wczytalem_z_debu == False:
             self.czy_juz_wczytalem_z_debu = True

        if self.czy_juz_wczytalem_z_sosny == True:
            self.entry_zbior_uczacy.configure(state='normal')
            self.entry_zbior_walidujacy.configure(state='normal')
            self.entry_zbior_testowy.configure(state='normal')
            self.button_zatwierdzajacy.configure(state='normal')
            self.czy_juz_wczytalem_z_debu = False
            self.czy_juz_wczytalem_z_sosny = False


        print(self.lokalizacja_debu)

    #Wywoływana przy naciśnięciu przycisku Wybierz sosna za pomocą niego mozemy wskazać lokalizacje zdjęć
    def zapisz_lokalizacje_sosny(self):

        self.lokalizacja_sosny = fd.askdirectory() # wywołanie okna dialogowego, aby znalezc folder z debami

        if self.czy_juz_wczytalem_z_sosny == False:
            self.czy_juz_wczytalem_z_sosny = True
        
        if self.czy_juz_wczytalem_z_debu == True:
            self.entry_zbior_uczacy.configure(state='normal')
            self.entry_zbior_walidujacy.configure(state='normal')
            self.entry_zbior_testowy.configure(state='normal')
            self.button_zatwierdzajacy.configure(state='normal')
            self.czy_juz_wczytalem_z_debu = False
            self.czy_juz_wczytalem_z_sosny = False

        print(self.lokalizacja_sosny)

    #Wywoływana przy naciśnięciu przycisku Zatwierdź ustawienia za pomocą zapisujemy wartości podziału i przechodzimy do dodawania struktury sieci
    def zatwierdz_ustawienia(self):

        wartosc_entry_zbior_uczacy = self.entry_zbior_uczacy.get()
        wartosc_entry_zbior_walidujacy = self.entry_zbior_walidujacy.get()
        wartosc_entry_zbior_testowy = self.entry_zbior_testowy.get()

        try:
            wartosc_entry_zbior_uczacy = int(wartosc_entry_zbior_uczacy)
            wartosc_entry_zbior_walidujacy = int(wartosc_entry_zbior_walidujacy)
            wartosc_entry_zbior_testowy = int(wartosc_entry_zbior_testowy)

            
            if wartosc_entry_zbior_uczacy + wartosc_entry_zbior_walidujacy + wartosc_entry_zbior_testowy == 100:
            
                self.button_zatwierdzajacy.configure(state = 'disabled')
                self.entry_zbior_uczacy.configure(state = 'disabled')
                self.entry_zbior_walidujacy.configure(state = 'disabled')
                self.entry_zbior_testowy.configure(state = 'disabled')
                self.button_wybierz_gdzie_dab.configure(state = 'disabled')
                self.button_wybierz_gdzie_sosna.configure(state = 'disabled')

                tk.messagebox.showinfo("Poczekaj","Zaczynam wczytywanie. Poczekaj chwilę!")

                self.siec_neuronowa = SieciNeuronowe.SiecNeuronowa(self.lokalizacja_debu,self.lokalizacja_sosny,wartosc_entry_zbior_uczacy,wartosc_entry_zbior_walidujacy,wartosc_entry_zbior_testowy)

                tk.messagebox.showinfo("Skończyłem","Skończyłem wczytywanie")
                self.siec_neuronowa.przygotuj_do_nauki()
                self.tworzenie_struktury()
            else:
                tk.messagebox.showinfo("Błąd", "Suma podziału musi wynosić 100 %")

        except ValueError or TypeError:
            tk.messagebox.showinfo("Błąd", "Podział musi być liczbą")

    #Utworzenie odpowiednich ramek do których następnie będzie dodawana m.in. Listbox w którym będą pokazywane informacji o dodanych strukrutach sieci neuronowej
    def tworzenie_struktury(self):

        self.ramka3 = tk.Frame(self.ramka_glowna)
        self.ramka3.pack()
        self.label_struktura = tk.Label(self.ramka3,compound=tk.CENTER , text = "Dodawanie warstw w sieci:", pady=4, font=(czcionka,14))
        self.label_struktura.pack()
        self.label_warstwa = [] 
        self.dodawanie_kolejnych_warstw()

    #Służy do początkwego zarządzania dodawną strutkurą Conv2D, Pooling, Flatten, Dense
    def dodawanie_kolejnych_warstw(self):

        self.ramka_ud = tk.Frame(self.ramka3)
        self.ramka_ud.pack()

        if self.siec_neuronowa.ile_mam_warstw == 0:

            scrollbar = tk.Scrollbar(self.ramka_ud, orient = tk.VERTICAL)

            self.lista_warstw = tk.Listbox(self.ramka_ud, yscrollcommand=scrollbar,width=100,height=5)

            scrollbar.config(command=self.lista_warstw.yview)
            scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
            self.lista_warstw.pack(side=tk.RIGHT, fill = tk.Y)
            self.lista_warstw.pack(pady=4)


        self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw,"Dodajesz warstwe "+str(self.siec_neuronowa.ile_mam_warstw+1)+".")

        self.ramka3_podramka = tk.Frame(self.ramka3)
        self.ramka3_podramka.pack()

        self.ramka3_podpodramka = tk.Frame(self.ramka3)
        self.ramka3_podpodramka.pack()

        button_conv2d = tk.Button(self.ramka3_podpodramka, text = "Wybieram Conv2d", font = (czcionka,10), command = self.dodaje_warstwe_conv2d)
        button_conv2d.grid(row = 0, column = 0)

        if self.siec_neuronowa.ile_mam_warstw >0:

            button_pooling = tk.Button(self.ramka3_podpodramka, text = "Wybieram Pooling", font = (czcionka,10), command = self.dodaje_warstwe_pooling)
            button_pooling.grid(row = 0, column = 1)

            button_flatten = tk.Button(self.ramka3_podpodramka, text = "Wybieram Flatten", font = (czcionka,10), command = self.dodaje_warstwe_flatten_i_ja_zatwierdzam)
            button_flatten.grid(row = 0, column = 2)

            button_dense = tk.Button(self.ramka3_podpodramka, text = "Wybieram Dense",font = (czcionka,10), command = self.dodaje_warstwe_dense)
            button_dense.grid(row = 0, column = 3)

    #Służy do czyszczenia ramek jak i znajdującej się w niej widgetów
    def wyczysc_ramke(self,jaka_ramka):
        list = jaka_ramka.grid_slaves()
        for l in list:
            l.destroy()

        list = jaka_ramka.pack_slaves()
        for l in list:
            l.destroy()

    #Wyświetla widgety za pomocą, kórych wprowadzamy informacje o parametrach warstwy Conv2D
    def dodaje_warstwe_conv2d(self):

        self.jaka_warstwe_dodaje = "Conv2D"
        self.wyczysc_ramke(self.ramka3_podpodramka)
        self.podramka = tk.Frame(self.ramka3_podramka)
        self.podramka.pack()
        
        label_wybierz_parametry = tk.Label(self.podramka, text = "Podaj paramtery warstwy Conv2d:", font=(czcionka,10))
        label_wybierz_parametry.pack()

        self.podpodramka = tk.Frame(self.podramka)
        self.podpodramka.pack()

        label_podaj_wielkosc = tk.Label(self.podpodramka, text = "Podaj wielkosc:", pady=4, font=(czcionka,8))
        label_podaj_wielkosc.grid(row = 0, column= 0)
        self.entry_podaj_wielkosc = tk.Entry(self.podpodramka, width = 7)
        self.entry_podaj_wielkosc.grid(row = 0, column= 1)

        label_podaj_wielkosc_kernela = tk.Label(self.podpodramka, text = "Podaj wielkość filtru:", pady=4, font=(czcionka,8))
        label_podaj_wielkosc_kernela.grid(row = 0, column= 2)
        self.entry_podaj_wielkosc_kernela = tk.Entry(self.podpodramka, width= 7)
        self.entry_podaj_wielkosc_kernela.grid(row = 0, column= 3)

        label_podaj_funkcje_aktywacji = tk.Label(self.podpodramka, text = "Wybierz funkcje aktywacji:", pady=4, font=(czcionka,8))
        label_podaj_funkcje_aktywacji.grid(row = 0, column= 4)

        n = tk.StringVar()
        self.combobox_podaj_funkcje_aktywacji = ttk.Combobox(self.podpodramka, width = 10, textvariable = n, state='readonly')
        self.combobox_podaj_funkcje_aktywacji['values'] = ('relu','sigmoid','tanh','elu','softmax')
        self.combobox_podaj_funkcje_aktywacji.grid(row = 0, column= 5)

        label_podaj_padding = tk.Label(self.podpodramka, text = "Wybierz typ paddingu:", pady=4, font=(czcionka,8))
        label_podaj_padding.grid(row = 0, column= 6)

        n2 = tk.StringVar()
        self.combobox_podaj_padding = ttk.Combobox(self.podpodramka, width = 10, textvariable = n2, state='readonly')
        self.combobox_podaj_padding['values'] = ('same','valid')
        self.combobox_podaj_padding.grid(row = 0, column= 7)

        self.button_zatwierdzam_kolejna_warstwe = tk.Button(self.podramka, text = "Zatwierdzam kolejna warstwe", font = (czcionka,10), command=self.zatwierdzam_conv2d)
        self.button_zatwierdzam_kolejna_warstwe.pack()

    #Służy do pobrania parametrów z widgetów oraz dodanie kolejnej warstwy Conv2D
    def zatwierdzam_conv2d(self):

        self.parametr1_do_opisu = self.entry_podaj_wielkosc.get() 
        self.parametr2_do_opisu = self.entry_podaj_wielkosc_kernela.get()
        self.paramter3_do_opisu = self.combobox_podaj_funkcje_aktywacji.get()
        self.parametr4_do_opisu = self.combobox_podaj_padding.get()

        self.button_zatwierdzam_kolejna_warstwe.configure(state = 'disabled')
        self.entry_podaj_wielkosc.configure(state = 'disabled')
        self.entry_podaj_wielkosc_kernela.configure(state = 'disabled')
        self.combobox_podaj_funkcje_aktywacji.configure(state = 'disabled')
        self.combobox_podaj_padding.configure(state = 'disabled')

        wartosc_entry_podaj_wielkosc = self.entry_podaj_wielkosc.get()
        wartosc_entry_podaj_wielkosc_kernela = self.entry_podaj_wielkosc_kernela.get()
        wartosc_combobox_podaj_funkcje_aktywacji = self.combobox_podaj_funkcje_aktywacji.get()
        wartosc_combobox_podaj_padding = self.combobox_podaj_padding.get()

        try:
            wartosc_entry_podaj_wielkosc = int(wartosc_entry_podaj_wielkosc)
            wartosc_entry_podaj_wielkosc_kernela = int(wartosc_entry_podaj_wielkosc_kernela)
            odpowiedz = self.siec_neuronowa.dodaje_warstwe_conv2d(wartosc_entry_podaj_wielkosc,wartosc_entry_podaj_wielkosc_kernela,wartosc_combobox_podaj_funkcje_aktywacji,wartosc_combobox_podaj_padding)

            if odpowiedz =="blad":
                raise ValueError
                
            self.wyswietl_strukture_sieci()

        except TypeError:
            tk.messagebox.showinfo("Błąd", "Wielkość jak i wielkość kernela muszą być liczbami!")
            self.button_zatwierdzam_kolejna_warstwe.configure(state = 'normal')
            self.entry_podaj_wielkosc.configure(state = 'normal')
            self.entry_podaj_wielkosc_kernela.configure(state = 'normal')
            self.combobox_podaj_funkcje_aktywacji.configure(state = 'normal')
            self.combobox_podaj_padding.configure(state = 'normal')
        except ValueError:
            tk.messagebox.showinfo("Błąd", "Takiego połączenia nie może być!")
            self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw)
            self.ramka3_podpodramka.destroy()
            self.wyczysc_ramke(self.podpodramka)
            self.podpodramka.destroy()
            self.wyczysc_ramke(self.podramka)
            self.podramka.destroy()
            self.ramka3_podramka.destroy()
            self.dodawanie_kolejnych_warstw()

    #Wyświetla widgety za pomocą, kórych wprowadzamy informacje o parametrach warstwy Pooling
    def dodaje_warstwe_pooling(self):

        self.jaka_warstwe_dodaje = "Pooling"
        self.wyczysc_ramke(self.ramka3_podpodramka)
        self.podramka = tk.Frame(self.ramka3_podramka)
        self.podramka.pack()
        
        label_wybierz_parametry = tk.Label(self.podramka, text = "Podaj paramtery warstwy Pooling:", font=(czcionka,10))
        label_wybierz_parametry.pack()

        self.podpodramka = tk.Frame(self.podramka)
        self.podpodramka.pack()

        label_podaj_jaki_typ_poolingu = tk.Label(self.podpodramka, text = "Wybierz typ pooling'u:", pady=4, font=(czcionka,8))
        label_podaj_jaki_typ_poolingu.grid(row = 0, column= 0)

        n3 = tk.StringVar()
        self.combobox_podaj_typ_poolingu = ttk.Combobox(self.podpodramka, width = 10, textvariable = n3, state='readonly')
        self.combobox_podaj_typ_poolingu['values'] = ('MAX','AVG')
        self.combobox_podaj_typ_poolingu.grid(row = 0, column= 1)

        label_podaj_wielkosc_poolingu = tk.Label(self.podpodramka, text = "Podaj wielkosc:", pady=4, font=(czcionka,8))
        label_podaj_wielkosc_poolingu.grid(row = 0, column= 2)
        self.entry_podaj_wielkosc_poolingu = tk.Entry(self.podpodramka, width = 7)
        self.entry_podaj_wielkosc_poolingu.grid(row = 0, column= 3)

        label_podaj_wielkosc_kroku = tk.Label(self.podpodramka, text = "Podaj wielkość kroku:", pady=4, font=(czcionka,8))
        label_podaj_wielkosc_kroku.grid(row = 0, column= 4)
        self.entry_podaj_wielkosc_kroku = tk.Entry(self.podpodramka, width= 7)
        self.entry_podaj_wielkosc_kroku.grid(row = 0, column= 5)

        self.button_zatwierdzam_kolejna_warstwe_poolingu = tk.Button(self.podramka, text = "Zatwierdzam kolejna warstwe", font = (czcionka,10), command=self.zatwierdzam_pooling)
        self.button_zatwierdzam_kolejna_warstwe_poolingu.pack()

    #Służy do pobrania parametrów z widgetów oraz dodanie kolejnej warstwy Pooling
    def zatwierdzam_pooling(self):

        self.parametr1_do_opisu = self.combobox_podaj_typ_poolingu.get() 
        self.parametr2_do_opisu = self.entry_podaj_wielkosc_poolingu.get()
        self.paramter3_do_opisu = self.entry_podaj_wielkosc_kroku.get()

        self.button_zatwierdzam_kolejna_warstwe_poolingu.configure(state= 'disabled')
        self.combobox_podaj_typ_poolingu.configure(state = 'disabled')
        self.entry_podaj_wielkosc_poolingu.configure(state = 'disabled')
        self.entry_podaj_wielkosc_kroku.configure(state = 'disabled')

        wartosc_combobox_podaj_typ_poolingu = self.combobox_podaj_typ_poolingu.get()
        wartosc_entry_podaj_wielkosc_poolingu = self.entry_podaj_wielkosc_poolingu.get()
        wartosc_entry_podaj_wielkosc_kroku = self.entry_podaj_wielkosc_kroku.get()

        print(wartosc_entry_podaj_wielkosc_poolingu, wartosc_entry_podaj_wielkosc_kroku)

        try:
            wartosc_entry_podaj_wielkosc_poolingu = int(wartosc_entry_podaj_wielkosc_poolingu)
            wartosc_entry_podaj_wielkosc_kroku = int(wartosc_entry_podaj_wielkosc_kroku)
            odpowiedz = self.siec_neuronowa.dodaje_warstwe_poolingu(wartosc_combobox_podaj_typ_poolingu,wartosc_entry_podaj_wielkosc_poolingu,wartosc_entry_podaj_wielkosc_kroku)

            if odpowiedz == "blad":
                raise ValueError
            
            self.wyswietl_strukture_sieci()

        except TypeError:
            tk.messagebox.showinfo("Błąd", "Wielkość jak i wielkość krok muszą być liczbami!")
            self.button_zatwierdzam_kolejna_warstwe_poolingu.configure(state= 'normal')
            self.combobox_podaj_typ_poolingu.configure(state = 'normal')
            self.entry_podaj_wielkosc_poolingu.configure(state = 'normal')
            self.entry_podaj_wielkosc_kroku.configure(state = 'normal')
        except ValueError:
            tk.messagebox.showinfo("Błąd", "Takiego połączenia nie może być!")
            self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw)
            self.ramka3_podpodramka.destroy()
            self.wyczysc_ramke(self.podpodramka)
            self.podpodramka.destroy()
            self.wyczysc_ramke(self.podramka)
            self.podramka.destroy()
            self.ramka3_podramka.destroy()
            self.dodawanie_kolejnych_warstw()

    #Wyświetla widgety za pomocą, kórych wprowadzamy informacje o parametrach warstwy Flatten jak i juz ja zatwierdzam
    def dodaje_warstwe_flatten_i_ja_zatwierdzam(self):

        self.jaka_warstwe_dodaje = "Flatten"
        self.wyczysc_ramke(self.ramka3_podpodramka)

        try:
            self.siec_neuronowa.dodaje_warstwe_flatten()
            self.wyswietl_strukture_sieci()
        except:
            tk.messagebox.showinfo("Błąd", "Błąd przy tworzeniu Flatten!")

    #Wyświetla widgety za pomocą, kórych wprowadzamy informacje o parametrach warstwy Dense
    def dodaje_warstwe_dense(self):

        self.jaka_warstwe_dodaje = "Dense"
        self.wyczysc_ramke(self.ramka3_podpodramka)
        self.podramka = tk.Frame(self.ramka3_podramka)
        self.podramka.pack()
        
        label_wybierz_parametry = tk.Label(self.podramka, text = "Podaj paramtery warstwy Dense:", font=(czcionka,10))
        label_wybierz_parametry.pack()

        self.podpodramka = tk.Frame(self.podramka)
        self.podpodramka.pack()

        label_podaj_liczbe_neuronow = tk.Label(self.podpodramka, text = "Podaj liczbę neuronów:", pady=4, font=(czcionka,8))
        label_podaj_liczbe_neuronow.grid(row = 0, column= 0)
        self.entry_podaj_liczbe_neuronow = tk.Entry(self.podpodramka, width = 7)
        self.entry_podaj_liczbe_neuronow.grid(row = 0, column= 1)

        label_podaj_funkcje_aktywacji_dense = tk.Label(self.podpodramka, text = "Wybierz funkcję aktywacji:", pady=4, font=(czcionka,8))
        label_podaj_funkcje_aktywacji_dense.grid(row = 0, column= 2)

        n = tk.StringVar()
        self.combobox_podaj_funkcje_aktywacji_dense = ttk.Combobox(self.podpodramka, width = 10, textvariable = n, state='readonly')
        self.combobox_podaj_funkcje_aktywacji_dense['values'] = ('relu','sigmoid','tanh','elu','softmax')
        self.combobox_podaj_funkcje_aktywacji_dense.grid(row = 0, column= 5)

        self.button_zatwierdzam_kolejna_warstwe_dense = tk.Button(self.podramka, text = "Zatwierdzam kolejna warstwe", font = (czcionka,10), command=self.zatwierdzam_dense)
        self.button_zatwierdzam_kolejna_warstwe_dense.pack()

    #Służy do pobrania parametrów z widgetów oraz dodanie kolejnej warstwy Dense
    def zatwierdzam_dense(self):

        self.parametr1_do_opisu = self.entry_podaj_liczbe_neuronow.get() 
        self.parametr2_do_opisu = self.combobox_podaj_funkcje_aktywacji_dense.get()

        self.entry_podaj_liczbe_neuronow.configure(state = 'disabled')
        self.combobox_podaj_funkcje_aktywacji_dense.configure(state = 'disabled')
        self.button_zatwierdzam_kolejna_warstwe_dense.config(state='disabled')

        wartosc_entry_podaj_liczbe_neuronow = self.entry_podaj_liczbe_neuronow.get()
        wartosc_combobox_podaj_funkcje_aktywcji_dense = self.combobox_podaj_funkcje_aktywacji_dense.get()

        try:
            wartosc_entry_podaj_liczbe_neuronow = int(wartosc_entry_podaj_liczbe_neuronow)
            self.siec_neuronowa.dodaje_warstwe_dense(wartosc_entry_podaj_liczbe_neuronow,wartosc_combobox_podaj_funkcje_aktywcji_dense)

            self.wyswietl_strukture_sieci()

        except TypeError:
            tk.messagebox.showinfo("Błąd", "Wielkość jak i wielkość krok muszą być liczbami!")
            self.entry_podaj_liczbe_neuronow.configure(state = 'normal')
            self.combobox_podaj_funkcje_aktywacji_dense.configure(state = 'normal')
            self.button_zatwierdzam_kolejna_warstwe_dense.config(state='normal')

    #Służy do wyświetlenia aktualnej struktury sieci po dodaniu koljnej warstwy 
    def wyswietl_strukture_sieci(self):

        self.okno_z_rysunkiem_sieci = tk.Toplevel(self.okno)
        self.okno_z_rysunkiem_sieci.geometry("700x800")
        self.okno_z_rysunkiem_sieci.title("Struktura sieci")

        self.button_ok = tk.Button(self.okno_z_rysunkiem_sieci, text = "OK", command = self.usuniecie_okna_z_struktura)
        self.button_ok.pack()

        ramka = tk.Frame(self.okno_z_rysunkiem_sieci)
        ramka.pack()

        canvas = tk.Canvas(ramka,width = 600, height = 1500)

        scrollbar = tk.Scrollbar(ramka, orient = tk.HORIZONTAL,command=canvas.xview)
        scrollbar.pack(side=tk.BOTTOM, fill = tk.X)
        canvas.config(xscrollcommand=scrollbar.set)

        obraz = SieciNeuronowe.visualkeras.layered_view(self.siec_neuronowa.model, legend=True)

        img = ImageTk.PhotoImage(obraz)

        canvas.create_image(300,750,image = img,anchor=tk.S)
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.pack()

        self.okno_z_rysunkiem_sieci.wait_window(self.okno_z_rysunkiem_sieci)

    #Służy do usunięcia okna z strukturą po naciśnięciu OK oraz wyboru czy dalej chcemy konytnuować dodawnie warstw cz też przejść już do nauki
    def usuniecie_okna_z_struktura(self):
        self.okno_z_rysunkiem_sieci.destroy()

        odpowiedz_z_messagebox = tk.messagebox.askquestion("Czy kontynujemy ?", "Jeżeli chcesz kontynuować dodawanie warstw naciśnij - Tak, jeśli chcesz zakończyć dodawanie i przejść do parametrów nauki naciśnij - Nie")

        if odpowiedz_z_messagebox == "yes":
            self.ramka3_podpodramka.destroy()

            if self.jaka_warstwe_dodaje == "Conv2D":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodałes już warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                + self.jaka_warstwe_dodaje + " , wielkość: " + self.parametr1_do_opisu +" , wielkość filtru: " + self.parametr2_do_opisu 
                + "x" + self.parametr2_do_opisu + " , fun. akty.: " + self.paramter3_do_opisu + " , padding: "+self.parametr4_do_opisu)

                self.wyczysc_ramke(self.podpodramka)
                self.podpodramka.destroy()
                self.wyczysc_ramke(self.podramka)
                self.podramka.destroy()
                self.ramka3_podramka.destroy()

            elif self.jaka_warstwe_dodaje == "Pooling":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                +" "+self.jaka_warstwe_dodaje + " , typ: " + self.parametr1_do_opisu + " , wielkość: " + self.parametr2_do_opisu 
                + "x" + self.parametr2_do_opisu + " , wielkość filtru: " + self.paramter3_do_opisu + " x "+self.paramter3_do_opisu)

                self.wyczysc_ramke(self.podpodramka)
                self.podpodramka.destroy()
                self.wyczysc_ramke(self.podramka)
                self.podramka.destroy()
                self.ramka3_podramka.destroy()

            elif self.jaka_warstwe_dodaje == "Flatten":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw)
                +" "+ self.jaka_warstwe_dodaje)

                self.ramka3_podramka.destroy()

            elif self.jaka_warstwe_dodaje == "Dense":

                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                +" "+self.jaka_warstwe_dodaje + " , liczba neuronów: " + self.parametr1_do_opisu + " , fun. akty.: " + self.parametr2_do_opisu)

                self.wyczysc_ramke(self.podpodramka)
                self.podpodramka.destroy()
                self.wyczysc_ramke(self.podramka)
                self.podramka.destroy()
                self.ramka3_podramka.destroy()

            self.dodawanie_kolejnych_warstw()

        else: 
            self.lokalizacja_modelu = ""

            if self.jaka_warstwe_dodaje == "Conv2D":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodałes już warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                + self.jaka_warstwe_dodaje + " , wielkość: " + self.parametr1_do_opisu +" , wielkość filtru: " + self.parametr2_do_opisu 
                + "x" + self.parametr2_do_opisu + " , fun. akty.: " + self.paramter3_do_opisu + " , padding: "+self.parametr4_do_opisu)

            elif self.jaka_warstwe_dodaje == "Pooling":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                +" "+self.jaka_warstwe_dodaje + " , typ: " + self.parametr1_do_opisu + " , wielkość: " + self.parametr2_do_opisu 
                + "x" + self.parametr2_do_opisu + " , wielkość filtru: " + self.paramter3_do_opisu + " x "+self.paramter3_do_opisu)

            elif self.jaka_warstwe_dodaje == "Flatten":
                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw)
                +" "+ self.jaka_warstwe_dodaje)

            elif self.jaka_warstwe_dodaje == "Dense":

                self.lista_warstw.delete(self.siec_neuronowa.ile_mam_warstw-1)

                self.lista_warstw.insert(self.siec_neuronowa.ile_mam_warstw-1,"Dodaleś juz warstwę - " + str(self.siec_neuronowa.ile_mam_warstw) 
                +" "+self.jaka_warstwe_dodaje + " , liczba neuronów: " + self.parametr1_do_opisu + " , fun. akty.: " + self.parametr2_do_opisu)

            self.tworzenie_okna_do_nauki()

    #Służy do stworzenia okna do nauki za pomocą, którego możemy okrelić parametry nauki sieci
    def tworzenie_okna_do_nauki(self):
        self.okno_do_nauki = tk.Toplevel(self.okno)
        self.okno_do_nauki.geometry("500x200")
        self.okno_do_nauki.title("Wybór parametrów do nauki sieci")

        label_informujacy = tk.Label(self.okno_do_nauki, text = "Proszę o podanie kilku parametrów związanych z nauką", font=(czcionka,12))
        label_informujacy.pack()

        ramka_do_wartosci = tk.Frame(self.okno_do_nauki)
        ramka_do_wartosci.pack()

        label_podaj_jaki_optimaizer = tk.Label(ramka_do_wartosci, text = "Wybierz optimizer:",font=(czcionka,8))
        label_podaj_jaki_optimaizer.grid(row=0,column=0)

        n3 = tk.StringVar()
        self.combobox_podaj_jaki_optimizer = ttk.Combobox(ramka_do_wartosci, width = 10, textvariable = n3, state='readonly')
        self.combobox_podaj_jaki_optimizer['values'] = ('Adam','Adamax','Nadam','RMSprop','SGD')
        self.combobox_podaj_jaki_optimizer.grid(row = 0, column= 1)

        label_podaj_jaka_liczba_epok = tk.Label(ramka_do_wartosci, text = "Podaj liczbę epok:",font=(czcionka,8))
        label_podaj_jaka_liczba_epok.grid(row=1,column=0)

        self.entry_podaj_jaka_liczba_epok = tk.Entry(ramka_do_wartosci)
        self.entry_podaj_jaka_liczba_epok.grid(row=1,column=1)

        label_podaj_jaki_batch = tk.Label(ramka_do_wartosci, text = "Podaj wielkość batch:",font=(czcionka,8))
        label_podaj_jaki_batch.grid(row=2,column=0)

        self.entry_podaj_jaki_batch = tk.Entry(ramka_do_wartosci)
        self.entry_podaj_jaki_batch.grid(row=2,column=1)

        label_podaj_co_ile_ma_sie_odswiezac = tk.Label(ramka_do_wartosci, text = "Podaj co ile epok ma się odświeżać wykres dokładności:",font=(czcionka,8))
        label_podaj_co_ile_ma_sie_odswiezac.grid(row=3,column=0)

        self.entry_podaj_co_ile_ma_sie_odswiezac = tk.Entry(ramka_do_wartosci)
        self.entry_podaj_co_ile_ma_sie_odswiezac.grid(row=3,column=1)

        label_podaj_nazwe_modelu = tk.Label(ramka_do_wartosci, text = "Podaj nazwe modelu:",font=(czcionka,8))
        label_podaj_nazwe_modelu.grid(row=4,column=0)

        self.entry_podaj_nazwe_modelu = tk.Entry(ramka_do_wartosci)
        self.entry_podaj_nazwe_modelu.grid(row=4,column=1)

        label_lokalizacje_gdzie_zapisac = tk.Label(ramka_do_wartosci, text = "Podaj gdzie zapisać model:",font=(czcionka,8))
        label_lokalizacje_gdzie_zapisac.grid(row=5,column=0)

        self.button_podaj_gdzie_zapisac_model = tk.Button(ramka_do_wartosci, text = "Wybierz lokalizacje",command=self.zapisz_lokalizacje_modelu)
        self.button_podaj_gdzie_zapisac_model.grid(row = 5, column = 1)

        self.button_zatwierdzajcy_parametry_nauki = tk.Button(self.okno_do_nauki, text = "Rozpocznij naukę",command=self.zatwierdzam_paramtery_nauki)
        self.button_zatwierdzajcy_parametry_nauki.pack()

        self.okno_do_nauki.wait_window(self.okno_do_nauki)

    #Wykorzystywana do zapisu pliku jak i sprawdzenia czy taki plik juz nie istnieje w tym przypadku trzeba jeszcze raz wpisać nazwę albo wybrać inną lokalizację
    def zapisz_lokalizacje_modelu(self):

        self.lokalizacja_modelu = fd.askdirectory()
        try:
            lista_plikow = listdir(self.lokalizacja_modelu)
        except FileNotFoundError:
            pass

        czy_byl_taki = False

        for a in lista_plikow:

            if a == self.entry_podaj_nazwe_modelu.get()+".h5":
                czy_byl_taki = True
                self.button_zatwierdzajcy_parametry_nauki.configure(state="disabled")

        if czy_byl_taki == True:
            tk.messagebox.showinfo("Błąd", "Już istnieje taki plik.")
            self.button_zatwierdzajcy_parametry_nauki.configure(state="disabled")
        else:
            self.button_zatwierdzajcy_parametry_nauki.configure(state="normal")
            
     #Służy do pobrania parametrów nauki jak i rozpoczęcia procesu   
    def zatwierdzam_paramtery_nauki(self):

        wartosc_combobox_podaj_jaki_optimizer = self.combobox_podaj_jaki_optimizer.get()
        wartosc_entry_podaj_jaka_liczba_epok = self.entry_podaj_jaka_liczba_epok.get()
        wartosc_entry_podaj_jaki_batch = self.entry_podaj_jaki_batch.get()
        wartosc_entry_podaj_co_ile_ma_sie_odswiezac = self.entry_podaj_co_ile_ma_sie_odswiezac.get()
        wartosc_entry_podaj_nazwe_modelu = self.entry_podaj_nazwe_modelu.get()

        try:
            wartosc_entry_podaj_jaka_liczba_epok = int(wartosc_entry_podaj_jaka_liczba_epok)
            wartosc_entry_podaj_jaki_batch = int(wartosc_entry_podaj_jaki_batch)
            wartosc_entry_podaj_co_ile_ma_sie_odswiezac = int(wartosc_entry_podaj_co_ile_ma_sie_odswiezac)

            self.combobox_podaj_jaki_optimizer.configure(state = 'disabled')
            self.entry_podaj_jaka_liczba_epok.configure(state = 'disabled')
            self.entry_podaj_jaki_batch.configure(state = 'disabled')
            self.entry_podaj_co_ile_ma_sie_odswiezac.configure(state = 'disabled')
            self.button_podaj_gdzie_zapisac_model.configure(state = 'disabled')
            self.entry_podaj_nazwe_modelu.configure(state = 'disabled')

            return_z_modelu = self.siec_neuronowa.rozpoczecie_nauki(wartosc_combobox_podaj_jaki_optimizer,wartosc_entry_podaj_jaka_liczba_epok,wartosc_entry_podaj_jaki_batch,
            wartosc_entry_podaj_co_ile_ma_sie_odswiezac,self.lokalizacja_modelu,wartosc_entry_podaj_nazwe_modelu)

        except TypeError:
            tk.messagebox.showinfo("Błąd", "Sprawdź powyższe wartości")
            self.combobox_podaj_jaki_optimizer.configure(state = 'normal')
            self.entry_podaj_jaka_liczba_epok.configure(state = 'normal')
            self.entry_podaj_jaki_batch.configure(state = 'normal')
            self.entry_podaj_co_ile_ma_sie_odswiezac.configure(state = 'normal')
            self.button_podaj_gdzie_zapisac_model.configure(state = 'normal')
            self.entry_podaj_nazwe_modelu.configure(state = 'normal')

        if return_z_modelu[0] == "niewlasciwy model":
            tk.messagebox.showinfo("Błąd", "Stworzyłeś niewłaściwy model wykonaj go jeszcze raz. Pamiętaj ostatnia warstwa powinna być Dense - softmax!")

            self.siec_neuronowa.ile_mam_warstw = 0

            self.ramka3.destroy()
            self.okno_do_nauki.destroy()
            self.lokalizacja_modelu = ""
            self.siec_neuronowa.model = SieciNeuronowe.tf.keras.models.Sequential()
            self.lista_warstw = []
            self.tworzenie_struktury()
        elif return_z_modelu[0] == "udalo sie stworzyc":

            wyniki_dla_zbior_testowego = self.siec_neuronowa.wyniki_dla_zbioru_testowego()

            text = "Udało Ci się uzyskać następujące wyniki: \ndla zbioru uczącego: loss - " + str(round(return_z_modelu[1].history['loss'][-1],3)) + " accuracy - " +str(round(return_z_modelu[1].history['accuracy'][-1],3))+"\n"+"dla zbioru walidującego: loss - " + str(round(return_z_modelu[1].history['val_loss'][-1],3)) + " accuracy - " +str(round(return_z_modelu[1].history['val_accuracy'][-1],3))+"\n" +"dla zbioru testowego: loss - "+str(round(wyniki_dla_zbior_testowego[0],3))+" accuracy - "+str(round(wyniki_dla_zbior_testowego[1],3))

            tk.messagebox.showinfo("Wyniki", text)

            odpowiedz = tk.messagebox.askquestion("Czy chcesz kontynuować ?", "Jeżeli chcesz przeprowadzić proces od początku naciśnij naciśnij TAK, jeżli chcesz zamknąć program NIE.")

            if odpowiedz == "no":
                self.okno_do_nauki.destroy()
                self.okno.destroy()
                exit()
            elif odpowiedz == "yes":
                self.okno_do_nauki.destroy()
                self.ramka_glowna.destroy()
                self.lokalizacja_modelu = ""
                self.siec_neuronowa.model = SieciNeuronowe.tf.keras.models.Sequential()
                self.lista_warstw = []
                self.main()

if __name__ == "__main__":
    aplikacja = GUI()

