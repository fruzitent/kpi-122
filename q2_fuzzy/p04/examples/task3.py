from dataclasses import dataclass
from math import exp, pi, sin
from pathlib import Path
from random import uniform

import numpy as np
from matplotlib import pyplot as plt


@dataclass
class PrintGraph(object):
    x1: str = "input"
    x2: str = "input"
    x3: str = "input1"
    x4: str = "input1"
    y1: str = "Target"
    y2: str = "Target - *"
    y3: str = "mu"
    y4: str = "Target - *"
    title1: str = "function"
    title2: str = "approximation"
    title3: str = "function"
    title4: str = "approximation"

    def print_g(self, p, t, y) -> None:
        fig, ax = plt.subplots()

        plt.subplot(121)
        plt.plot(p, t, color="blue", marker="o")
        plt.title(self.title1)
        plt.xlabel(self.x1)
        plt.ylabel(self.y1)

        plt.subplot(122)
        plt.plot(p, y, color="red", marker="o")
        plt.title(self.title2)
        plt.xlabel(self.x2)

        plt.show()

    def print_n(self, p, t, y, s1) -> None:
        fig, ax = plt.subplots()

        plt.subplot(211)
        for k1 in range(int(s1)):
            plt.plot(p, y[k1], color="blue", linestyle="-", label="sin(x)")
        plt.title(self.title3)
        plt.ylabel(self.y3)

        plt.subplot(212)
        plt.plot(p, t, color="red", linestyle="--", marker="o")
        plt.title(self.title4)
        plt.xlabel(self.x4)
        plt.ylabel(self.y4)

        plt.show()


class Neuron(object):
    def __init__(self, s1: float, npts: float, freq: float, phase: float) -> None:
        self._epoch = 0
        self._err_goal = 1e-3
        self._lr = 0.02
        self._res = 0
        self._res1 = 0
        self._rg = [-1.0, 1.0]
        self.freq = freq
        self.npts = npts
        self.phase = phase
        self.s1 = s1
        self.T = []
        self._c = [0 for _ in range(int(self.s1))]
        self._sigma = [0 for _ in range(int(self.s1))]
        self._d1 = (self._rg[1] - self._rg[0]) / (self.npts - 1.0)
        self._p1 = np.arange(self._rg[0], self._rg[1] + 1e-15, self._d1)
        self._sizeP = np.size(self._p1)
        self._w = [uniform(-1, 1) for _ in range(int(self.s1))]
        self._sizeP_e = 0
        self._f = [[0 for _ in range(int(self.s1))] for _ in range(self._sizeP)]
        self._y = [0 for _ in range(int(self._sizeP))]
        self._total = self._rg[1] - self._rg[0]
        self._p2 = np.arange(self._rg[0], self._rg[1] + 1e-15, (self._total / 25))
        self._sizePl1 = np.size(self._p2)
        self._t1 = [0 for _ in range(int(self._sizePl1))]
        self._yy = [[0 for _ in range(int(self._sizePl1))] for _ in range(int(self.s1))]

    def array_t(self) -> None:
        for keyP in self._p1:
            val = 2 * pi * (self.freq * keyP + self.phase / 360)
            self.T.append(sin(val) + 1)

    def array_c_and_sigma(self) -> None:
        i = 0
        while i < self.s1:
            self._c[i] = self._p1[i]
            self._sigma[i] = 3 * self._d1
            i += 1

    def count_f_w(self) -> None:
        while self._epoch < 10**6 or s > 10 ** (-3):
            s = 0
            u = [[0 for _ in range(int(self.s1))] for _ in range(self._sizeP)]
            for k1 in range(self._sizeP):
                e = 0
                for k2 in range(int(self.s1)):
                    self._sizeP_e = ((self._p1[k1] - self._c[k2]) ** 2) / (
                        self._sigma[k2] ** 2
                    )
                    u[k1][k2] += self._sizeP_e
                    self._f[k1][k2] = exp(-0.5 * u[k1][k2])
                    e += self._w[k2] * self._f[k1][k2]
                self._y[k1] = e
                s += (e - self.T[k1]) ** 2
                s /= self._sizeP
                self._epoch += 1
            if (s < self._err_goal) or (self._epoch > 10**6):
                break
            de_dc = [[0 for _ in range(int(self.s1))] for _ in range(int(self.s1))]
            de_dsig = [[0 for _ in range(int(self.s1))] for _ in range(int(self.s1))]
            de_dw = [[0 for _ in range(int(self.s1))] for _ in range(int(self.s1))]
            for k2 in range(int(self.s1)):
                for k1 in range(self._sizeP):
                    self._sizeP_e = self._y[k1] - self.T[k1]
                    de_dc[k2][0] += (
                        self._sizeP_e
                        * self._w[k2]
                        * exp(-0.5 * u[k1][k2])
                        * ((self._p1[k1] - self._c[k2]) / (self._sigma[k2] ** 2))
                    )
                    de_dsig[k2][0] += (
                        self._sizeP_e
                        * self._w[k2]
                        * exp(-0.5 * u[k1][k2])
                        * ((self._p1[k1] - self._c[k2]) ** 2 / (self._sigma[k2] ** 3))
                    )
                    de_dw[k2][0] += self._sizeP_e * exp(-0.5 * u[k1][k2])
            for k1 in range(int(self.s1)):
                self._c[k1] -= self._lr * de_dc[k1][0]
                self._sigma[k1] -= self._lr * de_dsig[k1][0]
                self._w[k1] -= self._lr * de_dw[k1][0]

    def choice_res(self) -> float:
        y = np.dot(self._f, self._w)
        e = [0 for _ in range(np.size(y))]
        for i in range(np.size(y)):
            e[i] = (y[i] - self.T[i]) ** 2
        return np.sum(e) / 12

    def choice_res1(self):
        for k1 in range(int(self.s1)):
            for i in range(int(self._sizePl1)):
                val = -0.5 * (self._p2[i] - self._c[k1]) ** 2 / (self._sigma[k1] ** 2)
                self._yy[k1][i] = exp(val)
        Y1 = np.dot(self._w, self._yy)
        for i in range(int(self._sizePl1)):
            val = 2 * pi * (self.freq * self._p2[i] + self.phase / 360)
            self._t1[i] = sin(val) + 1
        return (np.sum(Y1 - self._t1)) ** 2 / self._sizePl1

    def show(self, res, res1, p2) -> None:
        print(f"{res=}")
        print(f"{res1=}")
        print(f"{p2=}")
        print(f"{self._c=}")
        print(f"{self._sigma}")
        print(f"{self._w=}")

    def save_to_file(self, filename: Path | str) -> None:
        with open(filename, "a") as txt_file:
            txt_file.write(f"res   = {self._res}\n")
            txt_file.write(f"res1  = {self._res1}\n")
            txt_file.write(f"p2    = {self._p2}\n")
            txt_file.write(f"c     = {self._c}\n")
            txt_file.write(f"sigma = {self._sigma}\n")
            txt_file.write(f"w     = {self._w}\n\n\n")

    def build(self) -> None:
        self.array_t()
        self.array_c_and_sigma()
        self.count_f_w()
        self._res = self.choice_res()
        self._res1 = self.choice_res1()
        self.show(self._res, self._res1, self._p2)

        pr = PrintGraph()
        pr.print_g(self._p1, self.T, self._y)
        pr.print_n(self._p2, self._t1, self._yy, self.s1)


class Menu:
    @staticmethod
    def read_from_file(filename):
        with open(filename) as f:
            return [[float(x) for x in line.split()] for line in f]

    def show_menu(self) -> None:
        while True:
            print("click 1 to input data")
            print("click 2 to read data")
            print("click 3 to exit")
            choice = int(input("choice = "))
            if choice == 1:
                s1 = float(input("s1 = "))
                npts = float(input("npts = "))
                freq = float(input("freq = "))
                phase = float(input("phase = "))
                neuron1 = Neuron(s1, npts, freq, phase)
                neuron1.build()
                print("input 1 if you wont save to file")
                print("input other value if you don't wont save to file")
                choice = int(input("choice = "))
            if choice == 1:
                neuron1.save_to_file("./saveZavd.txt")
            if choice == 2:
                data = self.read_from_file("./nachZnach.txt")
                print(data)
                neuron2 = Neuron(data[0][0], data[0][1], data[0][2], data[0][3])
                neuron2.build()
                print("input 1 if you wont save to file")
                print("input other value if you don't wont save to file")
                choice = int(input("choice = "))
                if choice == 1:
                    neuron2.save_to_file("./saveZavd.txt")
            if choice not in [1, 2]:
                raise SystemExit(1)


def main() -> None:
    menu = Menu()
    menu.show_menu()
    # 1: 5 5 0.5 60


if __name__ == "__main__":
    main()
