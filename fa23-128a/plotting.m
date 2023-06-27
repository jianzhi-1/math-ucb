x = [1, 5, 4, 2]
y = [1, 2, 5, -1]
% plot(x, y)
% axis equal
% grid on
% plot(x, y, 'b', 'linewidth', 2)
% xlabel('this is x label')
% ylabel('this is y label')
% title('this is the title')
% plot([1, 4], [3, 2], 'o', 'linewidth', 3)
% hold on
% help plot

x_arr = 0:0.1:10
f = @(x) 2.*x.*cos(2.*x) - (x-2).^2;
plot(x_arr, f(x_arr))
