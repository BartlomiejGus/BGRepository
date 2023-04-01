function [kolejne_kroki_stosu,zbior_E,zbior_E_kolejne_kroki] = algorytm_przeszukiwania_grafu_w_glab(wierzcholek_poczatkowy,polaczenia)

stos = [wierzcholek_poczatkowy];

odwiedzone_wierzcholki = [wierzcholek_poczatkowy];

kolejne_kroki_stosu = {stos};
zbior_E = [];
zbior_E_kolejne_kroki = {{}};

numer_iteracji = 1;

disp(['Iteracja: ', num2str(numer_iteracji)]);
disp('Stos w obecnej iteracji:');
disp(stos);
disp('Zbior E:');
disp(zbior_E);
disp(' ');

while isempty(stos) == 0
    
    aktualnie_rozpatrywany_wierzcholek = stos(1,1);
    
    kolejny_wierzcholek_do_odwiedzenia = sprawdz_czy_istnieje_nastepny_do_odwiedzenia_stos...
    (aktualnie_rozpatrywany_wierzcholek,polaczenia,odwiedzone_wierzcholki);

    czy_istnieje_kolejny_wierzcholek_do_odwiedzenia = isempty(kolejny_wierzcholek_do_odwiedzenia);
    
    if czy_istnieje_kolejny_wierzcholek_do_odwiedzenia == 0
        
        odwiedzone_wierzcholki = [odwiedzone_wierzcholki;kolejny_wierzcholek_do_odwiedzenia];
        obecne_E = [stos(1,1),kolejny_wierzcholek_do_odwiedzenia];
        
        zbior_E = [zbior_E; obecne_E];
        
        stos = [kolejny_wierzcholek_do_odwiedzenia;stos];
        
        kolejne_kroki_stosu{end+1,1} = stos;
        
    else
        
        stos = stos(2:end);
        kolejne_kroki_stosu{end+1,1} = stos;
        
    end
    
    numer_iteracji = numer_iteracji + 1;
    
    zbior_E_kolejne_kroki{end+1,1} = zbior_E;

    disp(['Iteracja: ', num2str(numer_iteracji)]);
    disp('Stos w obecnej iteracji:');
    disp(stos);
    disp('Zbior E:');
    disp(zbior_E);
    disp(' ');
    
end

end

