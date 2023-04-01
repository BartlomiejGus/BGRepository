function [sciezka_do_rysunku,sciezka,kosztDrogi] = zrekonstruujTrase(przyszedlZ,p_meta,p_start,macierz_sasiedztwa)
kosztDrogi = 0;
odwroconaSciezka=[p_meta];
index = p_meta;
while przyszedlZ(index)~=p_start
    kosztDrogi = kosztDrogi + macierz_sasiedztwa(przyszedlZ(index),odwroconaSciezka(end));
    odwroconaSciezka=[odwroconaSciezka przyszedlZ(index)];
    index = przyszedlZ(index);
end
kosztDrogi = kosztDrogi + macierz_sasiedztwa(p_start,odwroconaSciezka(end));
odwroconaSciezka = [odwroconaSciezka p_start];
sciezka = flip(odwroconaSciezka);
sciezka_do_rysunku = {};
for i=1:(size(sciezka,2)-1)
    if isempty(sciezka_do_rysunku)
        sciezka_do_rysunku = {[sciezka(i) sciezka(i+1)]};
    else
        sciezka_do_rysunku{end+1,1} = [sciezka(i) sciezka(i+1)];
    end
end
disp("Znaleziona  trasa przez algorytm to: "+num2str(sciezka));