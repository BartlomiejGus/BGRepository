import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import visualkeras
from IPython.display import clear_output

#Klasa odpowiedzialna za opracje na sieci neruonowej   
class SiecNeuronowa:

    #Służy do wprowadzenia danych uczących 
    def __init__(self,path_dab,path_sosna,ilosc_zbior_uczacy, ilosc_zbior_walidujacy,ilosc_zbior_testowy):
        
        self.ile_mam_warstw = 0

        ilosc_zbior_uczacy = ilosc_zbior_uczacy/100
        ilosc_zbior_walidujacy = ilosc_zbior_walidujacy/100
        ilosc_zbior_testowy = ilosc_zbior_testowy/100

        path_dab = path_dab + "/"
        path_sosna = path_sosna + "/"

        [self.liczba_zdjec_debu,lista_folderow_debu] = self.zliczanie_zdjec(path_dab)
        [self.liczba_zdjec_sosny,lista_folderow_sosna] = self.zliczanie_zdjec(path_sosna)

        [self.dab_zbior_uczacy,aktualny_folder_debu] = self.dodawanie_do_zbioru(path_dab,lista_folderow_debu,ilosc_zbior_uczacy,self.liczba_zdjec_debu,0,0)
        [self.dab_zbior_walidujacy,aktualny_folder_debu] = self.dodawanie_do_zbioru(path_dab,lista_folderow_debu,ilosc_zbior_walidujacy,self.liczba_zdjec_debu,aktualny_folder_debu,1)
        [self.dab_zbior_testowy,aktualny_folder_debu] = self.dodawanie_do_zbioru(path_dab,lista_folderow_debu,ilosc_zbior_testowy,self.liczba_zdjec_debu,aktualny_folder_debu,2)

        [self.sosna_zbior_uczacy, aktualny_folder_sosny] = self.dodawanie_do_zbioru(path_sosna,lista_folderow_sosna,ilosc_zbior_uczacy,self.liczba_zdjec_sosny,0,0)
        [self.sosna_zbior_walidujacy, aktualny_folder_sosny] = self.dodawanie_do_zbioru(path_sosna,lista_folderow_sosna,ilosc_zbior_walidujacy,self.liczba_zdjec_sosny,aktualny_folder_sosny,1)
        [self.sosna_zbior_testowy, aktualny_folder_sosny] = self.dodawanie_do_zbioru(path_sosna,lista_folderow_sosna,ilosc_zbior_walidujacy,self.liczba_zdjec_sosny,aktualny_folder_sosny,2)

    #Służy do zliczenia zdjęć w danym folderze
    def zliczanie_zdjec(self,path):

        lista_folderow = os.listdir(path)
        print("Liczba folderow zdjec debu:", len(lista_folderow))
        liczba_zdjec = 0

        for a in lista_folderow:

            path_aktualnie_sprawdzany = path + a
            lista_plikow = os.listdir(path_aktualnie_sprawdzany)
            liczba_zdjec = liczba_zdjec + len(lista_plikow)

        return [liczba_zdjec,lista_folderow]

    #Wykorzytywana do dodawania danych do odpowiednich zbiorów, jeśli uczacy to 0, jesli walidujacy to 1, jesli testowy to 2
    def dodawanie_do_zbioru(self,path,lista_folderow, ilosc_zbioru, liczba_zdjec,aktualny_folder,czy_uczacy_czy_walidujacy_czy_testowy):

        zbior = []
        liczba_zdjec_w_zbiorze = 0
        przestan_dodawac = False

        if czy_uczacy_czy_walidujacy_czy_testowy == 0:
            index = 0
        else:
            index = lista_folderow.index(aktualny_folder)

        for aktualny_folder_uczacy in lista_folderow[index:len(lista_folderow)]:

            path_aktualnie_dodawany_folder = path + aktualny_folder_uczacy
            lista_plikow = os.listdir(path_aktualnie_dodawany_folder)
            print(path_aktualnie_dodawany_folder)
        
            for aktualny_plik_uczacy in lista_plikow:
                
                path_aktualnie_dodawne_zdjecie = path_aktualnie_dodawany_folder +"/"+ aktualny_plik_uczacy
                data = plt.imread(path_aktualnie_dodawne_zdjecie)
                zbior.append(data.copy())

                liczba_zdjec_w_zbiorze += 1

                if czy_uczacy_czy_walidujacy_czy_testowy == 0 or czy_uczacy_czy_walidujacy_czy_testowy == 1:

                    if liczba_zdjec_w_zbiorze >= ilosc_zbioru*liczba_zdjec:

                        if aktualny_plik_uczacy==lista_plikow[-1]:
                            pass
                        else:
                            index_ostatniego_dodanego = lista_plikow.index(aktualny_plik_uczacy)

                            for aktualny_plik_uczacy_2 in  lista_plikow[index_ostatniego_dodanego+1:len(lista_plikow)]:

                                path_aktualnie_dodawne_zdjecie = path_aktualnie_dodawany_folder +"/"+ aktualny_plik_uczacy_2
                                data = plt.imread(path_aktualnie_dodawne_zdjecie)
                                zbior.append(data.copy())

                                liczba_zdjec_w_zbiorze += 1

                        przestan_dodawac= True

                if przestan_dodawac== True:
                    break
            
            if przestan_dodawac == True:
                break

        zbior = np.asarray(zbior)

        return [zbior,aktualny_folder_uczacy]


    #Służy do odpowiedniego przygotowania danych do nauki
    def przygotuj_do_nauki(self):
        y_dab_uczacy = [0 for i in range (self.dab_zbior_uczacy.shape[0])]
        y_dab_walidujacy = [0 for i in range (self.dab_zbior_walidujacy.shape[0])]
        y_dab_testowy = [0 for i in range (self.dab_zbior_testowy.shape[0])]

        y_sosna_uczacy = [1 for i in range (self.sosna_zbior_uczacy.shape[0])]
        y_sosna_walidujacy = [1 for i in range (self.sosna_zbior_walidujacy.shape[0])]
        y_sosna_testowy = [1 for i in range (self.sosna_zbior_testowy.shape[0])]

        self.zbior_uczacy = [self.dab_zbior_uczacy,self.sosna_zbior_uczacy]
        self.zbior_uczacy = [item for podlista in self.zbior_uczacy for item in podlista]
        self.zbior_uczacy = np.asarray(self.zbior_uczacy)

        self.y_zbior_uczacy = [y_dab_uczacy,y_sosna_uczacy]
        self.y_zbior_uczacy = [item for podlista in self.y_zbior_uczacy for item in podlista]

        self.zbior_walidujacy = [self.dab_zbior_walidujacy,self.sosna_zbior_walidujacy]
        self.zbior_walidujacy = [item for podlista in self.zbior_walidujacy for item in podlista]
        self.zbior_walidujacy = np.asarray(self.zbior_walidujacy)

        self.y_zbior_walidujacy = [y_dab_walidujacy,y_sosna_walidujacy]
        self.y_zbior_walidujacy = [item for podlista in self.y_zbior_walidujacy for item in podlista]

        self.zbior_testowy = [self.dab_zbior_testowy,self.sosna_zbior_testowy]
        self.zbior_testowy = [item for podlista in self.zbior_testowy for item in podlista]
        self.zbior_testowy = np.asarray(self.zbior_testowy)

        self.y_zbior_testowy = [y_dab_testowy,y_sosna_testowy]
        self.y_zbior_testowy = [item for podlista in self.y_zbior_testowy for item in podlista]

        self.y_zbior_uczacy_one_hot = tf.keras.utils.to_categorical(self.y_zbior_uczacy, 2)
        self.y_zbior_walidujacy_one_hot = tf.keras.utils.to_categorical(self.y_zbior_walidujacy, 2)
        self.y_zbior_testowy_one_hot = tf.keras.utils.to_categorical(self.y_zbior_testowy, 2)

        self.zbior_uczacy = self.zbior_uczacy/255
        self.zbior_walidujacy = self.zbior_walidujacy/255
        self.zbior_testowy = self.zbior_testowy/255

        self.model = tf.keras.models.Sequential()

    #Służy do dodania warswty Conv2D o odpowiednich paramterach
    def dodaje_warstwe_conv2d(self,jaki_rozmiar,jaki_kernel,jaka_funkcja_aktywacji,jaki_padding):

        try:

            if self.ile_mam_warstw == 0:
                self.model.add(tf.keras.layers.Conv2D(jaki_rozmiar, kernel_size=(jaki_kernel, jaki_kernel), activation=jaka_funkcja_aktywacji, padding=jaki_padding, input_shape=(128, 128, 3)))
            else:
                self.model.add(tf.keras.layers.Conv2D(jaki_rozmiar, kernel_size=(jaki_kernel, jaki_kernel), activation=jaka_funkcja_aktywacji, padding=jaki_padding))
                
            print(self.model.summary())
            self.ile_mam_warstw += 1

            return "bez bledu"

        except ValueError:
            return "blad"

    #Służy do dodania warswty Poolingu o odpowiednich paramterach
    def dodaje_warstwe_poolingu(self,jaki_typ,jaki_rozmiar,jaki_krok):

        try:

            if jaki_typ == "MAX":
                self.model.add(tf.keras.layers.MaxPooling2D((jaki_rozmiar, jaki_rozmiar), strides=(jaki_krok, jaki_krok)))
            elif jaki_typ == "AVG":
                self.model.add(tf.keras.layers.AveragePooling2D((jaki_rozmiar, jaki_rozmiar), strides=(jaki_krok, jaki_krok)))

            self.ile_mam_warstw += 1
            return "bez bledu"

        except ValueError:
            return "blad"

    #Służy do dodania warswty Flatten
    def dodaje_warstwe_flatten(self):

        self.model.add(tf.keras.layers.Flatten())

        self.ile_mam_warstw += 1

    #Służy do dodania warswty Dense o odpowiednich paramterach
    def dodaje_warstwe_dense(self,ile_neuronow,jaka_funkcja_aktywacji):

        self.model.add(tf.keras.layers.Dense(ile_neuronow, activation=jaka_funkcja_aktywacji))

        self.ile_mam_warstw += 1

    #Wykorzystywana do rozpoczęcia nauki
    def rozpoczecie_nauki(self, jaki_optimizer,jaka_liczba_epok,jaki_batch,co_ile_odswiez,gdzie_zapisac_model,nazwa_modelu):

        wynik = []

        try:
            rysunki_online = Rysunki_w_trakcie_nauki(co_ile_mam_odswiezac=co_ile_odswiez, ile_bedzie_epok=jaka_liczba_epok)

            self.model.compile(optimizer = jaki_optimizer, loss = "binary_crossentropy", metrics = ["accuracy"])
            history = self.model.fit(x = self.zbior_uczacy, y = self.y_zbior_uczacy_one_hot, epochs = jaka_liczba_epok, 
            batch_size = jaki_batch, validation_data = (self.zbior_walidujacy, self.y_zbior_walidujacy_one_hot), callbacks = [rysunki_online])

            if gdzie_zapisac_model !="":
                self.model.save(gdzie_zapisac_model+"/"+nazwa_modelu+".h5")

            wynik.append("udalo sie stworzyc")
            wynik.append(history)

            return wynik

        except:
            wynik.append("niewlasciwy model")
            return wynik

    #Służy do określenia wyników dla zbioru testowego
    def wyniki_dla_zbioru_testowego(self):
        wyniki_dla_zbioru_testowego =  self.model.evaluate(x = self.zbior_testowy, y = self.y_zbior_testowy_one_hot)
        return wyniki_dla_zbioru_testowego

#Klasa za pomocą której istnieje możliwość dodania wykresów podczas nauki
class Rysunki_w_trakcie_nauki(tf.keras.callbacks.Callback):

    def __init__(self,co_ile_mam_odswiezac, ile_bedzie_epok):
        self.co_ile_mam_odswiezac = co_ile_mam_odswiezac
        self.ile_bedzie_epok = ile_bedzie_epok
    
    def on_train_begin(self,logs={}):
        self.losses = []
        self.acc = []
        self.losses_val = []
        self.acc_val = []
    
    # Ta funkcja wykonuje się tylko na końcu
    def on_epoch_end(self, epoch, logs={}):

        loss = logs.get('loss')
        accuracy = logs.get('accuracy')
        loss_val = logs.get('val_loss')
        accuracy_val = logs.get('val_accuracy')

        
        # self.logs.append(logs)
        self.losses.append(loss)
        self.acc.append(accuracy)
        self.losses_val.append(loss_val)
        self.acc_val.append(accuracy_val)
        
        if epoch > 0 and (epoch+1)%self.co_ile_mam_odswiezac==0 or epoch+1 == self.ile_bedzie_epok:

            clear_output(wait=True)
            N = np.arange(0, len(self.losses))

            plt.style.use("seaborn")
            
            fig, ax = plt.subplots(2,2, figsize=(12,7))
            ax[0,0].plot(N, self.losses)
            ax[0,0].set_title("Loss - zbiór uczący, dla epoki " + str(epoch+1))
            ax[0,0].set_ylabel("Loss")

            ax[0,1].plot(N, self.acc)
            ax[0,1].set_title("Accuracy - zbiór uczący, dla epoki "+str(epoch+1))
            ax[0,1].set_ylabel("Accuracy")

            ax[1,0].plot(N, self.losses_val)
            ax[1,0].set_title("Loss - zbiór walidujący, dla epoki "+str(epoch+1))
            ax[1,0].set_ylabel("Loss")

            ax[1,1].plot(N, self.acc_val)
            ax[1,1].set_title("Accuracy - zbiór walidujący, dla epoki "+str(epoch+1))
            ax[1,1].set_ylabel("Accuracy")

            plt.show()