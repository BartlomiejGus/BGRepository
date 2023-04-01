function [M_next_steps] = Project1_297415_simple_gradient_descent(rate,starting_point,neighborhood,epsilon,which_function,constraints)

M_pom = starting_point;

neighbourhood_plus = Project1_297415_function_to_optimize(starting_point+neighborhood,which_function);
neighbourhood_minus = Project1_297415_function_to_optimize(starting_point,which_function);

gradient = (neighbourhood_plus-neighbourhood_minus)/(neighborhood);

old_point = starting_point; 

difference_between_points = inf;

while difference_between_points >= epsilon
    
    new_point = old_point + rate*(-gradient);
    
    if new_point > constraints(2) || new_point < constraints(1)
        %Break function if new_point goes out from constraints
        break
    end
    
    M_pom = [M_pom new_point];
    
    neighbourhood_plus = Project1_297415_function_to_optimize(new_point+neighborhood,which_function);
    neighbourhood_minus = Project1_297415_function_to_optimize(new_point,which_function);

    gradient = (neighbourhood_plus-neighbourhood_minus)/(neighborhood);
    
    difference_between_points = abs(new_point - old_point);
    
    old_point = new_point;
    
end

M_next_steps = M_pom;

end

