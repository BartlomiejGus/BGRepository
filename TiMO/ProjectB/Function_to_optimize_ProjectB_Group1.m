function f_x = Function_to_optimize_ProjectB_Group1(x,which_function)
%Below choosen functions to optimize

switch which_function
    case 1
        %First function - one variable
        f_x = 2.*cos(0.4.*(cell2mat(x(1,1)))) - 2.*sin(1.5.*(cell2mat(x(1,1)))) + 40;
    case 2
        %Second Function - two variables "Himmelblau"
        f_x = ((cell2mat(x(1,1))).^2 + cell2mat(x(1,2)) - 11).^2 + ...
            (cell2mat(x(1,1)) + (cell2mat(x(1,2))).^2 - 7).^2 ; 
    case 3
        %Third function - three variables
        %f(x,y,z) =x.^2+ y^2+ z.^2
        f_x = ((cell2mat(x(1,1))).^2) +(cell2mat(x(1,2))).^2+ ...
            (cell2mat(x(1,3))).^2;      
          
        
end

end
