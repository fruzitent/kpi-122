import numpy as np
clear
close_('all')
fID = open('Information.txt','r')
Data_ = np.transpose(fscanf(fID,'%f, %f, %f',np.array([3,inf])))
x = Data_(:,np.array([np.arange(1,2+1)]))
T = Data_(:,3)
fclose(fID)
xn = x.shape
centers = np.array([[np.array([- 10,- 10])],[np.array([- 10,- 5.5])],[np.array([- 10,0])],[np.array([- 6.5,0])],[np.array([- 6.5,- 4.5])],[np.array([0,- 10])],[np.array([- 3.5,- 5])],[np.array([0,- 5])],[np.array([0,0])]])
sigma = np.array([[np.array([5,3])],[np.array([2,1.5])],[np.array([2,4])],[np.array([1.5,2.5])],[np.array([1.5,2])],[np.array([5,3])],[np.array([1.5,2])],[np.array([2,2])],[np.array([5,3])]])
cn = centers.shape
G = np.zeros((xn(1),cn(1)))
for a in np.arange(1,xn(1)+1).reshape(-1):
    for b in np.arange(1,cn(1)+1).reshape(-1):
        G[a,b] = make_func(centers(b,:),sigma(b,:),x(a,:))

Gplus = pinv(np.transpose(G) * G) * np.transpose(G)
W = Gplus * T
spivpad = 0
nespivp = 0
Y = np.zeros((xn(1),1))
for a in np.arange(1,xn(1)+1).reshape(-1):
    tmp = calc_group(W,centers,sigma,x(a,:))
    if tmp > 0.5:
        Y[a] = 1
    else:
        Y[a] = 0
    if Y(a) == T(a):
        spivpad = spivpad + 1
    else:
        nespivp = nespivp + 1

error1 = nespivp
fID = open('Test_information.txt','r')
test = np.transpose(fscanf(fID,'%f, %f, %f',np.array([3,inf])))
x = test(:,np.array([np.arange(1,2+1)]))
T = test(:,3)
fclose(fID)
xn = x.shape
spivpad = 0
nespivp = 0
Y = np.zeros((xn(1),1))
for a in np.arange(1,xn(1)+1).reshape(-1):
    tmp = calc_group(W,centers,sigma,x(a,:))
    if tmp > 0.5:
        Y[a] = 1
    else:
        Y[a] = 0
    if Y(a) == T(a):
        spivpad = spivpad + 1
    else:
        nespivp = nespivp + 1

error2 = nespivp

def make_func(c = None,sigma = None,x = None): 
func = 1
m = c.shape
for a in np.arange(1,m(2)+1).reshape(-1):
    func = func * np.exp(- ((x(a) - c(a)) ** 2) / (2 * sigma(a) ** 2))

return func


def calc_group(W = None,centers = None,sigma = None,x = None): 
y = 0
wn = W.shape
for b in np.arange(1,wn(1)+1).reshape(-1):
    y = y + W(b) * make_func(centers(b,:),sigma(b,:),x)

return y
