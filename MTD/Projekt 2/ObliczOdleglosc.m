Wartosci = Dane.wierzcholki;

Macierz = zeros(size(Wartosci,1));

for i = 1:size(Wartosci,1)
    
    for j = 1:size(Wartosci,1)
        
        Macierz(i,j) = round(getDistance(Wartosci{i},Wartosci{j}),2);
        
    end
    
end