from itertools import product
from math import exp

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from numpy import typing as npt
from numpy.linalg import pinv
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import export_text

TypeN = np.float64
ND = npt.NDArray[TypeN]
MIN: float = 0
MAX: float = 10.1
STEP: float = 0.1


train_set: ND = np.array(
    [
        [-10, -10, 1],
        [-10, -5.5, 0],
        [-10, 0, 1],
        [-6.5, 0, 1],
        [-6.5, -4.5, 0],
        [0, -10, 0],
        [-3.5, -5, 1],
        [0, -5, 0],
        [0, 0, 0],
    ],
    dtype=TypeN,
)

test_set: ND = np.array(
    [
        [-10, -9, 1],
        [-10, -4.5, 0],
        [-10.5, -1, 1],
    ],
    dtype=TypeN,
)


def fii(c=None, sigma=None, x=None):
    func = 1
    for itr, num in enumerate(c):
        func *= exp(-((x[itr] - num) ** 2) / (2 * sigma[itr] ** 2))
    return func


def calc_group(W=None, centers=None, sigma=None, x=None):
    y = 0
    for b in range(len(W)):
        y += W[b] * fii(centers[b, :], sigma[b, :], x)
        y += W[b] * fii(centers[b, :], sigma[b, :], x)
    return y


def main() -> None:
    centers: ND = train_set[:, [0, 1]]
    x: ND = train_set[:, [0, 1]]
    T: ND = train_set[:, 2]

    sigma: ND = np.array(
        [
            [5, 3],
            [2, 1.5],
            [2, 4],
            [1.5, 2.5],
            [1.5, 2],
            [5, 3],
            [1.5, 2],
            [2, 2],
            [5, 3],
        ],
        dtype=TypeN,
    )

    xn = centers.shape
    cn = sigma.shape

    G = np.zeros((xn[0], cn[0]), dtype=TypeN)
    for a, b in product(range(xn[0]), range(cn[0])):
        G[a, b] = fii(centers[b, :], sigma[b, :], centers[a, :])

    Gplus = pinv(np.transpose(G) * G) * np.transpose(G)
    W = Gplus * T
    spivpad = 0
    nespivp = 0
    Y = np.zeros([xn[1], 1], dtype=TypeN)

    for a in range(xn[1]):
        tmp = calc_group(W, centers, sigma, centers[a, :])
        Y[a] = 1 if tmp > 0.5 else 0
        if Y[a] == T[a]:
            spivpad += 1
        else:
            nespivp += 1

    error1 = nespivp

    x = test_set[:, [0, 1]]
    T = test_set[:, 2]

    xn = x.shape
    spivpad = 0
    nespivp = 0
    Y = np.zeros([xn[0], 1], dtype=TypeN)
    for a in range(xn[0]):
        tmp = calc_group(W, centers, sigma, x[a])
        Y[a] = 1 if tmp > 0.5 else 0
        if Y[a] == T[a]:
            spivpad = spivpad + 1
        else:
            nespivp = nespivp + 1

    error2 = nespivp


def main1() -> None:
    iris = load_iris()
    x, y = iris.data, iris.target

    clf = tree.DecisionTreeClassifier()
    clf.fit(x, y)

    print(export_text(clf, feature_names=iris.feature_names))


if __name__ == "__main__":
    main()
