from math import exp

import numpy as np
from numpy.linalg import inv


def print_list(arr):
    for itr in arr:
        print(itr)


def fii(c, sigma, x):
    p = 1
    for itr, num in enumerate(c):
        p *= exp(-((x[itr] - num) ** 2) / (sigma[itr] ** 2))
    return p


def main() -> None:
    with open("./c.dat") as f:
        c = [[float(j) for j in i.split(", ")] for i in f]
    with open("./sigma.dat") as f:
        sigma = [[float(j) for j in i.split(", ")] for i in f]
    with open("./data.dat") as f:
        data = [[float(j) for j in i.split(", ")] for i in f]
    with open("./test.dat") as f:
        test = [[float(j) for j in i.split(", ")] for i in f]

    x = [[i[0], i[1]] for i in data]
    y = [i[2] for i in data]

    f = []
    for i in range(len(y)):
        f.append([])
        for j in range(len(c)):
            f[i].append(fii(c[j], sigma[j], x[i]))

    ft = np.array(f)
    f = np.array(f)
    ft = ft.transpose()
    fa = np.dot(ft, f)
    fa = inv(fa)
    w = np.dot(np.dot(fa, ft), y)

    y1 = [round(sum(f[i][j] * w[j] for j in range(len(c))), 3) for i in range(len(y))]

    print("На множині навчання отримали такі значення класів:", y1)

    x = [[i[0], i[1]] for i in test]
    y = [i[2] for i in test]

    f = []
    for i in range(len(y)):
        f.append([])
        for j in range(len(c)):
            f[i].append(fii(c[j], sigma[j], x[i]))

    y1 = [round(sum(f[i][j] * w[j] for j in range(len(c))), 3) for i in range(len(y))]
    err = sum(abs(y[i] - y1[i]) for i in range(len(y)))

    print("На множині тестування отримали такі значення класів:", [str(i) for i in y1])
    print("Похибка: ", err)


if __name__ == "__main__":
    main()
