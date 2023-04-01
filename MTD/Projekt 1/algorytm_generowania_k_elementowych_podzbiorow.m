function podzbiory_k_elementowe = algorytm_generowania_k_elementowych_podzbiorow(n,k)

podzbiory_k_elementowe = {};

podzbiory_k_elementowe(1,1) = {[1:k]};
zbior_liczb = 1:n;

iterator = 1;

while 1
    
    badany_podzbior = podzbiory_k_elementowe(iterator,1);
    badany_podzbior = cell2mat(badany_podzbior);
    znaleziony_index = 0;
    
    for i = 1:k
        
        index = find(badany_podzbior==(badany_podzbior(1,i)+1));
        
        czy_istnieje_taki_element = isempty(index);
        
        if czy_istnieje_taki_element == 1
            znaleziony_index = i;
            break
        end
    end
    
    if badany_podzbior(1,znaleziony_index)==zbior_liczb(end)
       return
    elseif badany_podzbior(1,znaleziony_index)<zbior_liczb(end)
        badany_podzbior(1,znaleziony_index) = badany_podzbior(1,znaleziony_index) + 1;
        badany_podzbior(1,1:znaleziony_index-1) = (1:znaleziony_index-1);
    end
     
    podzbiory_k_elementowe(iterator+1,1) = {badany_podzbior};
    
    iterator = iterator + 1;
end


end

