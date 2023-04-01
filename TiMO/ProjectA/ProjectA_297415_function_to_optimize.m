function f_x = Project1_297415_function_to_optimize(x,which_function)
%Below choosen functions to optimize

switch which_function
    case 1
        f_x = x.^2 + 1; %First function
    case 2
        f_x = (x.^2 - 5.*x + 6)./(x.^2+1); %Second Function
    case 3
        f_x = sin(x) + sin(10/3.*x); %Third function
    case 4
        f_x = -exp(-x).*sin(2*pi.*x); %Fourth function
end

end

