import random
import itertools
from math import exp

from matplotlib import pyplot as plt


def log_sig(x):
    return 1 / (1 + exp(-x))


def mult(v1, v2):
    return sum(v1[itr] * v2[itr] for itr in range(len(v1)))


def main() -> None:
    s_1 = 2
    # HIDDEN NEURONS
    S1 = s_1
    S2 = 1
    p = []
    t = []  # input-output
    lr = 0.01
    for i in itertools.count(start=-1.5, step=0.25):
        if i > 0:
            break
        p.append(i)
        t.append(i**2)

    rab = len(p)
    W10 = []
    B10 = []
    W20 = []
    for i in range(0, S1):
        arr = random.uniform(-1, 1)  # випадкове дійсне число від -1 до1
        W10.append(arr)
        arr = random.uniform(-1, 1)
        B10.append(arr)
        W20.append(arr)
    B20 = random.uniform(-1, 1)
    err_goal = 0.01  # 1e-2=0.01
    epoch = 0
    s_error = 2
    e = []
    while epoch < 500000:  # (s_error)>1e-2
        s_error = 0
        for k in range(0, rab):
            A0 = p[k]
            A1 = []
            for i in range(0, S1):
                arr = W10[i] * A0 + B10[i]
                A1.append(log_sig(arr))
            # print(A1)
            A2 = mult(W20, A1) + B20  # purelin()
            if epoch == 0:
                e.append(t[k] - A2)
            else:
                e[k] = t[k] - A2
            r = []
            for i in range(0, S1):
                r.append([0, 0])  # range(0,S1)
            for i in range(0, S1):
                r[i][i] = (1 - A1[i]) * A1[i]
            ss2 = (-2) * 1 * e[k]
            ss1 = []
            for i in range(0, S1):
                arr = r[i][i] * W20[i] * ss2
                ss1.append(arr)
            W21 = []
            for i in range(0, S1):
                arr = W20[i] - lr * ss2 * A1[i]

                W21.append(arr)
            B21 = B20 - lr * ss2
            W11 = []
            B11 = []
            for i in range(0, S1):
                arr = W10[i] - lr * ss1[i] * A0
                W11.append(arr)
                arr = B10[i] - lr * ss1[i]
                B11.append(arr)
            W10 = W11
            B10 = B11
            W20 = W21
            B20 = B21
        epoch += 1
        s_error += sum(e[0:rab])
    print(s_error, epoch)
    y = []
    for k in range(0, rab):
        pp = p[k]
        A1 = []
        u = []
        for i in range(0, S1):
            arr = W10[i] * pp + B10[i]
            u.append(arr)
            arr = log_sig(u[i])
            A1.append(arr)
        y.append(mult(W20, A1) + B20)
    fig = plt.figure()
    ax1 = fig.add_subplot(131, polar=False)
    rect = ax1.patch
    rect.set_facecolor("gray")
    ax1.plot(p, t, "ok")
    ax1.legend(["data"], loc="best")
    ax1.plot(p, t, "w")
    ax1.set_title("FUNCTION")
    ax1.set_xlabel("Ось x")
    ax1.set_ylabel("Ось t")
    ax1.grid(True)
    ax2 = fig.add_subplot(133, polar=False)
    rect = ax2.patch
    rect.set_facecolor("gray")
    ax2.plot(p, y, "vr")
    ax2.legend(["data"], loc="best")
    ax2.plot(p, y, "w")
    ax2.set_title("FUNCTION APPROXIMATION")
    ax2.set_xlabel("Ось x")
    ax2.set_ylabel("Ось y")
    ax2.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
