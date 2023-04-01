%TiMO Project task: Part A, made by: Bartłomiej Guś - 297415
clear all;
clc;

which_function_you_want_to_optimize = 1;
without_limits = 0; % 1 - without limits,  0 - with limits

%% Golden ratio method

if without_limits == 1
    big_value = 10000;
    down_constraint = rand()*(2*big_value) - big_value;
    up_constraint = rand()*(2*big_value) - big_value;
else
    switch which_function_you_want_to_optimize
        case 1
            down_constraint = -5;
            up_constraint = 5;
            a_b(1) = rand()*(0-down_constraint) + down_constraint;
            a_b(2) = rand()*(up_constraint-0) + 0;
        case 2
            down_constraint = -6;
            up_constraint = 6;
            a_b(1) = rand()*(2-(-0.5)) + (-0.5);
            a_b(2) = rand()*(6-3) + 3;
        case 3
            down_constraint = 2.7;
            up_constraint = 7.5;
            a_b(1) = rand()*(5-4) + 4;
            a_b(2) = rand()*(6.5-5.5) + 5.5;
        case 4
            down_constraint = 0;
            up_constraint = 4;
            a_b(1) = rand()*(0.2-0) + 0;
            a_b(2) = rand()*(0.6-0.3) + 0.3;
    end
end

epsilon = 0.000001;

if down_constraint < up_constraint
    constraints = [down_constraint,up_constraint];
elseif down_constraint > up_constraint
    constraints = [up_constraint,down_constraint];
else
    disp("It doesn't make sense to use when the down constraint and up constraint are the same value");
    return
end

if without_limits == 1
    M_next_steps = Project1_297415_golden_ratio(epsilon,constraints,which_function_you_want_to_optimize);
else
    M_next_steps = Project1_297415_golden_ratio(epsilon,a_b,which_function_you_want_to_optimize);
end

steps_to_plot = 0.001;

M_X = constraints(1):steps_to_plot:constraints(2);
M_Y = Project1_297415_function_to_optimize(M_X,which_function_you_want_to_optimize);

if without_limits == 1
    M_Y_a_b = Project1_297415_function_to_optimize(constraints,which_function_you_want_to_optimize);
else
    M_Y_a_b = Project1_297415_function_to_optimize(a_b,which_function_you_want_to_optimize);
end

M_Y_next_steps = Project1_297415_function_to_optimize(M_next_steps,which_function_you_want_to_optimize);

found_minimum = M_next_steps(end);

Y_found_minimum = Project1_297415_function_to_optimize(found_minimum,which_function_you_want_to_optimize);

figure;
plot(M_X,M_Y);
hold on

if without_limits == 1
    plot(constraints,M_Y_a_b,'Color','#2c5140','LineStyle','None','Marker','x','MarkerSize',10);
else
    plot(a_b,M_Y_a_b,'Color','#2c5140','LineStyle','None','Marker','x','MarkerSize',10);
end


plot(M_next_steps,M_Y_next_steps,'Color','#e52b50','LineStyle','None','Marker','x','MarkerSize',15);
plot(found_minimum,Y_found_minimum,'*','MarkerSize',25);

title(strcat('Golden ratio optimazation - function: ',num2str(which_function_you_want_to_optimize),' ,found minimum in x: ', num2str(found_minimum)),'FontSize',25);
xlabel('x','FontSize',20);
ylabel('f(x)','FontSize',20);
legend('Function to optimize','Starting [a,b]','Next minimum','Final found minimium');
axis padded
grid on
hold off

%% Simple gradient descent

if without_limits == 1
    big_value = 1000;
    down_constraint = -big_value;
    up_constraint = big_value;
else
    switch which_function_you_want_to_optimize
        case 1
            down_constraint = -5;
            up_constraint = 5;
            rand_constraints(1) = down_constraint;
            rand_constraints(2) = up_constraint;
        case 2
            down_constraint = -5;
            up_constraint = 5;
            rand_constraints(1) = 0;
            rand_constraints(2) = 4.5;
        case 3
            down_constraint = 2.7;
            up_constraint = 7.5;
            rand_constraints(1) = 4.5;
            rand_constraints(2) = 6;
        case 4
            down_constraint = 0;
            up_constraint = 4;
            rand_constraints(1) = 0;
            rand_constraints(2) = 0.6;
    end
end

rate = 0.05;
neighborhood = 0.00001;
epsilon = 0.00001;

if down_constraint < up_constraint
    constraints = [down_constraint,up_constraint];
elseif down_constraint > up_constraint
    constraints = [up_constraint,down_constraint];
else
    disp("It doesn't make sense to use when the down constraint and up constraint are the same value");
    exit();
end

if without_limits == 1
    starting_point = rand()*(constraints(2)-constraints(1)) + constraints(1);
else
    starting_point = rand()*(rand_constraints(2)-rand_constraints(1)) + rand_constraints(1);
end

M_next_steps = Project1_297415_simple_gradient_descent(rate,starting_point,neighborhood,epsilon,...
    which_function_you_want_to_optimize,constraints);

steps_to_plot = 0.01;

if without_limits == 1
    M_to_plot = [M_next_steps starting_point];
    M_X = min(M_to_plot):steps_to_plot:max(M_to_plot);
else
    M_X = constraints(1):steps_to_plot:constraints(2);
end

M_Y = Project1_297415_function_to_optimize(M_X,which_function_you_want_to_optimize);

M_Y_starting_point = Project1_297415_function_to_optimize(starting_point,which_function_you_want_to_optimize);

M_Y_next_steps = Project1_297415_function_to_optimize(M_next_steps,which_function_you_want_to_optimize);

found_minimum = M_next_steps(end);

Y_found_minimum = Project1_297415_function_to_optimize(found_minimum,which_function_you_want_to_optimize);

figure;
plot(M_X,M_Y);
hold on
plot(starting_point,M_Y_starting_point,'Color','#2c5140','LineStyle','None','Marker','x','MarkerSize',10);
plot(M_next_steps,M_Y_next_steps,'Color','#e52b50','LineStyle','None','Marker','x','MarkerSize',15);
plot(found_minimum,Y_found_minimum,'*','MarkerSize',25);


title(strcat('Simple descent gradient optimazation - function: ',num2str(which_function_you_want_to_optimize),' ,found minimum in x: ', num2str(found_minimum)),'FontSize',25);
xlabel('x','FontSize',23);
ylabel('f(x)','FontSize',23);
legend('Function to optimize','Starting point','Next step','Found minimium');
axis padded
grid on
hold off
