function f_x = Function_to_optimize_ProjectB_Group1(x,which_function)
%Below choosen functions to optimize

switch which_function
    case 1
        %First function - one variable
        f_x = (cell2mat(x(1,1))).^2 + 1;
    case 2
        %Second Function - two variables "Himmelblau"
        f_x = ((cell2mat(x(1,1))).^2 + cell2mat(x(1,2)) - 11).^2 + ...
            (cell2mat(x(1,1)) + (cell2mat(x(1,2))).^2 - 7).^2 ; 
    case 3
        %Third function - three variables
        f_x = cell2mat(x(1,1)).^4 - ...
            3.*cell2mat(x(1,1)).^2.*cell2mat(x(1,2)).^2 + ...
            23.*(cell2mat(x(1,1)).^3 + 3.*cell2mat(x(1,2))).^2. -2 ; 
        
end

end
