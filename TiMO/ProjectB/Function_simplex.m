%Reflection function

function [result, results_to_draw_outpot] = Function_simplex(points, p_max, p_min, p_max_index, p_min_index, p_tilde,which_function_you_want_to_optimize, alfa, gamma, beta, sigma, epsilon, constraints)
   
results_to_draw = {p_max};

            while 1
                
                p_reflected = p_tilde + alfa*(p_tilde-p_max);
                p_reflected = Function_check_constraints(constraints,p_reflected);
                p_reflected_mod = {};
                p_min_mod = {};
                p_max_mod = {};
                p_e_mod = {};
                p_z_mod = {};
                
                
                for j = 1:which_function_you_want_to_optimize
                    p_reflected_mod{size(p_reflected_mod,2)+1} = p_reflected(1,j);
                    p_min_mod{size(p_min_mod,2)+1} = p_min(1,j);
                    p_max_mod{size(p_max_mod,2)+1} = p_max(1,j);
                end
                
                f_reflected = Function_to_optimize_ProjectB_Group1(p_reflected_mod,which_function_you_want_to_optimize);
                f_min = Function_to_optimize_ProjectB_Group1(p_min_mod,which_function_you_want_to_optimize);
                f_max = Function_to_optimize_ProjectB_Group1(p_max_mod,which_function_you_want_to_optimize);

                if f_reflected < f_min
                   p_e = p_tilde +  gamma*(p_reflected - p_tilde);
                   p_e = Function_check_constraints(constraints,p_e);
                   for j = 1:which_function_you_want_to_optimize
                       p_e_mod{size(p_e_mod,2)+1} = p_e(1,j);
                   end
                   f_e = Function_to_optimize_ProjectB_Group1(p_e_mod,which_function_you_want_to_optimize);
                   if f_e < f_reflected
                       points{p_max_index(1)} = p_e;
                   else
                       points{p_max_index(1)} = p_reflected;
                   end
                else
                    if f_reflected >= f_min && f_reflected < f_max 
                       points{p_max_index(1)} = p_reflected;
                    else
                        p_z = p_tilde + beta*(p_max - p_tilde);
                        p_z = Function_check_constraints(constraints,p_z);
                        for j = 1:which_function_you_want_to_optimize
                            p_z_mod{size(p_z_mod,2)+1} = p_z(1,j);
                        end
                        f_z = Function_to_optimize_ProjectB_Group1(p_z_mod,which_function_you_want_to_optimize);
                        if f_z >= f_max 
                            for i = 1:size(points)
                                if points{i} ~= p_min
                                    points{i} = sigma*(points{i}+p_min);
                                end
                            end
                        else
                            points{p_max_index(1)} = p_z; 
                        end
                    end
                end
                
                max_temp = [];
                for i = 1:size(points)
                    if i ~= p_min_index
                        %max_temp{i} = abs(p_min - points{i});
                        max_temp(i) = Function_get_distance_between_points(p_min,points{i});
                    else
                        max_temp(i) = -inf ;
                    end
                end

                max_ = max(max_temp);
                max_index = find(max_temp==max_);
                
                results_to_draw{size(results_to_draw,2)+1} = points{max_index,1};
                
                if max_ < epsilon
                    result = points{max_index,1};
                    results_to_draw_outpot = results_to_draw;
                    break
                else
                    [p_min, p_min_index, p_max, p_max_index, p_tilde] = Function_get_min_max_and_pG(points);

                end
                
            end
 
end