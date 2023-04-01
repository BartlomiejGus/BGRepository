function [newActualArray] = returnNewActualArray(actualArray,dynamicProgramming,whichColumn)

%whichColumn = which power plant

newActualArray.EnergyUsed = actualArray.EnergyUsed;
newActualArray.EnergyLeft = actualArray.EnergyLeft;

newActualArray.OptimalValue = zeros(size(newActualArray.EnergyUsed,2),1)';
newActualArray.OptimalOption = zeros(size(newActualArray.EnergyUsed,2),1)';
newActualArray.Array = zeros(size(newActualArray.EnergyUsed,2)) +Inf;

for i = 1:size(actualArray.EnergyUsed,2)
   
    for j = 1:size(actualArray.EnergyLeft,2)
           
        if i == j &&  whichColumn == size(dynamicProgramming.NOx,2) && i + j <= size(dynamicProgramming.NOx,1)
            
           newActualArray.Array(i,j) =  dynamicProgramming.NOx(i,whichColumn);
           
        elseif whichColumn ~= size(dynamicProgramming.NOx,2) && i <= size(dynamicProgramming.NOx,1) && j-i+1 >0
           
           newActualArray.Array(i,j) = actualArray.OptimalValue(1,j-i+1) + dynamicProgramming.NOx(i,whichColumn);
            
        else
            
           newActualArray.Array(i,j) = Inf;
           
        end
        
    end
    
end

%Fill the Optimal 

for i = 1:size(newActualArray.Array,2)
    
    tempArray = newActualArray.Array(:,i);
    
    [minValue,minIndex] = min(tempArray);
    
    newActualArray.OptimalValue(1,i) = minValue(1);
    
    newActualArray.OptimalOption(1,i) = minIndex(1);
    
end


end

