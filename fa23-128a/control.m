% compute the nth harmonic sum
n = 10;
sum = 0;
% for i = start:step:stop
for i = 1:n
    sum = sum + 1/i;
end
sum

% if
if mod(10, 3) == 1
    hnodd(4)
end

% while
while n > 5
    n = n - 1
end

% array
xx = [1, 2, 3, 4]
% MatLab is 1-indexed
length(xx)
zz = zeros(1, 10)
ww = ones(1, 10)
qq = 1:10
qq*zz' % ' is for transpose
qq + zz % component-wise addition
qq/zz % not sure what this does
qq./zz % component-wise division
% matrix
A = [1, 2, 3, 4; 
    8, 7, 6, 5; 
    9, 10, 11, 12]
B = [1, 2; 
    3, 4; 
    5, 6; 
    7, 8]
% Bx = y
% x = B \ y
% B(1, 2)
size(A)
size(A, 1)
cc = zeros(3, 4)
