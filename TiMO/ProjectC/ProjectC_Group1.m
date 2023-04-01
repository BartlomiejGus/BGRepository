%ProjectC - Group(1): Simplex Neldera-Meada
%Made by: WD, PW, MN, MM, Bartłomiej Guś

clear all,clc;

disp("1: (x^2+y-11)^2 + (x + y^2 -7)^2");
disp("2:  x^2+ x*y + 2*x + y^2");
disp("3: x^4 - 3*x^2*y^2+23*x^3+3*y^2 - 2");
which_function_you_want_to_optimize = input(" Which function you want to optimize? ");

how_many_inequality_constraints_you_want_to_give = input("How many inequality constraints you want to give? ");

how_many_equality_constraints_you_want_to_give = input("How many equality constraints you want to give? ");

inequality_constraints = zeros(how_many_inequality_constraints_you_want_to_give,2);
value_inequality_constraints = zeros(how_many_inequality_constraints_you_want_to_give,1);

equality_constraints = zeros(how_many_equality_constraints_you_want_to_give,2);
value_equality_constraints = zeros(how_many_equality_constraints_you_want_to_give,1);

disp("Convention of inequality constraints: A*x+B*Y<=C");

for i = 1:how_many_inequality_constraints_you_want_to_give
    
    inequality_constraints(i,1) = input("Give me the cofficient A: ");
    inequality_constraints(i,2) = input("Give me the cofficient B: ");
    value_inequality_constraints(i,1) = input("Give me the cofficient C: ");
    
end

disp("Convention of equality constraints: A*x+B*Y=C");

for i = 1:how_many_equality_constraints_you_want_to_give
    
    equality_constraints(i,1) = input("Give me the cofficient A: ");
    equality_constraints(i,2) = input("Give me the cofficient B: ");
    value_equality_constraints(i,1) = input("Give me the cofficient C: ");
    
end

x_lim(1,1) = input("Give me lower limit of x - needed to graph: ");
x_lim(2,1) = input("Give me upper limit of x - needed to graph: ");

y_lim(1,1) = input("Give me lower limit of y - needed to graph: ");
y_lim(2,1) = input("Give me upper limit of y - needed to graph: ");

%Docelowe ogranicznia dla 1 funkcji
%2*x+3*y==6
%x+y>=1

%Dla 2 funkcji
%0.5*x+y<=1
%x<=1
%-x+y<=0
%y>=-1.5

%Dla 3 funkcji
%x==0.3
%y==0.2


%% CasADI

addpath('C:\Users\barte\Desktop\StudiaMGRII\TiMO\Lab\CasADi')
import casadi.*

opti = casadi.Opti();

%which_function_you_want_to_optimize = 3;

switch which_function_you_want_to_optimize
    
    case 1
        x = opti.variable();
        y = opti.variable();

        opti.minimize( (x^2+y-11)^2 + (x + y^2 -7)^2 );
        
        for i = 1:how_many_inequality_constraints_you_want_to_give
            
            opti.subject_to(inequality_constraints(i,1)*x+inequality_constraints(i,2)*y <= value_inequality_constraints(i,1));
            
        end
        
        for i = 1:how_many_equality_constraints_you_want_to_give
            
            opti.subject_to(equality_constraints(i,1)*x+equality_constraints(i,2)*y == value_equality_constraints(i,1));
            
        end
%         opti.subject_to( 2*x+3*y==6 );
%         opti.subject_to(x+y>=1);


        opti.solver('ipopt');
        
        sol = opti.solve();
        
        figure
        
        plot(sol.value(x),sol.value(y),'go','LineWidth',3);
        text(sol.value(x),sol.value(y),"Found min : " + num2str(sol.value(x)) + " " + num2str(sol.value(y)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,(X.^2+Y-11).^2 + (X + Y.^2 -7).^2,100);
        title("CasADI: (x^2+y-11)^2 + (x + y^2 -7)^2",'FontSize',20);
        
    case 2
        x = opti.variable();
        y = opti.variable();
        opti.minimize( x^2+ x*y + 2*x + y^2 );
        %Docelowe ogranicznia
        %0.5*x+y<=1
        %x<=1
        %-x+y<=0
        %y>=-1.5
        
        for i = 1:how_many_inequality_constraints_you_want_to_give
            
            opti.subject_to(inequality_constraints(i,1)*x+inequality_constraints(i,2)*y <= value_inequality_constraints(i,1));
            
        end
        
        for i = 1:how_many_equality_constraints_you_want_to_give
            
            opti.subject_to(equality_constraints(i,1)*x+equality_constraints(i,2)*y == value_equality_constraints(i,1));
            
        end

        opti.solver('ipopt');
        
        sol = opti.solve();
        
        sol.value(x)
        sol.value(y)
        
        figure
        
        plot(sol.value(x),sol.value(y),'go','LineWidth',3);
        text(sol.value(x)+0.01,sol.value(y)+0.01,"Found min : " + num2str(sol.value(x)) + " " + num2str(sol.value(y)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,X.^2+X.*Y + 2.*X + Y.^2,100);
        title("CasADI: x^2+ x*y + 2*x + y^2",'FontSize',20);
        
    case 3
        
        x = opti.variable();
        y = opti.variable();
        opti.minimize( x^4 - 3*x^2*y^2+23*x^3+3*y^2 - 2 );
        %Docelowe ogranicznia
        %x==0.3
        %y==0.2
        
        for i = 1:how_many_inequality_constraints_you_want_to_give
            
            opti.subject_to(inequality_constraints(i,1)*x+inequality_constraints(i,2)*y <= value_inequality_constraints(i,1));
            
        end
        
        for i = 1:how_many_equality_constraints_you_want_to_give
            
            opti.subject_to(equality_constraints(i,1)*x+equality_constraints(i,2)*y == value_equality_constraints(i,1));
            
        end

        opti.solver('ipopt');
        
        sol = opti.solve();
        
        sol.value(x)
        sol.value(y)
        
        figure
        
        plot(sol.value(x),sol.value(y),'go','LineWidth',3);
        text(sol.value(x)+0.1,sol.value(y)+0.1,"Found min : " + num2str(sol.value(x)) + " " + num2str(sol.value(y)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,X.^4 - 3.*X.^2.*Y.^2+23.*X.^3+3.*Y.^2 - 2,100);
        title("CasADI: x^4 - 3*x^2*y^2+23*x^3+3*y^2 - 2",'FontSize',20);

end

%Below draw section
%Inequality section

ts = linspace(x_lim(1,1),x_lim(2,1));

for i = 1:how_many_inequality_constraints_you_want_to_give

    if inequality_constraints(i,1) == 0 && inequality_constraints(i,2) == 0

        if 0>value_inequality_constraints(i,1)
            disp("For "+num2str(inequality_constraints(i,1)) +"x + " + num2str(inequality_constraints(i,2)) +"y <= " +...
               num2str(value_inequality_constraints(i,1)));
            exit();
        end

    elseif inequality_constraints(i,1) == 0

        y_temp = zeros(1,size(ts,2)) + sign(inequality_constraints(i,2))*value_inequality_constraints(i,1);
        plot(ts,y_temp,'r','linewidth',1);

    elseif inequality_constraints(i,2) == 0

        x_temp = zeros(1,size(ts,2)) + sign(inequality_constraints(i,1))*value_inequality_constraints(i,1);
        plot(x_temp,ts,'r','linewidth',1);

    else

        plot(ts,value_inequality_constraints(i,1)/inequality_constraints(i,2) - (inequality_constraints(i,1)/inequality_constraints(i,2))*ts,'r','linewidth',1);

    end

end

%Equality section

for i = 1:how_many_equality_constraints_you_want_to_give

    if equality_constraints(i,1) == 0 && equality_constraints(i,2) == 0

        if 0>value_equality_constraints(i,1)
            disp("For "+num2str(equality_constraints(i,1)) +"x + " + num2str(equality_constraints(i,2)) +"y = " +...
               num2str(value_equality_constraints(i,1)));
            exit();
        end

    elseif equality_constraints(i,1) == 0

        y_temp = zeros(1,size(ts,2)) + sign(equality_constraints(i,2))*value_equality_constraints(i,1);
        plot(ts,y_temp,'k','linewidth',1);

    elseif equality_constraints(i,2) == 0

        x_temp = zeros(1,size(ts,2)) + sign(equality_constraints(i,1))*value_equality_constraints(i,1);
        plot(x_temp,ts,'k','linewidth',1);

    else

        plot(ts,value_equality_constraints(i,1)/equality_constraints(i,2) - (equality_constraints(i,1)/equality_constraints(i,2))*ts,'k','linewidth',1);

    end

end

our_legend(1,1) = "found minimum";
our_legend(2,1) = "function contours";

for i = 1:how_many_inequality_constraints_you_want_to_give
    our_legend(i+2,1) =  num2str(inequality_constraints(i,1)) +"x + " + num2str(inequality_constraints(i,2)) +"y <= " +num2str(value_inequality_constraints(i,1));
end

for i = 1:how_many_equality_constraints_you_want_to_give
    our_legend(i+2+how_many_inequality_constraints_you_want_to_give,1) =  num2str(equality_constraints(i,1)) +"x + " + num2str(equality_constraints(i,2)) +"y = " + num2str(value_equality_constraints(i,1));
end

our_legend = our_legend';

xlim([x_lim(1,1) x_lim(2,1)]);
ylim([y_lim(1,1) y_lim(2,1)]);
legend(our_legend);
xlabel('x');
ylabel('y');

%% Matlab

x0 = [0,0];

%which_function_you_want_to_optimize = 3;

switch which_function_you_want_to_optimize
    
    case 1
        
        fun = @(x)(x(1)^2 + x(2) - 11)^2 +(x(1) + x(2)^2 -7)^2;
        [x,fval,exitflag,output,lambda,grad,hessian] = fmincon(fun,x0,inequality_constraints,value_inequality_constraints,equality_constraints,value_equality_constraints);
        
        figure
        
        plot(x(1,1),x(1,2),'go','LineWidth',3);
        text(x(1,1),x(1,2),"Found min : " + num2str(x(1,1)) + " " + num2str(x(1,2)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,(X.^2+Y-11).^2 + (X + Y.^2 -7).^2,100);
        title("MATLAB Optimization Toolbox: (x^2+y-11)^2 + (x + y^2 -7)^2",'FontSize',20);
        
    case 2
        
        fun = @(x) x(1)^2 + x(1)*x(2) + 2*x(1) + x(2)^2;
        [x,fval,exitflag,output,lambda,grad,hessian] = fmincon(fun,x0,inequality_constraints,value_inequality_constraints,equality_constraints,value_equality_constraints);
        
        figure
        
        plot(x(1,1),x(1,2),'go','LineWidth',3);
        text(x(1,1),x(1,2),"Found min : " + num2str(x(1,1)) + " " + num2str(x(1,2)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,X.^2+X.*Y + 2.*X + Y.^2,100);
        title("MATLAB Optimization Toolbox: x^2+ x*y + 2*x + y^2",'FontSize',20);
        
    case 3
        
        fun = @(x)x(1)^4 - 3*x(1)^2*x(2)^2+23*x(1)^3+3*x(2)^2 - 2;
        [x,fval,exitflag,output,lambda,grad,hessian] = fmincon(fun,x0,inequality_constraints,value_inequality_constraints,equality_constraints,value_equality_constraints);
               
        figure
        
        plot(x(1,1),x(1,2),'go','LineWidth',3);
        text(x(1,1),x(1,2),"Found min : " + num2str(x(1,1)) + " " + num2str(x(1,2)));
        hold on
        [X,Y] = meshgrid(linspace(x_lim(1,1),x_lim(2,1)),linspace(y_lim(1,1),y_lim(2,1)));
        contour(X,Y,X.^4 - 3.*X.^2.*Y.^2+23.*X.^3+3.*Y.^2 - 2,100);
        title("MATLAB Optimization Toolbox: x^4 - 3*x^2*y^2+23*x^3+3*y^2 - 2",'FontSize',20);

end

%Below draw section
%Inequality section

ts = linspace(x_lim(1,1),x_lim(2,1));

for i = 1:how_many_inequality_constraints_you_want_to_give

    if inequality_constraints(i,1) == 0 && inequality_constraints(i,2) == 0

        if 0>value_inequality_constraints(i,1)
            disp("For "+num2str(inequality_constraints(i,1)) +"x + " + num2str(inequality_constraints(i,2)) +"y <= " +...
               num2str(value_inequality_constraints(i,1)));
            exit();
        end

    elseif inequality_constraints(i,1) == 0

        y_temp = zeros(1,size(ts,2)) + sign(inequality_constraints(i,2))*value_inequality_constraints(i,1);
        plot(ts,y_temp,'r','linewidth',1);

    elseif inequality_constraints(i,2) == 0

        x_temp = zeros(1,size(ts,2)) + sign(inequality_constraints(i,1))*value_inequality_constraints(i,1);
        plot(x_temp,ts,'r','linewidth',1);

    else

        plot(ts,value_inequality_constraints(i,1)/inequality_constraints(i,2) - (inequality_constraints(i,1)/inequality_constraints(i,2))*ts,'r','linewidth',1);

    end

end

%Equality section

for i = 1:how_many_equality_constraints_you_want_to_give

    if equality_constraints(i,1) == 0 && equality_constraints(i,2) == 0

        if 0>value_equality_constraints(i,1)
            disp("For "+num2str(equality_constraints(i,1)) +"x + " + num2str(equality_constraints(i,2)) +"y = " +...
               num2str(value_equality_constraints(i,1)));
            exit();
        end

    elseif equality_constraints(i,1) == 0

        y_temp = zeros(1,size(ts,2)) + sign(equality_constraints(i,2))*value_equality_constraints(i,1);
        plot(ts,y_temp,'k','linewidth',1);

    elseif equality_constraints(i,2) == 0

        x_temp = zeros(1,size(ts,2)) + sign(equality_constraints(i,1))*value_equality_constraints(i,1);
        plot(x_temp,ts,'k','linewidth',1);

    else

        plot(ts,value_equality_constraints(i,1)/equality_constraints(i,2) - (equality_constraints(i,1)/equality_constraints(i,2))*ts,'k','linewidth',1);

    end

end

our_legend(1,1) = "found minimum";
our_legend(2,1) = "function contours";

for i = 1:how_many_inequality_constraints_you_want_to_give
    our_legend(i+2,1) =  num2str(inequality_constraints(i,1)) +"x + " + num2str(inequality_constraints(i,2)) +"y <= " +num2str(value_inequality_constraints(i,1));
end

for i = 1:how_many_equality_constraints_you_want_to_give
    our_legend(i+2+how_many_inequality_constraints_you_want_to_give,1) =  num2str(equality_constraints(i,1)) +"x + " + num2str(equality_constraints(i,2)) +"y = " + num2str(value_equality_constraints(i,1));
end

our_legend = our_legend';

xlim([x_lim(1,1) x_lim(2,1)]);
ylim([y_lim(1,1) y_lim(2,1)]);
legend(our_legend);
xlabel('x');
ylabel('y');