import cv2
import numpy as np
import math

#Dodatkowy poziom do thresha przy progowaniu calego zdjecia, dodawany do wartosci tla zdjecia
POZIOM_THRESH = 17

#Najmniejsza mozliwa powierzchni karty
CARD_NAJMNIEJSZA_POWIERZCHNIA = 10000

#Najwieksze pole symbolu glownego na karcie i najmniejsze
MAX_POLE_SYMBOLU = 100000
MIN_POLE_SYMBOLU = 5000

#Tabela z wartosciami wzorcowymi HuMoments
HU_MOMENTY = np.array([[1.61208681e-01, 6.55484277e-04, 5.58412227e-08, 3.20465662e-10, -8.34160560e-19, -5.66997898e-12, -1.06863517e-18, 'Karta Stop'],
                      [2.52586293e-01, 2.88697398e-02, 2.09516532e-03, 4.95847459e-04, 4.94921274e-07, 8.16782123e-05, 1.02359394e-07,'UNO Reverse Card'],
                      [3.48446680e-01, 2.85770641e-02, 1.99812298e-04, 2.01477430e-05, -6.34921989e-10, -3.16904121e-06, -1.10953136e-09,'2'],
                      [2.06623702e-01, 5.02075815e-03, 3.40838598e-03, 5.21831868e-05, -1.64281430e-08, -2.07043763e-06, -1.46439481e-08,'4'],
                      [3.24642586e-01, 1.72536349e-02, 3.43356644e-04, 2.15143649e-06, -3.52364007e-11, -2.67043088e-07, -4.66652713e-11,'5']])

#Za pomoca niej można wyswietlic zdjecie
def pokaz(nazwa,obraz):
    cv2.imshow(nazwa,obraz)
    cv2.waitKey()

#Klasa w ktorej nastepowalo wczytanie calego obrazu i znalaznienie kart oraz ich zwrocenie
class Obraz:

    #Wczytanie zdjecia i odczytanie wysokosci oraz szerokosci zdjecia
    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path,cv2.IMREAD_UNCHANGED)
        self.wysokosc = self.image.shape[0]
        self.szerokosc = self.image.shape[1]

    #Poczatkowa obrobka zdjecia, ktora obejmowala zmiane na przestrzen w skali szarosci jak i progowanie
    def poczatkowa_obrobka(self):

        self.image = cv2.medianBlur(self.image,5)
        # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        # self.image = cv2.GaussianBlur(self.image, (3,3), 0)

        szary = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        poziom_tla = szary[int(self.wysokosc/2)][int(self.szerokosc/2)]
        wartosc_thresh = poziom_tla + POZIOM_THRESH

        ret, self.image_threshed = cv2.threshold(szary,wartosc_thresh,255,cv2.THRESH_BINARY)

    #Znajduje kontury i odrzuca te które pole powierzchni jest mniejsze od mozliwego pola powierzchni karty, zwraca zdjecia z samymi kartami
    def wyszukiwanie_kart(self):
        
        kontury, hierarchia = cv2.findContours(self.image_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        nic,rows,columns = hierarchia.shape

        self.ile_jest_kart = rows

        #cv2.drawContours(self.image_threshed, kontury, -1, (100, 100, 100), 3, cv2.LINE_AA)
        #cv2.imshow('Obraz z konturami', self.image_threshed)
        #cv2.waitKey()

        # for i, contour in enumerate(kontury[3]): # Do rysowania konturów wszystkich
        #      for j, contour_point in enumerate(kontury[3]): #
        #         #  print(j, contour_point[0], contour_point[0][1])
        #          cv2.circle(self.image_threshed, ((contour_point[0][0], contour_point[0][1])), 2, (100, 100, 100), 2, cv2.LINE_AA)
        # cv2.imshow('Gdzie sa zaznaczone kontury', self.image_threshed)
        # cv2.waitKey()

        lista_prawidlowych_konturow = []

        for i in range(self.ile_jest_kart):

            if len(kontury[i]) < 4:
                next

            size = cv2.contourArea(kontury[i])

            if size > CARD_NAJMNIEJSZA_POWIERZCHNIA:
                lista_prawidlowych_konturow.append(kontury[i])

        self.ile_jest_kart = len(lista_prawidlowych_konturow)

        out = []

        for i in range(self.ile_jest_kart):
            out.append(self.oblicz_transformacje_i_oblicz_wymiary_karty_oraz_srodek_karty(lista_prawidlowych_konturow[i]))

        return out

    #Oblicza transformacje perspektywiczną i zwraca pojedyncze zdjecia kart oraz srodek karty
    def oblicz_transformacje_i_oblicz_wymiary_karty_oraz_srodek_karty(self, kontury):
        
        paramtery = 0.01*cv2.arcLength(kontury,True)
        approx = cv2.approxPolyDP(kontury,paramtery,True)

        punkty_z_kontur = np.float32(approx[:][0:4])

        szerokosc = cv2.norm(punkty_z_kontur[0] - punkty_z_kontur[1])
        wysokosc = cv2.norm(punkty_z_kontur[1] - punkty_z_kontur[2])

        # Sluzylo do narysowania konkretnych kontur
        # for contour_point in (punkty_z_kontur[1:2]): # Do rysowania gdzie sa kontury
        #          cv2.circle(self.image_threshed2, ((int(contour_point[0][0]), int(contour_point[0][1]))), 2, (100, 50, 100), 2, cv2.LINE_AA)
        # cv2.imshow('Approx', self.image_threshed2)
        # cv2.waitKey()

        # cv2.rectangle(self.image_threshed,(x,y),(x+wysokosc,y+szerokosc),(100,100,10),2)
        # cv2.imshow('Approx',self.image_threshed)
        # cv2.waitKey()

        punkty_z_obliczen = np.float32([[szerokosc,0],
                                        [0,0],
                                        [0,wysokosc],
                                        [szerokosc,wysokosc]])

        Transformacja = cv2.getPerspectiveTransform(punkty_z_kontur,punkty_z_obliczen)

        image_out = cv2.warpPerspective(self.image,Transformacja,(int(szerokosc),int(wysokosc)))

        momenty = cv2.moments(kontury)
        self.srodek_x = momenty['m10']/momenty['m00']
        self.srodek_y = momenty['m01']/momenty['m00']

        if wysokosc < szerokosc:
            image_out = cv2.rotate(image_out,cv2.ROTATE_90_CLOCKWISE)

        out = [image_out,self.srodek_x,self.srodek_y]

        return out

#Klasa ktora przetrzymuje pojedyncze zdjecia kart, przetwarza je i rozpoznaje symbole
class Kart:

    #Odczytanie wysokosci i szerokosci zdjecia oraz odwolanie do funkcji detekcja_koloru_karty
    def __init__(self, image):
        self.image = image[0]
        self.image_do_obrobki = image[0].copy()
        self.wysokosc = self.image.shape[0]
        self.szerokosc = self.image.shape[1]
        self.srodek_x_na_obrazie = image[1]
        self.srodek_y_na_obrazie = image[2]

        self.detekcja_koloru_karty()

    #Sluzyla do detekcji koloru zdjecia oraz zamiane na czarne tlo
    def detekcja_koloru_karty(self):
        self.image_hsv = cv2.cvtColor(self.image_do_obrobki, cv2.COLOR_BGR2HSV)

        #Służyło do odczytania wartosci HSV z karty
        # def do_odczytu(event,x,y,flags,param):
        #     if event == cv2.EVENT_LBUTTONDBLCLK: #left mouse double click 
        #         print("HSV values:", self.image_hsv[y,x])
        #         cv2.circle(self.image_hsv, (x, y), 5, (0, 0, 0), 2, 4)

        # while True:

        #     cv2.imshow("RBG",self.image)
        #     cv2.imshow("HSV",self.image_hsv)

        #     cv2.setMouseCallback("HSV", do_odczytu)
        #     # cv2.setMouseCallback("Original",do_odczytu)

        #     if cv2.waitKey(1) &0xFF == ord("q"):
        #         cv2.destroyAllWindows()
        #         break

        dolna_wartosc_czerwonego = np.array([0,100,100])
        gorna_wartosc_czerwonego = np.array([10,255,255])

        dolna_wartosc_zoltego = np.array([14,50,50])
        gorna_wartosc_zoltego = np.array([40,255,255])

        dolna_wartosc_zielonego = np.array([45,100,100])
        gorna_wartosc_zielonego = np.array([85,255,255])

        dolna_wartosc_niebieskiego = np.array([100,100,100])
        gorna_wartosc_niebieskigo = np.array([140,255,255])

        czerwony = cv2.inRange(self.image_hsv, dolna_wartosc_czerwonego, gorna_wartosc_czerwonego)
        zolty = cv2.inRange(self.image_hsv, dolna_wartosc_zoltego, gorna_wartosc_zoltego)
        zielony = cv2.inRange(self.image_hsv, dolna_wartosc_zielonego, gorna_wartosc_zielonego)
        niebieski = cv2.inRange(self.image_hsv, dolna_wartosc_niebieskiego, gorna_wartosc_niebieskigo)

        zliczaj_czerwony  = np.count_nonzero(czerwony)
        zliczaj_zolty = np.count_nonzero(zolty)
        zliczaj_zielony = np.count_nonzero(zielony)
        zliczaj_niebieski = np.count_nonzero(niebieski)

        lst_zliczaj = [zliczaj_czerwony,zliczaj_zolty,zliczaj_zielony,zliczaj_niebieski]

        max_zliczaj = max(lst_zliczaj)

        if lst_zliczaj.index(max_zliczaj) == 0:
            self.moj_kolor = "czerwony"
            self.image_do_obrobki[czerwony>0] = (0,0,0)
        elif lst_zliczaj.index(max_zliczaj) == 1:
            self.moj_kolor = "zolty"
            self.image_do_obrobki[zolty>0] = (0,0,0)
        elif lst_zliczaj.index(max_zliczaj) == 2:
            self.moj_kolor = "zielony"
            self.image_do_obrobki[zielony>0] = (0,0,0)
        elif lst_zliczaj.index(max_zliczaj) == 3:
            self.moj_kolor = "niebieski"
            self.image_do_obrobki[niebieski>0] = (0,0,0)

        # Wyświetlenie zdjęć z czarnym tłem
        # cv2.imshow("Zdjecie z 'czarnym' tlem",self.image_do_obrobki)
        # cv2.waitKey(0)

    #Zamina na przestrzen w skali szarosci oraz dobranie odpowiedniego progowania jak i zamiana na zdjecie sprogowane
    def poczatkowa_obrobka(self):
        szary = cv2.cvtColor(self.image_do_obrobki, cv2.COLOR_BGR2GRAY)

        poziom_thresh_karty = 0

        if self.moj_kolor == "czerwony":
            poziom_thresh_karty = 95
        elif self.moj_kolor == "zolty":
            poziom_thresh_karty = 95
        elif self.moj_kolor == "zielony":
            poziom_thresh_karty = 120
        elif self.moj_kolor == "niebieski":
            poziom_thresh_karty = 120

        ret, self.image_threshed = cv2.threshold(szary,poziom_thresh_karty,255,cv2.THRESH_BINARY)

    #Wykorzystywana do znalezienia konturow oraz wyznaczenia konturow symboli glownych jak i obliczenie momentow oraz posiada odwolanie do funkcji przyporzadkowanie_symbolu
    def odczytanie_momentow(self):
        kontury, hierarchia = cv2.findContours(self.image_threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        lst_konturow_symboli = []
        lst_momenty = []

        for i in kontury:

            if  int(cv2.contourArea(i))>MIN_POLE_SYMBOLU and int(cv2.contourArea(i))<MAX_POLE_SYMBOLU:

                momenty = cv2.moments(i)

                srodek_x = momenty['m10']/momenty['m00']
                srodek_y = momenty['m01']/momenty['m00']

                if abs(self.szerokosc/2 - srodek_x) < 50 and abs(self.wysokosc/2 - srodek_y) < 100:
                    cv2.circle(self.image_threshed, (int(srodek_x), int(srodek_y)), 10, (0, 0, 0), 2, 4)
                    lst_konturow_symboli.append(i)
                    lst_momenty.append(momenty)


        # Służyło do narysowania konkretnych kontur
        # for i, contour in enumerate(lst_konturow_symboli[0]): # Do rysowania konturów wszystkich
        #      for j, contour_point in enumerate(lst_konturow_symboli[0]): #
        #         #  print(j, contour_point[0], contour_point[0][1])
        #          cv2.circle(self.image_threshed, ((contour_point[0][0], contour_point[0][1])), 2, (100, 100, 100), 2, cv2.LINE_AA)
        # cv2.imshow('Gdzie sa zaznaczone kontury', self.image_threshed)
        # cv2.waitKey()

        self.przyporzadkowanie_symbolu(lst_konturow_symboli,lst_momenty)

    #Przyporzadkowuje symbole na podstawie "znormalizowanych" wartosci HuMoment
    def przyporzadkowanie_symbolu(self,lst_konturow_symboli,lst_momenty):

        if len(lst_konturow_symboli) == 2:

            self.jaka_jestem_karta = "UNO Reverse Card"
        else:

            if len(lst_momenty) > 0:
                huMomenty = cv2.HuMoments(lst_momenty[0])

                max_odelglosc = 100000
                suma=0
                HuMomenty_odniesienia_znormalizowane = []

                HuMomenty_z_karty_znormalizowane = [(math.log10(abs(x))) for x in huMomenty]

                for x in HU_MOMENTY:
                    for y in range(0,7):
                        HuMomenty_odniesienia_znormalizowane.append(math.log10(abs(float(x[y]))))

                    for z in range(0,7):
                        suma = suma + (HuMomenty_odniesienia_znormalizowane[z]-HuMomenty_z_karty_znormalizowane[z])**2

                    if math.sqrt(suma)<max_odelglosc:
                        max_odelglosc = math.sqrt(suma)

                        self.jaka_jestem_karta = x[7]

                    suma=0
                    HuMomenty_odniesienia_znormalizowane = []
            else:
                self.jaka_jestem_karta = 'Nie wiem jaka jestem'
                

if __name__ == "__main__":

    #Przetrzymuje wartosc sumy cyfr na wszystkich kartach 
    suma_cyfr_na_wszystkich_kartach = 0

    #Sciezka do zdjecia
    path = "D:\Studia\StudiaMGR\CPO\Podstawa_obrazy_testowe\Image__2021-11-18__11-08-28.png"

    #Inicjacja obiektu przetrzymujacego zdjecie calej karty
    obraz_wejsciowy = Obraz(path)
    #Wykonanie poczatkowej obrobki zdjecia
    obraz_wejsciowy.poczatkowa_obrobka()
    #Przetrzymuje liste zdjec kart
    dane_do_kart = obraz_wejsciowy.wyszukiwanie_kart()

    #Stworznie list obiektow Kart z zdjeciami kart
    lst_kart = [Kart(x) for x in dane_do_kart]

    # Wyświetlenie zdjęć kart z 
    # for i in range(len(lst_kart)):
    #     pokaz("Zdjecie karty",lst_kart[i].image)

    #Wykonanie poczatkowej obrobki zdjec jak i odczytanie momentow na calej liscie zdjec
    for i in range(len(lst_kart)):
        lst_kart[i].poczatkowa_obrobka()
        lst_kart[i].odczytanie_momentow()

    #Obliczenie sumy cyfr na wszystkich kartach na podstawie symboli try i expect sluzy do tego, ze przy odczycie wartosci ktorej nie da sie zamienic na int
    #program sie nie konczyl
    for i in lst_kart:
        try:
            suma_cyfr_na_wszystkich_kartach = suma_cyfr_na_wszystkich_kartach+int(i.jaka_jestem_karta)
        except ValueError:
            next
    
    #Naniesinie wynikow na zdjecie kart takich jak sumy cyfr na wszystkich kartach jesli symbol to cyfra 
    #a w przypadku kart specjalnych to naniesinie nazwy typu karty jak i srodka karty
    for i in lst_kart:

        if i.jaka_jestem_karta == "4" or i.jaka_jestem_karta == "2" or i.jaka_jestem_karta == "5":
            text = "Suma wszystkich cyfr na kartach to: " + str(suma_cyfr_na_wszystkich_kartach)
            cv2.putText(i.image,text,(10,180),cv2.cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2,cv2.LINE_AA)
        elif i.jaka_jestem_karta == "Karta Stop" or i.jaka_jestem_karta == "UNO Reverse Card":
            text1 = "Jestem karta typu: "+i.jaka_jestem_karta
            cv2.putText(i.image,text1,(10,180),cv2.cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2,cv2.LINE_AA)
            text2 = "Wspolrzedne srodka to: " + str(round(i.srodek_y_na_obrazie,2)) + " " + str(round(i.srodek_x_na_obrazie,2))
            cv2.putText(i.image,text2,(10,220),cv2.cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2,cv2.LINE_AA)
            #Sluzylo do sprawdzania srodka karty na obrazie
            cv2.circle(obraz_wejsciowy.image, (int(i.srodek_x_na_obrazie), int(i.srodek_y_na_obrazie)), 10, (0, 0, 0), 2, 4)

    # Sprawdzenie czy dobrze znajduje srodki kart na obrazie
    # obraz_wejsciowy.image = cv2.resize(obraz_wejsciowy.image,(1500,1000))
    # pokaz("Z kropkami:", obraz_wejsciowy.image)

    #Przedstawienie wynikow
    for i in range(len(lst_kart)):
        pokaz("Zdjecie wynikowe",lst_kart[i].image)

    cv2.destroyAllWindows()