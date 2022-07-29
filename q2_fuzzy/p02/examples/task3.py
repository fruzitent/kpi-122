class Larsen(object):
    def __init__(self, p1=0, p2=0) -> None:
        self._p1 = p1
        self._p2 = p2
        self._b1 = [1, 0.8, 0.6, 0.4, 0.2, 0]
        self._b2 = [0, 0.2, 0.4, 0.6, 0.8, 1]
        self._y = [0, 0.2, 0.4, 0.6, 0.8, 1]
        self._rule_list = []
        self._star1 = []
        self._star2 = []
        self._star3 = []
        self._star4 = []
        self._total = []
        self._a11 = []
        self._a12 = []
        self._a21 = []
        self._a22 = []
        self._p11 = []
        self._p22 = []
        self._p = []

    def p12(self) -> None:
        while True:
            self._p1 = float(input("||>>Please, enter p1:"))
            if self._p1 >= 1 or self._p1 <= 0:
                print("||wrong input!! Please enter p1 between 0 and 1!")
            else:
                print("||>>p2=1-p1")
                break
        self._p2 = 1 - self._p1

    def point(self) -> None:
        self._p = [self._p1, self._p2]
        print("||P = ", self._p)

    def rules(self) -> None:
        print("||Please insert your rule list:")
        for i in range(4):
            self._rule_list.append([])
            for j in range(3):
                if j in [0, 1]:
                    print("||p", i + 1, ":")
                else:
                    print("||t", i + 1, ":")
                while True:
                    rule = int(input(">>"))
                    if rule in {0, 1}:
                        break
                    else:
                        print("||wrong input! Please enter 0 or 1!")
                self._rule_list[i].append(rule)
        print("||Your list of rules:", self._rule_list)

    def A11_A12(self) -> None:
        self._p11 = [0, self._p1, 1]
        self._a11 = [1, self._p2, 0]
        self._a12 = self._p11
        print("||p1  =", self._p11)
        print("||A11 =", self._a11)
        print("||A12 =", self._a12)

    def A21_A22(self) -> None:
        self._p22 = [0, self._p2, 1]
        self._a21 = [1, self._p1, 0]
        self._a22 = self._p22
        print("||p2  =", self._p22)
        print("||A21 =", self._a21)
        print("||A22 =", self._a22)

    def B1_B2(self) -> None:
        print("||y  =", self._y)
        print("||B1 =", self._b1)
        print("||B2 =", self._b2)

    def first_rule(self) -> None:
        f1 = self._a11[1] if self._rule_list[0][0] == 0 else self._a12[1]
        f2 = self._a21[1] if self._rule_list[0][1] == 0 else self._a22[1]
        f3 = self._b1 if self._rule_list[0][2] == 0 else self._b2
        f12 = f1 * f2
        fx = []
        z = 6
        for itr in range(z):
            zr = f12 * f3[itr]
            fx.append(zr)
        self._star1 = fx
        print("||For the first rule:")
        print(self._rule_list[0])
        print("alfa1 = ", f12)
        print("y", f3)
        print("Rule`s exit", fx)

    def second_rule(self) -> None:
        f1 = self._a11[1] if self._rule_list[1][0] == 0 else self._a12[1]
        f2 = self._a21[1] if self._rule_list[1][1] == 0 else self._a22[1]
        f3 = self._b1 if self._rule_list[1][2] == 0 else self._b2
        f12 = min(f1, f2)
        fx = []
        z = 6
        for itr in range(z):
            zr = f12 * f3[itr]
            fx.append(zr)
        self._star2 = fx
        print("||For the second rule:")
        print(self._rule_list[0])
        print("alfa2 = ", f12)
        print("y", f3)
        print("Rule`s exit", fx)

    def third_rule(self) -> None:
        f1 = self._a11[1] if self._rule_list[2][0] == 0 else self._a12[1]
        f2 = self._a21[1] if self._rule_list[2][1] == 0 else self._a22[1]
        f3 = self._b1 if self._rule_list[2][2] == 0 else self._b2
        f12 = f1 * f2
        fx = []
        z = 6
        for itr in range(z):
            zr = f12 * f3[itr]
            fx.append(zr)
        self._star3 = fx
        print("||For the third rule:")
        print(self._rule_list[0])
        print(">>alfa3 = ", f12)
        print(">>y", f3)
        print(">>Rule`s exit", fx)

    def fourth_rule(self) -> None:
        f1 = self._a11[1] if self._rule_list[3][0] == 0 else self._a12[1]
        f2 = self._a21[1] if self._rule_list[3][1] == 0 else self._a22[1]
        f3 = self._b1 if self._rule_list[3][2] == 0 else self._b2
        f12 = f1 * f2
        fx = []
        z = 6
        for itr in range(z):
            zr = f12 * f3[itr]
            fx.append(zr)
        self._star4 = fx
        print("||For the fourth rule:")
        print(self._rule_list[0])
        print(">>alfa4 = ", f12)
        print(">>y", f3)
        print(">>Rule`s exit", fx)

    def max(self) -> None:
        for itr in range(6):
            zzz = max(
                self._star1[itr], self._star2[itr], self._star3[itr], self._star4[itr]
            )
            self._total.append(zzz)
        print(self._total)

    def answer(self) -> None:
        lf = (self._y[itr] * self._total[itr] for itr in range(6))
        res = sum(lf) / sum(self._total)
        print("||The final answer is: ", res)


def main() -> None:
    task = Larsen()
    task.p12()
    task.point()
    task.A11_A12()
    task.A21_A22()
    task.B1_B2()
    task.rules()
    task.first_rule()
    task.second_rule()
    task.third_rule()
    task.fourth_rule()
    task.max()
    task.answer()
    input("||Press any key to exit")


if __name__ == "__main__":
    main()
