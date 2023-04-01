function [drawn_points] = Function_draw_ProjectB_Group1(which_function,constraints)
%Below - draw starting points

drawn_point_0 = [];
drawn_next_point = [];
drawn_points = {};
lambda = [];

all_good = false;

for i = 1:(which_function+1)
    
    if i == 1
    
        for j = 1:which_function
            drawn_point_new_0 = rand(1,1).*(constraints(j,2) - constraints(j,1)) + constraints(j,1);
            drawn_point_0 = [drawn_point_0, drawn_point_new_0]; 
        end
        
        drawn_points(i,1) = {drawn_point_0};
        
    else
        
        while 1
        
            drawn_next_point = [];
            lambda = [];

            for j = 1:which_function
                lambda_new = rand(1,1).*(constraints(j,2) - constraints(j,1)) + constraints(j,1);
                lambda = [lambda, lambda_new];
            end

            drawn_next_point = drawn_point_0 + lambda.*ones(1,which_function);

            for j = 1:which_function
                if drawn_next_point(1,j) < constraints(j,1) || drawn_next_point(1,j) > constraints(j,2)
                    all_good = false;
                end
            end

            if all_good == true 
                break
            end

            all_good = true;

        end
        
        drawn_points(i,1) = {drawn_next_point};
    end
  
end

end

