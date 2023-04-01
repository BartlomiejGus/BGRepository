clc;
clear;

tytul = ['  Projekt 5 - IPP,                                        '
         '  Wykonali:                                               '
         '  ŁJ                       '
         '  Bartłomiej Guś nr albumu 297415 gr.IPAUT-161            '
         '  Wybierz metodę:                                         '];

        Podaj_alfa_1 = ('Podaj wartość współczynnika alfa_1 w [1/min]');
        Podaj_alfa_2 = ('Podaj wartość współczynnika alfa_2 w [1/min]');
        Podaj_beta_1 = ('Podaj wartość współczynnika beta_1 w [1/min]');
        Podaj_beta_2 = ('Podaj wartość współczynnika beta_2 w [1/min]');
        Podaj_lambda_1 = ('Podaj wartość współczynnika lambda_1 w [Btu/lb mol]');
        Podaj_lambda_2 = ('Podaj wartość współczynnika lambda_2 w [Btu/lb*mol]');

        Podaj_c_p = ('Podaj wartość ciepła właściwego c_p w [Btu/lbm F]');
        Podaj_ro = ('Podaj wartość gęstości ro w [lbm/ft3]');
        Podaj_V = ('Podaj wartość objętość V w [ft3]');
        Podaj_h_i = ('Podaj wartość współczynnika wymiany ciepła h_i w [Btu/h F ft2]');
        Podaj_A_i = ('Podaj wartość pola powierzchni A_i w [ft2]');
        
        Podaj_c_m = ('Podaj wartość ciepła właściwego c_m w [Btu/lbm F]');
        Podaj_ro_m = ('Podaj wartość gęstości ro_m w [lbm/ft3]');
        Podaj_V_m = ('Podaj wartość objętość V_m w [ft3]');
        Podaj_h_os = ('Podaj wartość współczynnika wymiany ciepła h_os w [Btu/h F ft2]');
        Podaj_A_os = ('Podaj wartość pola powierzchni A_os w [ft2]');
        
        answer=inputdlg({Podaj_alfa_1,Podaj_alfa_2,Podaj_beta_1,Podaj_beta_2,Podaj_lambda_1,Podaj_lambda_2,Podaj_c_p,Podaj_ro,Podaj_V,Podaj_h_i,Podaj_A_i,Podaj_c_m,Podaj_ro_m,Podaj_V_m,Podaj_h_os,Podaj_A_os});
        
       
            if isempty(str2num(answer{1,1}))
                alfa_1 = 729.55;
            else alfa_1 = str2num(answer{1,1});
            end

            if isempty(str2num(answer{2,1}))
                alfa_2 = 6567.6;
            else alfa_2 = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                beta_1 = -15000;
            else beta_1 = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                beta_2 = -20000;
            else beta_2 = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                lambda_1 = -40000;
            else lambda_1 = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                lambda_2 = -50000;
            else lambda_2 = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                c_p = 1;
            else c_p = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                ro = 50;
            else ro = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                V = 42.5;
            else V = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                h_i = 160/60;
            else h_i = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                A_i = 56.5;
            else A_i = str2num(answer{11,1});
            end
            
            if isempty(str2num(answer{12,1}))
                c_m = 0.12;
            else c_m = str2num(answer{12,1});
            end
            
            if isempty(str2num(answer{13,1}))
                ro_m = 512;
            else ro_m = str2num(answer{13,1});
            end
            
            if isempty(str2num(answer{14,1}))
                V_m = 9.42;
            else V_m = str2num(answer{14,1});
            end
            
            if isempty(str2num(answer{15,1}))
                h_os = 1000/60;
            else h_os = str2num(answer{15,1});
            end
            
            if isempty(str2num(answer{16,1}))
                A_os = 56.5;
            else A_os = str2num(answer{16,1});
            end
            
            Tj = 212;
            T_m0 = 80;
            T_0 = 80;
          
        
        
   