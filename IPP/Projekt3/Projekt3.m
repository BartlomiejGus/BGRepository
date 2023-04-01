clc;
clear;

tytul = ['  Projekt 3 - IPP,                                        '
         '  Wykonali:                                               '
         '  ŁJ                       '
         '  Bartłomiej Guś nr albumu 297415 gr.IPAUT-161            '
         '  Wybierz metodę:                                         '];

     
odpowiedz=[1,2];
wybor=menu(tytul,'Zadanie 1 - wymiennik ciepła przeciwprądowy','Zadanie 2 - wymiennik ciepła współprądowy');

switch odpowiedz(wybor)
    case 1
        
        Podaj_T0a = ('Podaj wartość początkową temperatury panującej w przepływie A w [K]');
        Podaj_T0b = ('Podaj wartość początkową temperatury panującej w przepływie B w [K]');
        Podaj_ro_a = ('Podaj wartość gęstości płynu w przepływie A w [kg/m3]');
        Podaj_ro_b = ('Podaj wartość gęstości płynu w przepływie B w [kg/m3]');
        Podaj_Q_a = ('Podaj wartość natężenia przepływu w przepływie A w [m3/s]');
        Podaj_Q_b = ('Podaj wartość natężenia przepływu w przepływie B w [m3/s]');
        Podaj_cw_a = ('Podaj wartość ciepła właściwego płynu w przepływie A w [m2/(s2*K)]');
        Podaj_cw_b = ('Podaj wartość ciepła właściwego płynu w przepływie A w [m2/(s2*K)]');
        Podaj_alfa= ('Podaj wartość współczynnika wymiany ciepła wymmiennika w [W/(m2*K)]');
        Podaj_S= ('Podaj wartość pola powierzchni wymiany ciepła w [m2]');
        Podaj_N= ('Podaj wartość ilości iteracji w [bezwymiarowe]');
        
        
        answer=inputdlg({Podaj_T0a,Podaj_T0b,Podaj_ro_a,Podaj_ro_b,Podaj_Q_a,Podaj_Q_b,Podaj_cw_a,Podaj_cw_b,Podaj_alfa,Podaj_S,Podaj_N});
        
       
            if isempty(str2num(answer{1,1}))
                T0_a = 363;
            else T0_a = str2num(answer{1,1});
            end

            if isempty(str2num(answer{2,1}))
                T0_b = 283;
            else T0_b = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                ro_a = 1000;
            else ro_a = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                ro_b = 1000;
            else ro_b = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                Q_a = 0.002;
            else Q_a = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                Q_b = 0.002;
            else Q_b = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                cw_a = 4000;
            else cw_a = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                cw_b = 4200;
            else cw_b = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                alfa = 100;
            else alfa = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                S = 0.01;
            else S = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                N = 7;
            else N = str2num(answer{11,1});
            end
          
            a = ro_a*cw_a*Q_a;
            b = ro_b*cw_b*Q_b;
            p = alfa*S;
            
            %Uwaga nadpisanie wartości a, b i p takie jak na wykładzie
            
            a = 132;
            b = 250;
            p = 18;
            
            T=zeros(1,N);
            t=zeros(1,N);
            
            T(1) = T0_a; 
            t(N) = 343;
            t1 = T0_b;
            
            while(abs(t1-t(1))>=0.01 )
                
                for w = 2:1:N 
                    T(w) = (a*T(w-1)+p*t(N-w+2))/(a+p);
                    t(N-w+1) = (t(N-w+2)*(b+p)-p*T(w))/b;
                end 
                
                if t(1)<t1
                    t(N)=t(N)+0.001;
                end
                
                if t(1)>t1
                    t(N)=t(N)-0.001;
                end 
                
            end
           
            t2=zeros(1,N);
            
            for w=1:1:N
                t2(w)=t(N-w+1);
            end
            
            %Deklaracja dla aktualnego 
            a = 132;
            b = 250;
            p = 9;
            
            TA=zeros(1,N);
            tA=zeros(1,N);
            
            TA(1) = T0_a; 
            tA(N) = 343;
            t1 = T0_b;
            
            while(abs(t1-tA(1))>=0.01 )
                
                for w = 2:1:N 
                    TA(w) = (a*TA(w-1)+p*tA(N-w+2))/(a+p);
                    tA(N-w+1) = (tA(N-w+2)*(b+p)-p*TA(w))/b;
                end 
                
                if tA(1)<t1
                    tA(N)=tA(N)+0.001;
                end
                
                if tA(1)>t1
                    tA(N)=tA(N)-0.001;
                end 
            end
            
            t2A=zeros(1,N);
            
            for w=1:1:N
                t2A(w)=tA(N-w+1);
            end
    
            % Deklaracaj osi X
            X = 0:1:N-1;
            
            plot(X,T,'k',X,t,'b','LineWidth',0.1);
            hold on
            plot(X,TA,'k',X,tA,'b','LineWidth',1.5);
            hold off
            xlabel('N [-]');
            ylabel('T[K], t[K]');
            legend('przepływ A - bazowy','przepływ B - bazowy','przepływ A - aktualny','przepływ B - aktualny')
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys])
            
            title('Wykres dla warunków: a = 132 [W/K], b = 250 [W/K], p = 18 [W/K]');
            
        
        
    case 2
        
        Podaj_T0a = ('Podaj wartość początkową temperatury panującej w przepływie A w [K]');
        Podaj_T0b = ('Podaj wartość początkową temperatury panującej w przepływie B w [K]');
        Podaj_ro_a = ('Podaj wartość gęstości płynu w przepływie A w [kg/m3]');
        Podaj_ro_b = ('Podaj wartość gęstości płynu w przepływie B w [kg/m3]');
        Podaj_Q_a = ('Podaj wartość natężenia przepływu w przepływie A w [m3/s]');
        Podaj_Q_b = ('Podaj wartość natężenia przepływu w przepływie B w [m3/s]');
        Podaj_cw_a = ('Podaj wartość ciepła właściwego płynu w przepływie A w [m2/(s2*K)]');
        Podaj_cw_b = ('Podaj wartość ciepła właściwego płynu w przepływie A w [m2/(s2*K)]');
        Podaj_alfa= ('Podaj wartość współczynnika wymiany ciepła wymmiennika w [W/(m2*K)]');
        Podaj_S= ('Podaj wartość pola powierzchni wymiany ciepła w [m2]');
        Podaj_N= ('Podaj wartość ilości iteracji w [bezwymiarowe]');
        
        
        answer=inputdlg({Podaj_T0a,Podaj_T0b,Podaj_ro_a,Podaj_ro_b,Podaj_Q_a,Podaj_Q_b,Podaj_cw_a,Podaj_cw_b,Podaj_alfa,Podaj_S,Podaj_N});
        
       
            if isempty(str2num(answer{1,1}))
                T0_a = 363;
            else T0_a = str2num(answer{1,1});
            end

            if isempty(str2num(answer{2,1}))
                T0_b = 283;
            else T0_b = str2num(answer{2,1});
            end

            if isempty(str2num(answer{3,1}))
                ro_a = 1000;
            else ro_a = str2num(answer{3,1});
            end

            if isempty(str2num(answer{4,1}))
                ro_b = 1000;
            else ro_b = str2num(answer{4,1});
            end

            if isempty(str2num(answer{5,1}))
                Q_a = 0.002;
            else Q_a = str2num(answer{5,1});
            end

            if isempty(str2num(answer{6,1}))
                Q_b = 0.002;
            else Q_b = str2num(answer{6,1});
            end

            if isempty(str2num(answer{7,1}))
                cw_a = 4000;
            else cw_a = str2num(answer{7,1});
            end
            
            if isempty(str2num(answer{8,1}))
                cw_b = 4200;
            else cw_b = str2num(answer{8,1});
            end
            
            if isempty(str2num(answer{9,1}))
                alfa = 100;
            else alfa = str2num(answer{9,1});
            end
            
            if isempty(str2num(answer{10,1}))
                S = 0.01;
            else S = str2num(answer{10,1});
            end
            
            if isempty(str2num(answer{11,1}))
                N = 7;
            else N = str2num(answer{11,1});
            end
          
            a = ro_a*cw_a*Q_a;
            b = ro_b*cw_b*Q_b;
            p = alfa*S;
            
            a = 132;
            b = 250;
            p = 18;
            
            T=zeros(1,N);
            t=zeros(1,N);
            
            T(1) = T0_a; 
            t(N) = 343;
            t1 = T0_b;
            
            while(abs(t1-t(1))>=0.01 )
                
                for w = 2:1:N 
                    T(w) = (a*T(w-1)+p*t(N-w+2))/(a+p);
                    t(N-w+1) = (t(N-w+2)*(b+p)-p*T(w))/b;
                end 
                
                if t(1)<t1
                    t(N)=t(N)+0.001;
                end
                
                if t(1)>t1
                    t(N)=t(N)-0.001;
                end 
            end
            
            t2=zeros(1,N);
            
            for w=1:1:N
                t2(w)=t(N-w+1);
            end
            
            %Dla współprądowego
            
            a = 132;
            b = 250;
            p = 18;
            
            TA=zeros(1,N);
            tA=zeros(1,N);
            
            TA(1) = T0_a; 
            tA(1) = T0_b;
            
          
            for w = 2:1:N 
                tA(w) = (1/(b-p*p/(a+p)+p))*(b*tA(w-1)+ p*a*(1/(a+p))*TA(w-1));
                TA(w) = (a*TA(w-1)+p*tA(w))/(a+p);                
            end 
              
            % Deklaracaj osi X
            X = 0:1:N-1;
            
            plot(X,T,'k',X,t,'b','LineWidth',0.1);
            hold on
            plot(X,TA,'k',X,tA,'b','LineWidth',1.5);
            hold off
            xlabel('N [-]');
            ylabel('T[K], t[K]');
            legend('przepływ A - bazowy','przepływ B - bazowy','przepływ A - aktualny','przepływ B - aktualny')
            grid;
            
            x0 = 100;
            y0 = 200;
            szer = 1000;
            wys = 500;
            set(gcf,'position',[x0,y0,szer,wys])
            
            title('Wykres dla warunków: a = 132 [W/K], b = 250 [W/K], p = 18 [W/K]');
end
        