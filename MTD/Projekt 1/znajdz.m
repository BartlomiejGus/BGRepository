function index = znajdz(podzbiory,szukany_podzbior)

index = 0;
wielkosc_podzbiory = size(podzbiory,1);

for i = 1:wielkosc_podzbiory
    
    badany_podzbior = podzbiory(i,1);
    badany_podzbior = cell2mat(badany_podzbior);
    czy_to_ten = isequal(badany_podzbior,szukany_podzbior);
    
    if czy_to_ten == 1
        index = i;
        return
    end

end


