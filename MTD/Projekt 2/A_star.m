clear;
clc;

plik_wejsciowy = "1";
sciezka = plik_wejsciowy+".mat";
load(sciezka);

rozpatrywane = [Dane.p_start];
przyszedlZ = [];
% droga od startu do aktualnego wierzcholka
g = [];
% f = g + h //h - heurystyka
f = [];

if Dane.p_start == Dane.p_meta
    msgbox('Wybrany punkt startowy jest punktem końcowym!');
    return
end

for i=1:size(Dane.wierzcholki,1)
    przyszedlZ(i)=0;
    g(i) = inf;
    f(i) = inf;
end

g(Dane.p_start) = 0;
f(Dane.p_start) = getDistance(Dane.wierzcholki{Dane.p_start},Dane.wierzcholki{Dane.p_meta});

while size(rozpatrywane,1)~=0
    tmp = inf;
    f_rozp = f(rozpatrywane);
    minF = min(f_rozp);
    indexMin = find(f==minF);
    for i=1:size(indexMin,2)
       if ~isempty(find(rozpatrywane==indexMin(i)))
           x = indexMin(i);
       end
    end
    if x==Dane.p_meta
        
       [sciezka, sciezka_do_napisu, kosztDrogi] = zrekonstruujTrase(przyszedlZ,Dane.p_meta,Dane.p_start,Dane.macierz_sasiedztwa);
       narysujWyniki(Dane,sciezka,sciezka_do_napisu, kosztDrogi);
       break;
    end
    rozpatrywane(rozpatrywane==x) = [];
    for i=1:size(Dane.macierz_sasiedztwa,2)
       if Dane.macierz_sasiedztwa(x,i)~=0
          tym_g = g(x) + Dane.macierz_sasiedztwa(x,i);
          if tym_g < g(i)
             przyszedlZ(i) = x;
             g(i) = tym_g;
             f(i) = g(i) + getDistance(Dane.wierzcholki{i},Dane.wierzcholki{Dane.p_meta});
             if isempty(rozpatrywane)
                czyYrozpatrywane = false;
             else
                czyYrozpatrywane = rozpatrywane==i;
             end
             if ~czyYrozpatrywane
                rozpatrywane = [rozpatrywane;i]; 
             end
          end
       end
    end
end