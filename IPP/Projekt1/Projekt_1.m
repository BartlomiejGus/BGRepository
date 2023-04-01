clc;
clear;

tytul = ['  Projekt 1 - IPP,                                        '
         '  Wykonali:                                               '
         '  ŁJ                       '
         '  Bartłomiej Guś nr albumu 297415 gr.IPAUT-161            '
         '  Wybierz metodę:                                         '];

     
odpowiedz=[1,2];
wybor=menu(tytul,'Zadanie 1 - Qwe - wymuszenie skokowe','Zadanie 2 - Qwe - wymuszenie sinusoidalne');

switch odpowiedz(wybor)
    case 1
        typ_wymuszenia = 1;
        Podaj_Rz = ('Podaj wartość promienia zbiornika w [m]');
        Podaj_Rp = ('Podaj wartość promienia rury w [m]');
        Podaj_h0 = ('Podaj wartość wysokości początkowej cieczy w zbiorniku w [m]');
        Podaj_L =  ('Podaj wartość długości rury w [m]');
        Podaj_ro = ('Podaj wartość gęstości cieczy w [kg/m3]');
        Podaj_kf = ('Podaj wartość współczynnika oporu w [kg/m2]');
        
        Rp = 0;
        h0 = -1;
        f = 0;
        g = 9.81;
        Qwe = 0.1;
        
        while(2*Rp>h0)
        
        answer=inputdlg({Podaj_Rz,Podaj_Rp,Podaj_h0,Podaj_L,Podaj_ro,Podaj_kf});
        
       
            if isempty(str2num(answer{1,1}))
                Rz = 1;
            else Rz = str2num(answer(1,1));
            end

            if isempty(str2num(answer{2,1}))
                Rp = 0.05;
            else Rp = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                h0 = 0.2;
            else h0 = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                L = 1;
            else L = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                ro = 1000;
            else ro = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                kf = 0.5;
            else kf = str2num(answer{6,1});
            end
            
        end
        
        Az = 3.14*Rz*Rz;
        Ap = 3.14*Rp*Rp;
        
    case 2
        
        typ_wymuszenia = 2;
        Podaj_Rz = ('Podaj wartość promienia zbiornika w [m]');
        Podaj_Rp = ('Podaj wartość promienia rury w [m]');
        Podaj_h0 = ('Podaj wartość wysokości początkowej cieczy w zbiorniku w [m]');
        Podaj_L =  ('Podaj wartość długości rury w [m]');
        Podaj_ro = ('Podaj wartość gęstości cieczy w [kg/m3]');
        Podaj_kf = ('Podaj wartość współczynnika oporu w [kg/m2]');
        Podaj_Qwe =('Podaj wartość natężenia przepływu cieczy wejściowe w [m3/s]');
        Podaj_f =('Podaj wartość częstotliwości zmian przepływu cieczy wejściowe w [Hz]');
        
        Rp = 0;
        h0 = -1;
        g = 9.81;
       
        while(2*Rp>h0)
        
        answer=inputdlg({Podaj_Rz,Podaj_Rp,Podaj_h0,Podaj_L,Podaj_ro,Podaj_kf,Podaj_Qwe,Podaj_f});
        
       
            if isempty(str2num(answer{1,1}))
                Rz = 1;
            else Rz = str2num(answer(1,1));
            end

            if isempty(str2num(answer{2,1}))
                Rp = 0.04;
            else Rp = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                h0 = 0.2;
            else h0 = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                L = 1;
            else L = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                ro = 1000;
            else ro = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                kf = 0.5;
            else kf = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                Qwe = 0.1;
            else Qwe = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                f = 0.1;
            else f = str2num(answer{8,1});
            end
        end
        
        Az = 3.14*Rz*Rz;
        Ap = 3.14*Rp*Rp;
         
end
        