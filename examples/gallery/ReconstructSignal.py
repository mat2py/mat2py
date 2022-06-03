# type: ignore
import mat2py as mp
from mat2py.core import *


def square(t, duty):
    tmp = mod(t, 2 * pi)
    w0 = ((2 * pi) @ M[duty]) / 100
    nodd = tmp < w0
    s = (2 * nodd) - 1
    return s


def example():
    clear()
    clc()
    T = 40
    F = mrdivide(1, T)
    D = 23
    dt = (mrdivide(D, T)) * 100
    N = 50
    w0 = mrdivide(2 * pi, T)
    t1 = M[0:0.002:T]
    x1 = square(((2 * pi) @ M[F]) @ M[t1], dt)
    t2 = M[0:0.002:D]
    x2 = zeros(1, length(t2))
    dif = T - D
    null_index = t1 <= D
    x2[I[null_index(M[1 : length(x2)])]] = x1(t1 <= D)
    x2[I[1, dif:D]] = x1(1, M[dif:D])
    X = zeros(1, (2 * N) + 1) + 0j
    for k in M[(-N):N]:
        x3 = copy(x1)
        x3 = x3 * exp((((-1j) * k) @ M[w0]) @ M[t1])

    for i in M[1 : (length(t1) - 1)]:
        X[I[(k + N) + 1]] = X((k + N) + 1) + (
            ((M[t1(i + 1) - t1(i)]) @ (x3(i) + x3(i + 1))) / 2
        )

    x_rec = zeros(1, length(t1)) + 0j
    for k in M[(-N):N]:
        x_rec[I[i]] = x_rec(i) + (
            (M[(mrdivide(1, T)) @ M[X(k + 51)]]) @ exp(((1j * k) @ M[w0]) @ M[t1(i)])
        )

    plot(t2, x2, t1, x_rec, "--")
    shg()
    w = M[((-50) * w0) : w0 : (50 * w0)]
    plot(mrdivide(w, 2 * pi), abs(X), "o")
    shg()


if __name__ == "__main__":
    example()

__doc__ = """
% this example is a slightly modified version
% from [here](https://www.physicsforums.com/threads/reconstruct-a-signal-by-determining-the-n-fourier-coefficients.982179/)

function example()

clear();
clc();

%My code:
%Type of signal: square


T = 40; %Period of the signal [s]
F=1/T;   % fr
D = 23; % length of signal(duration)
dt=(D/T)*100;
N = 50; %Number of coefficients
w0 = 2*pi/T; %signal pulse
t1= 0:0.002:T; % original signal sampling
x1 = square((2*pi*F)*(t1),dt);%initial square signal
t2= 0:0.002:D; %modified signal sampling
x2 = zeros(1,length(t2)); %initializing the modified signal with null values.
dif=T-D;

null_index = t1<=D; % Matlab have a lot of strange beheviour
x2(null_index(1:length(x2)))=x1(t1<=D);% modify the null values with values from the original signal.
x2(1,dif:D)=x1(1,dif:D); %modify for values of t1>=T-D.


X = zeros(1, 2*N+1)+0j;
for k = -N:N %k represents the variable after which the sum is achieved
x3 = x1; %x3 represents the signal obtained after the Fourier Series formula;
x3 = x3 .* exp(-1i*k*w0*t1);
end


for i = 1:length(t1)-1
X(k+N+1) = X(k+N+1) + (t1(i+1)-t1(i)) * (x3(i)+x3(i+1))/2; %reconstruction using the coefficients
end

x_rec = zeros(1, length(t1))+0j;

for k=-N:N
x_rec(i) = x_rec(i) + (1/T) * X(k+51) * exp(1i*k*w0*t1(i));  %reconstruction using the coefficients ( the integral being calculated as a sum)
end


plot(t2,x2, t1, x_rec, '--')
shg()

w=-50*w0:w0:50*w0; %w is the vector which allows displaying the spectre of the function

plot(w/(2*pi),abs(X), 'o');
shg()

end


% This function is copied from Matlab signal toolbox
function s = square(t,duty)

% Compute values of t normalized to (0,2*pi)
tmp = mod(t,2*pi);

% Compute normalized frequency for breaking up the interval (0,2*pi)
w0 = 2*pi*duty/100;

% Assign 1 values to normalized t between (0,w0), 0 elsewhere
nodd = (tmp < w0);

% The actual square wave computation
s = 2*nodd-1;

end
"""
