function answerDynamicProgramming(target,dynamicProgramming,bigArray)

disp("Minimum emission of Nox: " + num2str(bigArray{1,10}.OptimalValue(1,end)));

disp(" ");

leftEnergy = target - (bigArray{1,10}.OptimalOption(1,end)-1)*50;
nextEnergy = leftEnergy/50 + 1;

disp('Optimal choice of power plants: ');
disp("Power plant " + num2str(1) + " power: " + num2str((bigArray{1,10}.OptimalOption(1,end)-1)*50)+" ,emission: " + num2str(dynamicProgramming.NOx(bigArray{1,10}.OptimalOption(1,end),1)));

tempValue = 2;

for i=(size(dynamicProgramming.NOx,2)-1):-1:1
    
    disp("Power plant " + num2str(tempValue) + " power: " + num2str((bigArray{1,i}.OptimalOption(1,nextEnergy)-1)*50)+" ,emission: " + num2str(dynamicProgramming.NOx(bigArray{1,i}.OptimalOption(1,nextEnergy),tempValue)));
    
    tempValue = tempValue + 1;
    
    leftEnergy = leftEnergy - (bigArray{1,i}.OptimalOption(1,nextEnergy)-1)*50;
    nextEnergy = leftEnergy/50 + 1;
    
end

end

