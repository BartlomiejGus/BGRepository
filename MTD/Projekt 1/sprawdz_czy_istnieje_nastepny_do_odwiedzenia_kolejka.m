function kolejne_wierzcholki_do_odwiedzenia = sprawdz_czy_istnieje_nastepny_do_odwiedzenia_kolejka...
    (aktualnie_rozpatrywany_wierzcholek,polaczenia,odwiedzone_wierzcholki)

kolejne_wierzcholki_do_odwiedzenia = [];

for i = 1:size(polaczenia,1)
   
    badane_polaczenie = polaczenia{i,1};
    badane_polaczenie_wierzcholek = badane_polaczenie{1,1};
    badane_polaczenie_wektor_polaczen = badane_polaczenie{1,2};
    
    if badane_polaczenie_wierzcholek == aktualnie_rozpatrywany_wierzcholek
        
        for j = 1:size(badane_polaczenie_wektor_polaczen,2)
            
            czy_byl_juz_odwiedzany = isempty(find(odwiedzone_wierzcholki==badane_polaczenie_wektor_polaczen(1,j)));
            
            if czy_byl_juz_odwiedzany == 1
                
                kolejne_wierzcholki_do_odwiedzenia = [kolejne_wierzcholki_do_odwiedzenia;badane_polaczenie_wektor_polaczen(1,j)];
                
            end
            
        end
        
    end
    
end


end

