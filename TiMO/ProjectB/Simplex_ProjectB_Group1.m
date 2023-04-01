
%ProjectB - Group(1): Simplex Neldera-Meada
%Made by: WD, PW, MN, MM, Bartłomiej Guś

clear all, clc

txt = "Which function you want to optimize ? Opportunity:(1,2,3): ";
which_function_you_want_to_optimize = input(txt);

constraints = zeros(which_function_you_want_to_optimize,2);

%Below constraints
for i = 1:which_function_you_want_to_optimize
    
    txt = "Give the low constraint for the " + int2str(i) + " variable: ";
    constraints(i,1) = input(txt);
    
    txt = "Give the high constraint for the " + int2str(i) + " variable: ";
    constraints(i,2) = input(txt);
end

txt = "Give the alpha value: ";
alpha = input(txt);

txt = "Give the beta value: ";
beta = input(txt);

txt = "Give the gamma value: ";
gamma = input(txt);

txt = "Give the sigma value: ";
sigma = input(txt);

txt = "Give the epsilon value: ";
epsilon = input(txt);

steps_to_plot = 0.1;

% which_function_you_want_to_optimize = 2;
% alpha = 1;
% beta = 0.5;
% gamma = 0.1;
% sigma = 0.5;
% epsilon = 0.1;

switch which_function_you_want_to_optimize
    
    case 1
       
        %constraints = [-10,10];
        x(1,:) = constraints(1,1):steps_to_plot:constraints(1,2);
        x_to_draw = {};
        x_to_draw(1,1) = {x};
        y = Function_to_optimize_ProjectB_Group1(x_to_draw,which_function_you_want_to_optimize);
        
        plot(x,y);
        hold on;
        
        drawn_points = Function_draw_ProjectB_Group1(which_function_you_want_to_optimize,constraints);
        
        [pMin, indexMin,pMax,indexMax,pG] = Function_get_min_max_and_pG(drawn_points);

        [result, results_to_draw] = Function_simplex(drawn_points,pMax,pMin,indexMax,indexMin,pG,which_function_you_want_to_optimize,alpha, gamma, beta, sigma, epsilon, constraints);
        
        results_to_draw = results_to_draw';
        
        x_points = [];
        z_points = [];
        
        z_result = Function_to_optimize_ProjectB_Group1({result},which_function_you_want_to_optimize);
        
        for i = 1:size(results_to_draw,1)
             x_points = [x_points, results_to_draw{i,1}];
    
             z_points = [z_points, Function_to_optimize_ProjectB_Group1({results_to_draw{i,1}},which_function_you_want_to_optimize)];
              mess = "Itr: "  + num2str(i)  + ...
                  " val " + num2str(z_points(1,i));
            %disp(num2str(x_points(1,i)));
            text(x_points(1,i),z_points(1,i),mess);
        end
        
        plot(x_points,z_points,'+','Color','r','MarkerSize',9,'LineWidth',3);
        
        plot(result,z_result,'+','Color','magenta','MarkerSize',20,'LineWidth',3);
        [t,s] = title('First Function - one variable"');
        t.FontSize = 16;
        xlabel('X','fontsize',10);
        ylabel('Z','fontsize',10);
        hold off;

        disp(" ")
        disp("Below results:")
        disp("Min first varliable :" + num2str(result(1,1))); 
        disp("Min function value : "+ num2str(z_result));
      

        
    case 2
        
        %constraints = [-4,4;-4,4];
                        
        x_temp(1,1) = size(constraints(1,1):steps_to_plot:constraints(1,2),2);
        x_temp(1,2) = size(constraints(2,1):steps_to_plot:constraints(2,2),2);
        
        n = min(x_temp);

        x_surf(1,:) = linspace(constraints(1,1),constraints(1,2),n);
        x_surf(2,:) = linspace(constraints(2,1),constraints(2,2),n);
        
        [X1_mesh,X2_mesh] = meshgrid(x_surf(1,:),x_surf(2,:));
        
        x_to_draw = {};
        x_to_draw(1,1) = {X1_mesh};
        x_to_draw(1,2) = {X2_mesh};
        
        z_surf = Function_to_optimize_ProjectB_Group1(x_to_draw,which_function_you_want_to_optimize);
        
        surf(x_surf(1,:),x_surf(2,:),z_surf)
        hold on;
        
        drawn_points = Function_draw_ProjectB_Group1(which_function_you_want_to_optimize,constraints);
        
        [pMin, indexMin,pMax,indexMax,pG] = Function_get_min_max_and_pG(drawn_points);
        
        [result, results_to_draw] = Function_simplex(drawn_points,pMax,pMin,indexMax,indexMin,pG,which_function_you_want_to_optimize,alpha, gamma, beta, sigma, epsilon, constraints);
        
        results_to_draw = results_to_draw';
        
        cell_results_to_draw = {};
        
        x = [];
        y = [];
        z = [];
        
        for i = 1:size(results_to_draw,1)
             for j = 1:which_function_you_want_to_optimize
                 cell_results_to_draw{size(cell_results_to_draw,2)+1} = results_to_draw{i}(1,j);
             end
             x = [x, cell_results_to_draw{1,1}];
             y = [y, cell_results_to_draw{1,2}];
             
             z = [z, Function_to_optimize_ProjectB_Group1(cell_results_to_draw,which_function_you_want_to_optimize)];
             cell_results_to_draw = {};
        end
        
        z_result_final = Function_to_optimize_ProjectB_Group1({result(1,1),result(1,2)},which_function_you_want_to_optimize);
        
        shading interp
        
        for i = 1:(size(x,2)-2)
            
            x_line = linspace(x(i),x(i+1));
            y_line = linspace(y(i),y(i+1)) ;
            z_line = interp2(x_surf(1,:),x_surf(2,:),z_surf,x_line,y_line); 
            plot3(x_line,y_line,z_line, '--','Color','r','LineWidth',2);
            
        end
        
        plot3(x,y,z, '+','Color','r','MarkerSize',9,'LineWidth',3);
        plot3(result(1,1),result(1,2),z_result_final,'+','Color','magenta','MarkerSize',20,'LineWidth',3);
        [t,s] = title('Second Function - two variables:"Himmelblau"');
        t.FontSize = 16;
        xlabel('X','fontsize',10);
        ylabel('Y','fontsize',10);
        zlabel('Z','fontsize',10);
        hold off;

        disp(" ")
        disp("Below results:")
        disp("Min first varliable :" + num2str(result(1,1))); 
        disp("Min second varliable :" + num2str(result(1,2)));
        disp("Min function value : "+ num2str(z_result_final));
         

        
    case 3
        %constraints = [-4,4;-4,4;-4 4];
        x_temp(1,1) = size(constraints(1,1):steps_to_plot:constraints(1,2),2);
        x_temp(1,2) = size(constraints(2,1):steps_to_plot:constraints(2,2),2);
        x_temp(1,3) = size(constraints(3,1):steps_to_plot:constraints(3,2),2);

        n = min(x_temp);

        x_surf(1,:) = linspace(constraints(1,1),constraints(1,2),n);
        x_surf(2,:) = linspace(constraints(2,1),constraints(2,2),n);
        x_surf(3,:) = linspace(constraints(3,1),constraints(3,2),n);

        [X1_mesh,X2_mesh,X3_mesh] = meshgrid(x_surf(1,:),x_surf(2,:),x_surf(3,:));

        x_to_draw = {};
        x_to_draw(1,1) = {X1_mesh};
        x_to_draw(1,2) = {X2_mesh};
        x_to_draw(1,3) = {X3_mesh};
        
        z_surf= Function_to_optimize_ProjectB_Group1(x_to_draw,which_function_you_want_to_optimize);
        
        %surf(x_surf(1,:),x_surf(2,:),x_surf(3,:),z_surf);
         
        drawn_points = Function_draw_ProjectB_Group1(which_function_you_want_to_optimize,constraints);
        
        [pMin, indexMin,pMax,indexMax,pG] = Function_get_min_max_and_pG(drawn_points);
        [result, results_to_draw] = Function_simplex(drawn_points,pMax,pMin,indexMax,indexMin,pG,which_function_you_want_to_optimize,alpha, gamma, beta, sigma, epsilon, constraints);
        
        results_to_draw = results_to_draw';
        
        cell_results_to_draw = {};
        x = [];
        y = [];
        z = [];
        g = [];
        for i = 1:size(results_to_draw,1)
             for j = 1:which_function_you_want_to_optimize
                 cell_results_to_draw{size(cell_results_to_draw,2)+1} = results_to_draw{i}(1,j);
             end
             x = [x; cell_results_to_draw{1,1}];
             y = [y; cell_results_to_draw{1,2}];
             z = [z; cell_results_to_draw{1,3}];
             g = [g; Function_to_optimize_ProjectB_Group1(cell_results_to_draw,which_function_you_want_to_optimize)];
             cell_results_to_draw = {};
        end
        z_result_final = Function_to_optimize_ProjectB_Group1({result(1,1),result(1,2),result(1,3)},which_function_you_want_to_optimize);

        scatter3(x,y,z,40,g,'filled')
        hold on

        scatter3(result(1,1),result(1,2),result(1,3),200 ...
            ,z_result_final,'+','magenta');
        xlabel('X') 
        ylabel('Y')
        zlabel('Z')
        cb = colorbar;
        hold off
        
        disp(" ")
        disp("Below results:")
        disp("Min first varliable :" + num2str(result(1,1))); 
        disp("Min second varliable :" + num2str(result(1,2))); 
        disp("Min third varliable :" + num2str(result(1,3)));
        disp("Min function value : "+ num2str(z_result_final)); 

end







