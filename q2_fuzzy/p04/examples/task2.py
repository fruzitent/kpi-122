from math import pi
import numpy as np
import matplotlib.pyplot as plt


def train(x, y, size, n_h=3, num_it=150, rate=0.1):
    m = x.shape[0]
    costs = []
    w1 = np.random.rand(size, n_h)
    w2 = np.random.rand(n_h, size)
    for _ in range(num_it):
        z1 = np.dot(x, w1)
        a1 = np.tanh(z1)
        z2 = np.dot(a1, w2)
        cost = np.sum(np.power((y - z2), 2)) / (2 * size)
        costs.append(cost)
        dz2 = (y - z2) / size
        dw2 = 1 / m * (np.dot(a1.T, dz2))
        dz1 = np.dot(dz2, w2.T) * (1 - np.power(a1, 2))
        dw1 = 1 / m * (np.dot(x.T, dz1))
        w1 += rate * dw1
        w2 += rate * dw2
    plt.plot(costs, marker="o")
    plt.show()
    return {"w1": w1, "w2": w2}


def predict(x, parameters, size):
    z1 = np.dot(x, parameters["w1"])
    a1 = np.tanh(z1)
    z2 = np.dot(a1, parameters["w2"])
    for itr in range(size):
        print(f"{x[0][itr]}: -> {z2[0][itr]}")
    return z2


def approx(x):  # функція апроксимації
    return x * np.sin(x)


def main():  # x*sin(x) [0; pi]
    size: int = 5
    x_tr = np.array([itr * 2 * pi / size for itr in range(size)])[np.newaxis]
    y_tr = np.array([approx(itr) for itr in x_tr])
    parameters = train(x_tr, y_tr, size)
    y_pred = predict(x_tr, parameters, size)

    fig = plt.figure()
    ax1 = fig.add_subplot(131, polar=False)
    ax1.patch.set_facecolor("gray")
    ax1.plot(x_tr, y_tr, "ok")
    ax1.legend(["data"], loc="best")
    ax1.plot(x_tr[0], y_tr[0], "w")
    ax1.set_title("FUNCTION")
    ax1.set_xlabel("Ось x")
    ax1.set_ylabel("Ось t")
    ax1.grid(True)

    ax2 = fig.add_subplot(133, polar=False)
    ax2.patch.set_facecolor("gray")
    ax2.plot(x_tr, y_pred, "vr")
    ax2.legend(["data"], loc="best")
    ax2.plot(x_tr[0], y_pred[0], "w")
    ax2.set_title("FUNCTION APPROXIMATION")
    ax2.set_xlabel("Ось x")
    ax2.set_ylabel("Ось y")
    ax2.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
