function [pMin, indexMin,pMax,indexMax,pG] = Function_get_min_max_and_pG(points)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
rozmiar = size(points,1);
liczbaArgumentow = size(points{1},2);
wyniki = [];
punkt = {};

for i=1:rozmiar
    for j = 1:liczbaArgumentow
        punkt{size(punkt,2)+1} = points{i}(1,j);  
    end
    wyniki = [wyniki Function_to_optimize_ProjectB_Group1(punkt,liczbaArgumentow)];
    punkt = {};
end

wynikMax = max(wyniki);
indexMax = find(wyniki==wynikMax);
wynikMin = min(wyniki);
indexMin = find(wyniki==wynikMin);
pMin = points{indexMin};
pMax = points{indexMax};
pointsNoMax = points;

for i=1:size(pointsNoMax,1)
   if pointsNoMax{i} == pMax
       pointsNoMax{i} = [];
       break;
   end
end

suma=0;
partsOfpG=[];
for j=1:liczbaArgumentow
    for i=1:size(pointsNoMax,1)
        if ~isempty(pointsNoMax{i})
            suma = suma+pointsNoMax{i}(1,j);
        end
    end
    partsOfpG = [partsOfpG suma/(size(pointsNoMax,1)-1)];
    suma=0;
end
pG = partsOfpG;
end

