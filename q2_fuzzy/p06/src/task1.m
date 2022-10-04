clear;close all;clc;
fID = fopen('train.txt','r');
Data = fscanf(fID,'%f, %f, %f', [3 inf])';
x = Data(:,[1:2]);
T = Data(:,3); fclose(fID); xn=size(x);
centers = [[-10, -10];[-10, -5.5];[-10, 0];[-6.5, 0];[-6.5, -4.5];[0, -10];[-3.5, -5];[0, -5];[0, 0]];

sigma = [[5, 3]; [2,1.5];[2,4];[1.5,2.5];[1.5,2];[5,3];[1.5,2]; [2,2];[5,3]];
cn = size(centers); G = zeros(xn(1), cn(1));
for a = 1:xn(1)
    for b = 1:cn(1)
        G(a,b) = make_func(centers(b,:),sigma(b,:),x(a,:));
    end
end
Gplus = pinv(G'*G)*G';
W = Gplus*T;
spivpad = 0;
nespivp = 0;
Y = zeros(xn(1),1);
for a = 1:xn(1)
    tmp = calc_group(W,centers,sigma,x(a,:));
    if tmp > 0.5
        Y(a) = 1;
    else
        Y(a) = 0;
    end
    if Y(a) == T(a)
        spivpad = spivpad+1;
    else
        nespivp = nespivp+1;
    end
end

error1 = nespivp;

fID = fopen('test.txt','r');
test = fscanf(fID,'%f, %f, %f', [3 inf])';
x = test(:,[1:2]);
T = test(:,3);
fclose(fID);
xn = size(x);
spivpad = 0;
nespivp = 0;
Y = zeros(xn(1),1);
for a = 1:xn(1)
    tmp = calc_group(W,centers,sigma,x(a,:));
    if tmp > 0.5
        Y(a) = 1;
    else
        Y(a) = 0;
    end
    if Y(a) == T(a)
        spivpad = spivpad+1;
    else
        nespivp = nespivp+1;
    end
end

error2 = nespivp;

function func=make_func(c,sigma,x)
    func = 1; m = size(c);
    for a = 1:m(2)
        func = func*exp(-((x(a)-c(a))^2)/(2*sigma(a)^2));
    end
end

function y = calc_group(W,centers,sigma,x)
    y = 0; wn = size(W);
    for b = 1:wn(1)
        y = y+W(b)*make_func(centers(b,:),sigma(b,:),x);
    end
end
