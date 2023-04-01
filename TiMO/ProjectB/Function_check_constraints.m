function checked_points = Function_check_constraints(constraints,point)

for i = 1:size(point,2)
    if point(i) < constraints(i,1) 
        point(i) = constraints(i,1);
    end
    if point(i) > constraints(i,2) 
        point(i) = constraints(i,2);
    end
end

checked_points = point;

end

