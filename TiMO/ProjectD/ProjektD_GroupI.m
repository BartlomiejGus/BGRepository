%ProjectD - Group(1): Dynamic Programming
%Made by: WD, PW, MN, MM, Bartłomiej Guś

clear all,clc;

load('dynamicProgramming.mat');

target = input('Give me the level of energy demand: ');

actualArray.EnergyUsed = 0:50:target;
actualArray.EnergyLeft = 0:50:target;

actualArray.OptimalValue = zeros(size(actualArray.EnergyUsed,2),1)';
actualArray.OptimalOption = zeros(size(actualArray.EnergyUsed,2),1)';
actualArray.Array = zeros(size(actualArray.EnergyUsed,2));

bigArray = {};

for i = size(dynamicProgramming.NOx,2):-1:1
    
    [newActualArray] = returnNewActualArray(actualArray,dynamicProgramming,i);
    
    bigArray{end+1} = newActualArray;
    
    actualArray = newActualArray;
    
end

answerDynamicProgramming(target,dynamicProgramming,bigArray);