function permutacje_zbioru = algorytm_generowania_permutacji_zbioru(n)

permutacje_zbioru = {};
permutacje_zbioru(1,1) = {[1:n]};
iterator = 1;

while 1
    
    badany_podzbior = permutacje_zbioru(iterator,1);
    badany_podzbior = cell2mat(badany_podzbior);
    znaleziony_index = 0;
    
    for i = n:-1:2
        
        if badany_podzbior(i-1) <  badany_podzbior(i)
            znaleziony_index = i-1;
            break
        end
       
    end
    
    if znaleziony_index == 0
        return
    else
        a_j = badany_podzbior(1,znaleziony_index);
        zbior_pom = badany_podzbior(1,(znaleziony_index+1):size(badany_podzbior,2));
        zbior_pom = zbior_pom(zbior_pom>a_j);
        najmniejsza_wartosc_zbior_pom = min(zbior_pom);
        indeks_najmniejszej_wartosci_zbior_pom = find(badany_podzbior==najmniejsza_wartosc_zbior_pom);
        
        for i = 1:size(indeks_najmniejszej_wartosci_zbior_pom,2)
            
            if indeks_najmniejszej_wartosci_zbior_pom(i) > znaleziony_index
                badany_podzbior(1,znaleziony_index) = najmniejsza_wartosc_zbior_pom;
                badany_podzbior(1,indeks_najmniejszej_wartosci_zbior_pom) = a_j;
                wartosci_od_ajplusjeden_do_an = badany_podzbior(1,(znaleziony_index+1):size(badany_podzbior,2));
                wartosci_od_ajplusjeden_do_an_flip = flip(wartosci_od_ajplusjeden_do_an);
                badany_podzbior(1,(znaleziony_index+1):size(badany_podzbior,2)) = wartosci_od_ajplusjeden_do_an_flip;
                break;
            end
            
        end
        
    end
    
    permutacje_zbioru(iterator+1,1) = {badany_podzbior};
    
    iterator = iterator + 1;
end

end

