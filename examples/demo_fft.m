function demo_fft()
clear
clc
rng default

t = 1:10;
x = randn(size(t))';
ts = linspace(-5,15,2^9);
[Ts,T] = ndgrid(ts,t);
y = sinc(Ts - T)*x;

f = my_fft(y);

disp([y, f]);
%plot(y, 'o')
%plot(f, 'o')
end


function X = my_fft(x)
%only works if N = 2^k
N = numel(x);
xp = x(1:2:end);
xpp = x(2:2:end);
if N>=8
    Xp = my_fft(xp);
    Xpp = my_fft(xpp);
    %X = zeros(N,1);
    Wn = exp(-1i*2*pi*((0:N/2-1)')/N);
    tmp = Wn .* Xpp;
    X = [(Xp + tmp);(Xp -tmp)];
else
    switch N
        case 2
            X = [1 1;1 -1]*x;
        case 4
            X = [1 0 1 0; 0 1 0 -1i; 1 0 -1 0;0 1 0 1i]*[1 0 1 0;1 0 -1 0;0 1 0 1;0 1 0 -1]*x;
        otherwise
            error('N not correct.');
    end
end
end

function y=sinc(x)

i=find(x==0);
x(i)= 1;
y = sin(pi*x)./(pi*x);
y(i) = 1;
end
