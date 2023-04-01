clc;
clear;

tytul = ['  Projekt 4 - IPP,                                        '
         '  Wykonali:                                               '
         '  ŁF                       '
         '  Bartłomiej Guś nr albumu 297415 gr.IPAUT-161            '
         '  Wybierz metodę:                                         '];

     
odpowiedz=[1,2,3,4];
wybor=menu(tytul,'Zadanie 1 - Metoda Bisekcji','Zadanie 2 - Metoda Newtona Rhapsona', 'Zadanie 3 - Metoda False Postion', 'Zadanie 4 - Porówananie');

        Podaj_p0 = ('Podaj wartość ciśnienia otoczenia w [Pa]');
        
        Podaj_ilosc_Toulenu = ('Podaj wartość ilości toulenu w [-]');
        Podaj_ilosc_Benzenu = ('Podaj wartość ilości benzenu w [-]');
        
        Podaj_A_Toulenu = ('Podaj wartość współczynnika A toulenu w [-]');
        Podaj_B_Toulenu = ('Podaj wartość współczynnika B toulenu w [-]');
        Podaj_C_Toulenu = ('Podaj wartość współczynnika C toulenu w [-]');
        
        Podaj_A_Benzenu = ('Podaj wartość współczynnika A benzenu w [-]');
        Podaj_B_Benzenu = ('Podaj wartość współczynnika B benzenu w [-]');
        Podaj_C_Benzenu = ('Podaj wartość współczynnika C benzenu w [-]');
        
        Podaj_T_zgadywane = ('Podaj wartość temperatury początkowej T w [K]');
                
        answer=inputdlg({Podaj_p0,Podaj_ilosc_Toulenu,Podaj_ilosc_Benzenu,Podaj_A_Toulenu,Podaj_B_Toulenu,Podaj_C_Toulenu,Podaj_A_Benzenu,Podaj_B_Benzenu,Podaj_C_Benzenu,Podaj_T_zgadywane});
        
       
            if isempty(str2num(answer{1,1}))
                p0 = 760;
            else p0 = str2num(answer{1,1});
            end

            if isempty(str2num(answer{2,1}))
                ilosc_Toulenu = 0.5;
            else ilosc_Toulenu = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                ilosc_Benzenu = 0.5;
            else ilosc_Benzenu = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                A_Toulenu = 4.08245;
            else A_Toulenu = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                B_Toulenu = 1346.382;
            else B_Toulenu = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                C_Toulenu = -53.508;
            else C_Toulenu = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                A_Benzenu = 6.87987;
            else A_Benzenu = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                B_Benzenu = 1196.76;
            else B_Benzenu= str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                C_Benzenu = 219.161;
            else C_Benzenu = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                T_zgadywane = 80;
            else T_zgadywane = str2num(answer{10,1});
            end

switch odpowiedz(wybor)
    case 1      
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            krok_T = 10;
            
            po_jakiej_stronie_bylem_ostatnio = false; 
            
            if(P_T_B-p0>0)
                po_jakiej_stronie_bylem_ostatnio = true;
            end
            
            licznik = 1;
            
            T = zeros(1,licznik);
            
            T(licznik) = T_zgadywane;
            
            
            while(abs(p0-P_T_B)>=0.01)
                
                if(P_T_B-p0>0)
                    if(po_jakiej_stronie_bylem_ostatnio == false)
                            krok_T=krok_T/2;
                    end
                    T_zgadywane = T_zgadywane - krok_T;
                    po_jakiej_stronie_bylem_ostatnio = true;
                else if (P_T_B-p0<0)
                        if(po_jakiej_stronie_bylem_ostatnio == true)
                            krok_T=krok_T/2;
                        end
                        T_zgadywane = T_zgadywane + krok_T;
                        po_jakiej_stronie_bylem_ostatnio = false;
                    end
                end
                
                P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
                P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
                P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
                
                licznik = licznik + 1;
                
                T(licznik) = T_zgadywane;
               
            end
            
            y = ilosc_Toulenu*P_Toulenu/p0
            
            1-y
            
            X = 0:1:licznik-1;
            
            plot(X,T,'k','LineWidth',1);
            xlabel('N [-]');
            ylabel('T[°C]');
            legend('Metoda bisekcji');
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys]);
            
            title('Wykres zmiany temperatury w zależności od numeru iteracji dla metody Bisekcji');
            
        
    case 2 
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            wartosc_1 = p0 - P_T_B;
            
            licznik = 1;
            
            T = zeros(1,licznik);
            
            T(licznik) = T_zgadywane;
            
          while(abs(wartosc_1)>=0.01)
            
            T_zgadywane2 = T_zgadywane + 0.1;
            
            P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
            P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
            P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;

            wartosc_2 = p0 - P_T_B2;   
            
            rozniczka = (wartosc_2-wartosc_1)/(T_zgadywane2 - T_zgadywane);
            
            T_zgadywane = T_zgadywane - wartosc_1/rozniczka;
            
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            licznik = licznik + 1;
            T(licznik) = T_zgadywane;
            
            wartosc_1 = p0 - P_T_B;
            
          end
          
            y = ilosc_Toulenu*P_Toulenu/p0
            
            1-y

            X = 0:1:licznik-1;
            
            plot(X,T,'r','LineWidth',1);
            xlabel('N [-]');
            ylabel('T[°C]');
            legend('Metoda Newtona - Raphsona');
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys]);
            
            title('Wykres zmiany temperatury w zależności od numeru iteracji dla metody Newtona - Raphsona');
       
    case 3
            
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            wartosc_1 = P_T_B - p0;  
            
            T_zgadywane2 = 140;
            
            P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
            P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
            P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
            wartosc_2 = P_T_B2 - p0; 
            
            licznik = 1;
            
            T = zeros(1,licznik);
            
            T(licznik) = T_zgadywane;
            
            if(wartosc_1<0)
                while(wartosc_2<=0)
                    T_zgadywane2 =T_zgadywane2 + 10;
            
                    P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
                    P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
                    P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
                    wartosc_2 = P_T_B2 - p0; 
                end
            else
                 while(wartosc_2>=0)
                    T_zgadywane2 =T_zgadywane2 - 10;
            
                    P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
                    P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
                    P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
                    wartosc_2 = P_T_B2 - p0;  
                 end
            end
            
            while (abs(wartosc_1)>=0.01)
                
                T_S = T_zgadywane2 - (wartosc_2*(T_zgadywane2 - T_zgadywane))/(wartosc_2-wartosc_1);
                
                P_Toulenu_S = 10^(A_Toulenu - B_Toulenu/(T_S + C_Toulenu));
                P_Benzenu_S = 10^(A_Benzenu - B_Benzenu/(T_S + C_Benzenu));
            
                P_T_B_S = ilosc_Toulenu*P_Toulenu_S + (1 - ilosc_Toulenu)*P_Benzenu_S;
                
                wartosc_S = P_T_B_S - p0;
                
                if(wartosc_S<0)
                    T_zgadywane = T_S;      
                    wartosc_1 = wartosc_S;
                else if (wartosc_S>0)
                    T_zgadywane2 = T_S;
                    wartosc_2 = wartosc_S;
                    end
                end
                
            licznik = licznik + 1;
            
            T(licznik) = T_S;
            
            end
            
            y = ilosc_Toulenu*P_Toulenu_S/p0
            
            1-y
            
            X = 0:1:licznik-1;

            plot(X,T,'b','LineWidth',1);
            xlabel('N [-]');
            ylabel('T[°C]');
            legend('Metoda False Position');
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys]);
            
            title('Wykres zmiany temperatury w zależności od numeru iteracji dla metody False Position');
            
    case 4
          
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            krok_T = 10;
            
            po_jakiej_stronie_bylem_ostatnio = false; 
            
            if(P_T_B-p0>0)
                po_jakiej_stronie_bylem_ostatnio = true;
            end
            
            licznik = 1;
            
            T = zeros(1,licznik);
            
            T(licznik) = T_zgadywane;
            
            while(abs(p0-P_T_B)>=0.01)
                
                if(P_T_B-p0>0)
                    if(po_jakiej_stronie_bylem_ostatnio == false)
                            krok_T=krok_T/2;
                    end
                    T_zgadywane = T_zgadywane - krok_T;
                    po_jakiej_stronie_bylem_ostatnio = true;
                else if (P_T_B-p0<0)
                        if(po_jakiej_stronie_bylem_ostatnio == true)
                            krok_T=krok_T/2;
                        end
                        T_zgadywane = T_zgadywane + krok_T;
                        po_jakiej_stronie_bylem_ostatnio = false;
                    end
                end
                
                P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
                P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
                P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
                
                licznik = licznik + 1;
                
                T(licznik) = T_zgadywane;
               
            end

            X = 0:1:licznik-1;

            % Metoda N-R

            T_zgadywane = 80;

            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            wartosc_1 = p0 - P_T_B;
            
            licznik = 1;
            
            T_2 = zeros(1,licznik);
            
            T_2(licznik) = T_zgadywane;
            
          while(abs(wartosc_1)>=0.01)
            
            T_zgadywane2 = T_zgadywane + 0.1;
            
            P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
            P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
            P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;

            wartosc_2 = p0 - P_T_B2;   
            
            rozniczka = (wartosc_2-wartosc_1)/(T_zgadywane2 - T_zgadywane);
            
            T_zgadywane = T_zgadywane - wartosc_1/rozniczka;
            
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            licznik = licznik + 1;
            T_2(licznik) = T_zgadywane;
            
            wartosc_1 = p0 - P_T_B;
            
          end

          X_2 = 0:1:licznik-1;
 
          % Metoda False   
          
            T_zgadywane = 80;
          
            P_Toulenu = 10^(A_Toulenu - B_Toulenu/(T_zgadywane + C_Toulenu));
            P_Benzenu = 10^(A_Benzenu - B_Benzenu/(T_zgadywane + C_Benzenu));
            
            P_T_B = ilosc_Toulenu*P_Toulenu + (1 - ilosc_Toulenu)*P_Benzenu;
            
            wartosc_1 = P_T_B - p0;  
            
            T_zgadywane2 = 140;
            
            P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
            P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
            P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
            wartosc_2 = P_T_B2 - p0; 
            
            licznik = 1;
            
            T_3 = zeros(1,licznik);
            
            T_3(licznik) = T_zgadywane;
            
            if(wartosc_1<0)
                while(wartosc_2<=0)
                    T_zgadywane2 =T_zgadywane2 + 10;
            
                    P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
                    P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
                    P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
                    wartosc_2 = P_T_B2 - p0; 
                end
            else
                 while(wartosc_2>=0)
                    T_zgadywane2 =T_zgadywane2 - 10;
            
                    P_Toulenu2 = 10^(A_Toulenu - B_Toulenu/(T_zgadywane2 + C_Toulenu));
                    P_Benzenu2 = 10^(A_Benzenu - B_Benzenu/(T_zgadywane2 + C_Benzenu));
            
                    P_T_B2 = ilosc_Toulenu*P_Toulenu2 + (1 - ilosc_Toulenu)*P_Benzenu2;
            
                    wartosc_2 = P_T_B2 - p0;  
                 end
            end
            
            while (abs(wartosc_1)>=0.01)
                
                T_S = T_zgadywane2 - (wartosc_2*(T_zgadywane2 - T_zgadywane))/(wartosc_2-wartosc_1);
                
                P_Toulenu_S = 10^(A_Toulenu - B_Toulenu/(T_S + C_Toulenu));
                P_Benzenu_S = 10^(A_Benzenu - B_Benzenu/(T_S + C_Benzenu));
            
                P_T_B_S = ilosc_Toulenu*P_Toulenu_S + (1 - ilosc_Toulenu)*P_Benzenu_S;
                
                wartosc_S = P_T_B_S - p0;
                
                if(wartosc_S<0)
                    T_zgadywane = T_S;      
                    wartosc_1 = wartosc_S;
                else if (wartosc_S>0)
                    T_zgadywane2 = T_S;
                    wartosc_2 = wartosc_S;
                    end
                end
                
            licznik = licznik + 1;
            
            T_3(licznik) = T_S;
            
            end
            
            X_3 = 0:1:licznik-1;
            
            plot(X,T,'k',X_2,T_2,'r',X_3,T_3,'b','LineWidth',1);
            xlabel('N [-]');
            ylabel('T[°C]');
            legend('Metoda Bisekcji','Metoda Newtona - Raphsona','Metoda False Position');
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys]);
            
            title('Wykres zmiany temperatury w zależności od numeru iteracji dla różnych metod');
        
end
        