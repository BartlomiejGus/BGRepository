function podzbiory_zbioru = algorytm_generowania_podzbiorow(n)

podzbiory_zbioru = {};

podzbiory_zbioru(1,1) = {[]};

iterator = 1;

zbior_liczb = 1:n;
zbior_liczb_pom = zbior_liczb;
czy_to_koniec = 1;

while 1
    
    for i = 1:n
        
      maximum = max(zbior_liczb_pom);
      badany_podzbior = podzbiory_zbioru(iterator,1);
      badany_podzbior = cell2mat(badany_podzbior);
      index = find(badany_podzbior==maximum);
      
      czy_istnieje_taki_element = isempty(index);
      
      if czy_istnieje_taki_element == 1
          czy_to_koniec = 0;
          nastepny_podzbior = [badany_podzbior,maximum];
          nastepny_podzbior(nastepny_podzbior>maximum)=[];
          
          podzbiory_zbioru(iterator+1,1) = {nastepny_podzbior};
          break
      end
      
      zbior_liczb_pom(zbior_liczb_pom==maximum) = [];
    end
    
    if czy_to_koniec == 1
        return
    end
    
    zbior_liczb_pom = zbior_liczb;
    czy_to_koniec = 1;
    iterator = iterator + 1;
    
end

end

