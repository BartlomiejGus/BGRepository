function [kolejne_kroki_kolejki,zbior_E,zbior_E_kolejne_kroki] = algorytm_przeszukiwania_grafu_wszerz(wierzcholek_poczatkowy,polaczenia)

kolejka = [wierzcholek_poczatkowy];

odwiedzone_wierzcholki = [wierzcholek_poczatkowy];

kolejne_kroki_kolejki = {kolejka};
zbior_E = [];

zbior_E_kolejne_kroki = {{}};

numer_iteracji = 1;

disp(['Iteracja: ', num2str(numer_iteracji)]);
disp('Kolejka w obecnej iteracji:');
disp(kolejka);
disp('Zbior E:');
disp(zbior_E);
disp(' ');

while isempty(kolejka) == 0
    
    aktualnie_rozpatrywany_wierzcholek = kolejka(1,1);
    
    kolejne_wierzcholki_do_odwiedzenia = sprawdz_czy_istnieje_nastepny_do_odwiedzenia_kolejka...
    (aktualnie_rozpatrywany_wierzcholek,polaczenia,odwiedzone_wierzcholki);

    czy_istnieje_kolejny_wierzcholek_do_odwiedzenia = isempty(kolejne_wierzcholki_do_odwiedzenia);
    
    if czy_istnieje_kolejny_wierzcholek_do_odwiedzenia == 0
        
        odwiedzone_wierzcholki = [odwiedzone_wierzcholki;kolejne_wierzcholki_do_odwiedzenia];
        
        obecne_E = [];
        
        for i = 1:size(kolejne_wierzcholki_do_odwiedzenia,1)
        
            obecne_E_do_dodania = [kolejka(1,1),kolejne_wierzcholki_do_odwiedzenia(i,1)];
            obecne_E = [obecne_E;obecne_E_do_dodania];
      
        end
        
        zbior_E = [zbior_E; obecne_E];
        
        kolejka = [kolejka;kolejne_wierzcholki_do_odwiedzenia];
        kolejne_kroki_kolejki{end+1,1} = kolejka;
        
    else
        
        kolejka = kolejka(2:end);
        kolejne_kroki_kolejki{end+1,1} = kolejka;
        
    end
    
    numer_iteracji = numer_iteracji + 1;
    
    zbior_E_kolejne_kroki{end+1,1} = zbior_E;
     
    disp(['Iteracja: ', num2str(numer_iteracji)]);
    disp('Kolejka w obecnej iteracji:');
    disp(kolejka);
    disp('Zbior E:');
    disp(zbior_E);
    disp(' ');
    
    
end


end

