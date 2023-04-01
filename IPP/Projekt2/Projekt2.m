clc;
clear;

tytul = ['  Projekt 2 - IPP,                                        '
         '  Wykonali:                                               '
         '  ŁJ                       '
         '  Bartłomiej Guś nr albumu 297415 gr.IPAUT-161            '
         '  Wybierz metodę:                                         '];

     
odpowiedz=[1,2,3];
wybor=menu(tytul,'Zadanie 1 - bez mleka','Zadanie 2 - mleko od razu','Zadanie 3 - mleko po jakimś czasie');

A_s_wew = 1;
A_s_zew = 1;
V_kawy= 1;
cp_kawy = 1;
        
h_kawy=1;
        
        
m_kawy=1;
m_mleka = 1;
        
ro_kawy_2 = 1;
            
A_s_zew_2 = 1;
V_s=1;
A_s_wew_2 = 1;
A_p_kawa = 1;
V_kawy_2=1;
cp_s=1;
cp_kawy_2 = 1;

T0_mleka = 1;
ro_mleka = 1;
h0_mleka = 1;

T_symulacji = 4000;
Timeop = T_symulacji + 1;

switch odpowiedz(wybor)
    case 1
        
        Podaj_Tp = ('Podaj wartość temperatury panującej w pomieszczeniu w [K]');
        Podaj_alfa_p_s = ('Podaj wartość współczynnika wymiany ciepła powietrze - ściana kubka w [W/(m2*K)]');
        Podaj_r = ('Podaj wartość promienia kubka w [m]');
        Podaj_h =  ('Podaj wartość wysokości kubka w [m]');
        Podaj_g = ('Podaj wartość grubości ścianki w [m]');
        Podaj_ro_s = ('Podaj wartość gęstości materiału z jakiego wykonana jest ścianka kubka w [kg/m3]');
        Podaj_alfa_s_k = ('Podaj wartość współczynnika wymiany ciepła ścianka - kawa w [W/(m2*K)]');
        Podaj_T0_s = ('Podaj początkową wartość temperatury kubka w [K]');
        Podaj_h_kawy = ('Podaj wartość wysokości kawy z wrzątkiem w [m]');
        Podaj_alfa_p_kawa = ('Podaj wartość współczynnika wymiany ciepła powietrze - kawa w [W/(m2*K)]');
        Podaj_ro_kawy = ('Podaj wartość gęstości kawy w [kg/m3]');
        Podaj_T0_kawy = ('Podaj początkową wartość temperatury kawy w [K]');
        
        
        answer=inputdlg({Podaj_Tp,Podaj_alfa_p_s,Podaj_r,Podaj_h,Podaj_g,Podaj_ro_s,Podaj_alfa_s_k,Podaj_T0_s,Podaj_h_kawy,Podaj_alfa_p_kawa,Podaj_ro_kawy,Podaj_T0_kawy});
        
       
            if isempty(str2num(answer{1,1}))
                Tp = 293;
            else Tp = str2num(answer{1,1});
            end

            if isempty(str2num(answer{2,1}))
                alfa_p_s = 12;
            else alfa_p_s = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                r = 0.56;
            else r = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                h = 1;
            else h = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                g = 0.01;
            else g = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                ro_s = 7500;
            else ro_s = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                alfa_s_kawa = 10;
            else alfa_s_kawa = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                T0_s = 293;
            else T0_s = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                h_kawy = 0.5;
            else h_kawy = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                alfa_p_kawa = 10;
            else alfa_p_kawa = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                ro_kawy = 1100;
            else ro_kawy = str2num(answer{11,1});
            end
            
            if isempty(str2num(answer{12,1}))
                T0_kawy = 323;
            else T0_kawy = str2num(answer{12,1});
            end
            
            
        A_s_zew =(2*h-h_kawy)*2*3.14*r;
        V_s=3.14*((r+g)*(r+g)-r*r)*h;
        A_s_wew = 2*3.14*r*h_kawy;
        A_p_kawa = 3.14*r*r;
        V_kawy=3.14*r*r*h_kawy;
        cp_s=452;
        cp_kawy = 4000;
        
        
    case 2
        
        Podaj_Tp = ('Podaj wartość temperatury panującej w pomieszczeniu w [K]');
        Podaj_alfa_p_s = ('Podaj wartość współczynnika wymiany ciepła powietrze - ściana kubka w [W/(m2*K)]');
        Podaj_r = ('Podaj wartość promienia kubka w [m]');
        Podaj_h =  ('Podaj wartość wysokości kubka w [m]');
        Podaj_g = ('Podaj wartość grubości ścianki w [m]');
        Podaj_ro_s = ('Podaj wartość gęstości materiału z jakiego wykonana jest ścianka kubka w [kg/m3]');
        Podaj_alfa_s_k = ('Podaj wartość współczynnika wymiany ciepła ścianka - kawa w [W/(m2*K)]');
        Podaj_T0_s = ('Podaj początkową wartość temperatury kubka w [K]');
        Podaj_h_kawy = ('Podaj wartość wysokości kawy z wrzątkiem w [m]');
        Podaj_alfa_p_kawa = ('Podaj wartość współczynnika wymiany ciepła powietrze - kawa w [W/(m2*K)]');
        Podaj_ro_kawy = ('Podaj wartość gęstości kawy w [kg/m3]');
        Podaj_T0_kawy = ('Podaj początkową wartość temperatury kawy [K]');
        Podaj_T0_mleka = ('Podaj początkową wartość temperatury mleka w [K]');
        Podaj_ro_mleka = ('Podaj wartość gęstości mleka w [kg/m3]');
        Podaj_ho_mleka = ('Podaj wartość wysokości mleka w [m]');
        
        answer=inputdlg({Podaj_Tp,Podaj_alfa_p_s,Podaj_r,Podaj_h,Podaj_g,Podaj_ro_s,Podaj_alfa_s_k,Podaj_T0_s,Podaj_h_kawy,Podaj_alfa_p_kawa,Podaj_ro_kawy,Podaj_T0_kawy,Podaj_T0_mleka,Podaj_ro_mleka,Podaj_ho_mleka});
        
       
            if isempty(str2num(answer{1,1}))
                Tp = 293;
            else Tp = str2num(answer(1,1));
            end

            if isempty(str2num(answer{2,1}))
                alfa_p_s = 10;
            else alfa_p_s = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                r = 0.04;
            else r = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                h = 0.09;
            else h = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                g = 0.002;
            else g = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                ro_s = 2400;
            else ro_s = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                alfa_s_kawa = 50;
            else alfa_s_kawa = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                T0_s = 293;
            else T0_s = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                h0_kawy = 0.05;
            else h0_kawy = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                alfa_p_kawa = 10;
            else alfa_p_kawa = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                ro_kawy = 1200;
            else ro_kawy = str2num(answer{11,1});
            end
            
            if isempty(str2num(answer{12,1}))
                T0_kawy = 360;
            else T0_kawy = str2num(answer{12,1});
            end
            
            if isempty(str2num(answer{13,1}))
                T0_mleka = 278;
            else T0_mleka = str2num(answer{13,1});
            end
            
            if isempty(str2num(answer{14,1}))
                ro_mleka = 1030;
            else ro_mleka = str2num(answer{14,1});
            end
            
            if isempty(str2num(answer{15,1}))
                h0_mleka = 0.04;
            else h0_mleka = str2num(answer{15,1});
            end
            
        h_kawy=h0_kawy + h0_mleka;
        
        m_kawy=ro_kawy*3.14*r*r*h0_kawy;
        m_mleka = ro_mleka*3.14*r*r*h0_mleka;
        
        ro_kawy = (ro_kawy*h0_kawy+ro_mleka*h0_mleka)/(h0_kawy+h0_mleka);
            
        A_s_zew =(2*h-h_kawy)*2*3.14*r;
        V_s=3.14*((r+g)*(r+g)-r*r)*h;
        A_s_wew = 2*3.14*r*h_kawy;
        A_p_kawa = 3.14*r*r;
        V_kawy=3.14*r*r*h_kawy;
        cp_s=800;
        cp_kawy = 4000;
        
        
        
        T0_kawy = (m_kawy*4200*T0_kawy+m_mleka*4050*T0_mleka)/(m_kawy*4200+m_mleka*4050);
        
 case 3
        
        Podaj_Tp = ('Podaj wartość temperatury panującej w pomieszczeniu w [K]');
        Podaj_alfa_p_s = ('Podaj wartość współczynnika wymiany ciepła powietrze - ściana kubka w [W/(m2*K)]');
        Podaj_r = ('Podaj wartość promienia kubka w [m]');
        Podaj_h =  ('Podaj wartość wysokości kubka w [m]');
        Podaj_g = ('Podaj wartość grubości ścianki w [m]');
        Podaj_ro_s = ('Podaj wartość gęstości materiału z jakiego wykonana jest ścianka kubka w [kg/m3]');
        Podaj_alfa_s_k = ('Podaj wartość współczynnika wymiany ciepła ścianka - kawa w [W/(m2*K)]');
        Podaj_T0_s = ('Podaj początkową wartość temperatury kubka w [K]');
        Podaj_h_kawy = ('Podaj wartość wysokości kawy z wrzątkiem w [m]');
        Podaj_alfa_p_kawa = ('Podaj wartość współczynnika wymiany ciepła powietrze - kawa w [W/(m2*K)]');
        Podaj_ro_kawy = ('Podaj wartość gęstości kawy w [kg/m3]');
        Podaj_T0_kawy = ('Podaj początkową wartość temperatury kawy w [K]');
        Podaj_T0_mleka = ('Podaj początkową wartość temperatury mleka w [K]');
        Podaj_ro_mleka = ('Podaj wartość gęstości mleka w [kg/m3]');
        Podaj_ho_mleka = ('Podaj wartość wysokości mleka w [m]');
        Podaj_Timeop = ('Po jakim czasie dolewasz kawę w [s]');
        
        answer=inputdlg({Podaj_Tp,Podaj_alfa_p_s,Podaj_r,Podaj_h,Podaj_g,Podaj_ro_s,Podaj_alfa_s_k,Podaj_T0_s,Podaj_h_kawy,Podaj_alfa_p_kawa,Podaj_ro_kawy,Podaj_T0_kawy,Podaj_T0_mleka,Podaj_ro_mleka,Podaj_ho_mleka,Podaj_Timeop});
        
       
            if isempty(str2num(answer{1,1}))
                Tp = 293;
            else Tp = str2num(answer(1,1));
            end

            if isempty(str2num(answer{2,1}))
                alfa_p_s = 10;
            else alfa_p_s = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                r = 0.04;
            else r = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                h = 0.09;
            else h = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                g = 0.002;
            else g = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                ro_s = 2400;
            else ro_s = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                alfa_s_kawa = 250;
            else alfa_s_kawa = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                T0_s = 293;
            else T0_s = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                h0_kawy = 0.05;
            else h0_kawy = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                alfa_p_kawa = 10;
            else alfa_p_kawa = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                ro_kawy = 1100;
            else ro_kawy = str2num(answer{11,1});
            end
            
            if isempty(str2num(answer{12,1}))
                T0_kawy = 360;
            else T0_kawy = str2num(answer{12,1});
            end
            
            if isempty(str2num(answer{13,1}))
                T0_mleka = 278;
            else T0_mleka = str2num(answer{13,1});
            end
            
            if isempty(str2num(answer{14,1}))
                ro_mleka = 1030;
            else ro_mleka = str2num(answer{14,1});
            end
            
            if isempty(str2num(answer{15,1}))
                h0_mleka = 0.04;
            else h0_mleka = str2num(answer{15,1});
            end
            
            if isempty(str2num(answer{16,1}))
                Timeop = 500;
            else Timeop = str2num(answer{16,1});
            end
            
        A_s_wew = 2*3.14*r*h0_kawy;
        A_s_zew =(2*h-h0_kawy)*2*3.14*r;
        V_kawy=3.14*r*r*h0_kawy;
        cp_kawy = 4000;
        
        h_kawy=h0_kawy + h0_mleka;
        
        
        m_kawy=ro_kawy*3.14*r*r*h0_kawy;
        m_mleka = ro_mleka*3.14*r*r*h0_mleka;
        
        ro_kawy_2 = (ro_kawy*h0_kawy+ro_mleka*h0_mleka)/(h0_kawy+h0_mleka);
            
        A_s_zew_2 = (2*h-h_kawy)*2*3.14*r;
        V_s=3.14*((r+g)*(r+g)-r*r)*h;
        A_s_wew_2 = 2*3.14*r*h_kawy;
        A_p_kawa = 3.14*r*r;
        V_kawy_2=3.14*r*r*h_kawy;
        cp_s=800;
        cp_kawy_2 = 4000;
       
         
end
        