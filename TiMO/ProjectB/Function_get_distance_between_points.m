function result = Function_get_distance_between_points(p1,p2)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
[rows colls] = size(p1);
sum=0;
for i=1:colls
    distance = sqrt((p2(i)-p1(i))^2);
    sum = sum+distance;
end
result = sum;
end

