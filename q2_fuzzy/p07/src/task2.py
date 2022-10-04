import numpy as np
clear('all')
close_('all')
f = open('db.txt')
input_data = np.transpose(fscanf(f,'%d;%f;%f;%f;%f;%f;%f;%f;%f;%f;%d',np.array([11,inf])))
fclose(f)
train_data = input_data(np.arange(1,10+1),np.arange(2,10+1))
train_t = input_data(np.arange(1,10+1),11)
test_data = input_data(np.arange(11,16+1),np.arange(2,10+1))
train_data = norm16(train_data)
test_data = norm16(test_data)

test_t = np.transpose(input_data(np.arange(11,16+1),11))
d = dispersion(train_data)
d = 0.25 * d
# кла�теризаці�
centers = f_c_means(train_data,4)
centers_n,centers_m = centers.shape
train_n = train_data.shape
G = np.zeros((train_n(1),centers_n))
for i in np.arange(1,train_n(1)+1).reshape(-1):
    for j in np.arange(1,centers_n+1).reshape(-1):
        G[i,j] = gauss(train_data(i,:),centers(j,:),centers_m,d)

# Обчи�ленн� вектора ваги
Gplus = inv(np.transpose(G) * G) * np.transpose(G)
W = Gplus * train_t
size_w = W.shape
# кла�ифікаці� на даних навчанн�
test_n = test_data.shape
test_y = np.zeros((1,test_n(1)))
for i in np.arange(1,train_n(1)+1).reshape(-1):
    y = 0
    for k in np.arange(1,size_w+1).reshape(-1):
        y = y + W(k) * gauss(train_data(i,:),centers(k,:),centers_m,d)
    if y <= 0:
        test_y[i] = - 1
    else:
        test_y[i] = 1

error1 = 0
for i in np.arange(1,test_n(1)+1).reshape(-1):
    if not_(train_t(i) == test_y(i)):
        error1 = error1 + 1

test_n = test_data.shape
test_y = np.zeros((1,test_n(1)))
for i in np.arange(1,test_n(1)+1).reshape(-1):
    y = 0
    for k in np.arange(1,size_w+1).reshape(-1):
        y = y + W(k) * gauss(test_data(i,:),centers(k,:),centers_m,d)
    if y <= 0:
        test_y[i] = - 1
    else:
        test_y[i] = 1

error2 = 0
for i in np.arange(1,test_n(1)+1).reshape(-1):
    if not_(test_t(i) == test_y(i)):
        error2 = error2 + 1

#f_c_means.m

def f_c_means(data = None,cluster_n = None):
    e = 0.1
    n,m = data.shape
    centers = np.zeros((cluster_n,m))
    O = np.zeros((n,cluster_n))
    for i in np.arange(1,n+1).reshape(-1):
        k = 1
        for j in np.arange(1,cluster_n+1).reshape(-1):
            r = k * rand
            k = k - r
            O[i,j] = r

    cond = False
    iteration = 1
    d = np.zeros((cluster_n,n))
    while (not_(cond) and iteration <= 100):

        print(np.array(['Iteration ',num2str(iteration)]))
        O_old = O
        for i in np.arange(1,cluster_n+1).reshape(-1):
            for k in np.arange(1,m+1).reshape(-1):
                c = 0
                z = 0
                for j in np.arange(1,n+1).reshape(-1):
                    c = c + (O(j,i) ** 2) * data(j,k)
                    z = z + O(j,i) ** 2
                centers[i,k] = c / z
        for i in np.arange(1,cluster_n+1).reshape(-1):
            for j in np.arange(1,n+1).reshape(-1):
                c = 0
                for l in np.arange(1,m+1).reshape(-1):
                    c = c + (data(j,l) - centers(i,l)) ** 2
                d[i,j] = np.sqrt(c)
        for i in np.arange(1,cluster_n+1).reshape(-1):
            for j in np.arange(1,n+1).reshape(-1):
                c = 0
                if d(i,j) == 0:
                    O[j,i] = 1
                else:
                    for k in np.arange(1,cluster_n+1).reshape(-1):
                        c = c + (d(i,j) / d(k,j)) ** 2
                    O[j,i] = 1 / c
        if sum(np.abs(O - O_old)) <= e:
            cond = True
        iteration = iteration + 1
    return centers

#norm16.m

def norm16(x = None):
    r = x.shape
    dl = np.zeros((r(1),1))
    xx = np.zeros((r(1),r(2)))
    for i in np.arange(1,r(1)+1).reshape(-1):
        dl[i] = norm(x(i,:))

    for i in np.arange(1,r(1)+1).reshape(-1):
        for j in np.arange(1,r(2)+1).reshape(-1):
            xx[i,j] = x(i,j) / dl(i,1)

    return xx

#dispersion.m

def dispersion(data = None):
    n,m = data.shape
    dispersion = np.zeros((1,m))
    for k in np.arange(1,m+1).reshape(-1):
        p = 0
        for i in np.arange(1,n+1).reshape(-1):
            p = p + data(i,k)
        p = p / n
        z = 0
        for i in np.arange(1,n+1).reshape(-1):
            z = z + (data(i,k) - p) ** 2
        dispersion[k] = z / n

    return dispersion

#gauss.m

def gauss(x = None,center = None,m = None,dispersion = None):
    val = 1
    for i in np.arange(1,m+1).reshape(-1):
        val = val + ((x(i) - center(i)) ** 2) / dispersion(i)

    val = np.exp(- np.sqrt(val))
    return val
