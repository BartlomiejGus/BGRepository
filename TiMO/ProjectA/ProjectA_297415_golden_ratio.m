function [M_next_steps] = Project1_297415_golden_ratio(epsilon,constraints,which_function)
%Golden ratio method to optimize

if constraints(1) == 0 && constraints(2) == 0
    %Case where there aren't constraints
end

M_intervals = constraints;
M_lambdas = zeros(1,2);
golden_ratio = (sqrt(5) - 1)/2;
distance_between_tested_intervals = abs(M_intervals(1) - M_intervals(2));

M_pom = 0;

while distance_between_tested_intervals >= epsilon
    
    M_lambdas(1) = M_intervals(1) + golden_ratio*golden_ratio*distance_between_tested_intervals;
    M_lambdas(2) = M_intervals(2) - golden_ratio*golden_ratio*distance_between_tested_intervals;
    
    M_f_lambdas(1) = Project1_297415_function_to_optimize(M_lambdas(1),which_function);
    M_f_lambdas(2) = Project1_297415_function_to_optimize(M_lambdas(2),which_function);

%     disp('Intervals');
%     disp(M_intervals);
%     
%     disp('Lambdas');
%     disp(M_lambdas);
    
    if M_f_lambdas(2) >= M_f_lambdas(1)
        M_intervals(2) = M_lambdas(2);
    elseif M_f_lambdas(2) < M_f_lambdas(1)
        M_intervals(1) = M_lambdas(1);
    end
    
    min = (M_intervals(1)+M_intervals(2))/2;
    
    M_pom = [M_pom min];
    
    distance_between_tested_intervals = abs(M_intervals(1) - M_intervals(2));
    
end

M_next_steps = M_pom(2:end);

end

