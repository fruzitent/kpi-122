from matplotlib import pyplot


class Larsen:
    A11 = []
    A12 = []
    A21 = []
    A22 = []

    B11 = []
    B12 = []
    B21 = []
    B22 = []

    B = []
    B1 = [1, 0.8, 0.6, 0.4, 0.2, 0]
    B2 = [0, 0.2, 0.4, 0.6, 0.8, 1]
    rullist = []
    x11 = []
    x = []
    x1 = 0
    x2 = 0
    x22 = []
    y = [0, 0.2, 0.4, 0.6, 0.8, 1]

    def set(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def x12(self):
        print('you need to enter x')
        self.x1 = float(input('from 0<x<1 :'))
        self.x2 = 1 - self.x1
        self.x = [self.x1, self.x2]
        if 0 < self.x1 < 1:
            print("X=", self.x)
        else:
            print("Erorr input")
            exit(0)

    def regulations(self):
        string = 4
        quantity = 3
        for i in range(string):
            self.rullist.append([])
            print("fill matrix")
            for _ in range(quantity):
                number = int(input(''))
                self.rullist[i].append(number)
            print(' ')
        print(self.rullist)

    def a11(self):
        self.x11 = [0, self.x1, 1]
        self.A11 = [1, self.x2, 0]
        self.A12 = self.x11
        print('\n x1 =', self.x11)
        print('A11 =', self.A11)
        print('A12 =', self.A12)

    def a22(self):
        self.x22 = [0, self.x2, 1]
        self.A21 = [1, self.x1, 0]
        self.A22 = self.x22
        print('\n x2 =', self.x22)
        print('A21 =', self.A21)
        print('A22 =', self.A22)

    def YB(self):
        print('\n y =', self.y)
        print('B1 =', self.B1)
        print('B2 =', self.B2, '\n')

    def first(self):
        f1 = 0
        f2 = 0
        f3 = []
        f12 = 0
        fx = []
        f1 = self.A11[1] if self.rullist[0][0] == 0 else self.A12[1]
        f2 = self.A21[1] if self.rullist[0][1] == 0 else self.A22[1]
        f3 = self.B1 if self.rullist[0][2] == 0 else self.B2
        f12 = f1 * f2
        z = 6
        zr = 0
        for i in range(z):
            zr = round(f12 * f3[i], 4)
            fx.append(zr)
        self.B11 = fx
        print(self.rullist[0])
        print('prod=', round(f12, 3))
        print('y', f3)
        print('B11', fx)
        print(' ')

    def second(self):
        f1 = 0
        f2 = 0
        f3 = []
        f12 = 0
        fx = []
        f1 = self.A11[1] if self.rullist[1][0] == 0 else self.A12[1]
        f2 = self.A21[1] if self.rullist[1][1] == 0 else self.A22[1]
        f3 = self.B1 if self.rullist[1][2] == 0 else self.B2
        f12 = f1 * f2
        z = 6
        zr = 0
        for i in range(z):
            zr = round(f12 * f3[i], 4)
            fx.append(zr)
        self.B12 = fx
        print(self.rullist[0])
        print('prod= ', round(f12, 3))
        print('y', f3)
        print('B12', fx)
        print(' ')

    def third(self):
        f1 = 0
        f2 = 0
        f3 = []
        f12 = 0
        fx = []
        f1 = self.A11[1] if self.rullist[2][0] == 0 else self.A12[1]
        f2 = self.A21[1] if self.rullist[2][1] == 0 else self.A22[1]
        f3 = self.B1 if self.rullist[2][2] == 0 else self.B2
        f12 = f1 * f2
        z = 6
        zr = 0
        for i in range(z):
            zr = round(f12 * f3[i], 4)
            fx.append(zr)
        self.B21 = fx
        print(self.rullist[0])
        print('prod=', round(f12, 3))
        print('y', f3)
        print('B21', fx)
        print(' ')

    def fourth(self):
        f1 = 0
        f2 = 0
        f3 = []
        f12 = 0
        fx = []
        f1 = self.A11[1] if self.rullist[3][0] == 0 else self.A12[1]
        f2 = self.A21[1] if self.rullist[3][1] == 0 else self.A22[1]
        f3 = self.B1 if self.rullist[3][2] == 0 else self.B2
        f12 = f1 * f2
        z = 6
        zr = 0
        for i in range(z):
            zr = round(f12 * f3[i], 4)
            fx.append(zr)
        self.B22 = fx
        print(self.rullist[0])
        print('prod=', round(f12, 3))
        print('y', f3)
        print('B22', fx)
        print(' ')

    def max_sug(self):
        l = 6
        k = 0
        for i in range(6):
            k = max(self.B11[i], self.B12[i], self.B21[i], self.B22[i])
            self.B.append(k)
        print('Output system:', self.B)

    def counted(self):
        count = ((self.y[0] * self.B[0] + self.y[1] * self.B[1] + self.y[2] * self.B[2] + self.y[3] * self.B[3] +
                  self.y[4] * self.B[4] + self.y[5] * self.B[5])
                 / (self.B[0] + self.B[1] + self.B[2] + self.B[3] + self.B[4] + self.B[5]))
        print('Output Larsen:', round(count, 4))


if __name__ == '__main__':
    '''
    you need to enter x from 0<x<1: 0.2
    fill matrix: 0 0 0
    fill matrix: 0 1 0
    fill matrix: 1 0 1
    fill matrix: 1 1 1
    '''
    start = Larsen()
    start.x12()
    start.a11()
    start.a22()
    start.YB()
    start.regulations()
    start.first()
    start.second()
    start.third()
    start.fourth()
    start.max_sug()
    start.counted()

'''
X= [0.2, 0.8]

 x1 = [0, 0.2, 1]
A11 = [1, 0.8, 0]
A12 = [0, 0.2, 1]

 x2 = [0, 0.8, 1]
A21 = [1, 0.2, 0]
A22 = [0, 0.8, 1]

 y = [0, 0.2, 0.4, 0.6, 0.8, 1]
B1 = [1, 0.8, 0.6, 0.4, 0.2, 0]
B2 = [0, 0.2, 0.4, 0.6, 0.8, 1]

[[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1]]
[0, 0, 0]
prod= 0.16
y [1, 0.8, 0.6, 0.4, 0.2, 0]
B11 [0.16, 0.128, 0.096, 0.064, 0.032, 0.0]

[0, 0, 0]
prod=  0.64
y [1, 0.8, 0.6, 0.4, 0.2, 0]
B12 [0.64, 0.512, 0.384, 0.256, 0.128, 0.0]

[0, 0, 0]
prod= 0.04
y [0, 0.2, 0.4, 0.6, 0.8, 1]
B21 [0.0, 0.008, 0.016, 0.024, 0.032, 0.04]

[0, 0, 0]
prod= 0.16
y [0, 0.2, 0.4, 0.6, 0.8, 1]
B22 [0.0, 0.032, 0.064, 0.096, 0.128, 0.16]

Output system: [0.64, 0.512, 0.384, 0.256, 0.128, 0.16]
Output Larsen: 0.3231
'''
