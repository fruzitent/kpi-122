import numpy as np
import matplotlib.pyplot as plt


def rbf(x, c, s):
    return np.exp(-1 / (2 * s**2) * (x - c) ** 2)


def fcm(X, k):
    clusters = np.random.choice(np.squeeze(X), size=k)
    prevClusters = clusters.copy()
    stds = np.zeros(k)
    converged = False

    while not converged:
        distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))
        closestCluster = np.argmin(distances, axis=1)
        for i in range(k):
            pointsForCluster = X[closestCluster == i]
            if len(pointsForCluster) > 0:
                clusters[i] = np.mean(pointsForCluster, axis=0)
        converged = np.linalg.norm(clusters - prevClusters) < 1e-6
        prevClusters = clusters.copy()

    distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))
    closestCluster = np.argmin(distances, axis=1)
    clustersWithNoPoints = []

    for i in range(k):
        pointsForCluster = X[closestCluster == i]
        if len(pointsForCluster) < 2:
            clustersWithNoPoints.append(i)
            continue
        else:
            stds[i] = np.std(X[closestCluster == i])

    if clustersWithNoPoints:
        pointsToAverage = [
            X[closestCluster == i] for i in range(k) if i not in clustersWithNoPoints
        ]

        pointsToAverage = np.concatenate(pointsToAverage).ravel()
        stds[clustersWithNoPoints] = np.mean(np.std(pointsToAverage))

    return clusters, stds


class RBFNet(object):
    def __init__(self, k=2, lr=0.01, epochs=100, rbf=rbf, infer_stds=True):
        self.k = k
        self.lr = lr
        self.epochs = epochs
        self.rbf = rbf
        self.inferStds = infer_stds
        self.w = np.random.randn(k)
        self.b = np.random.randn(1)

    def fit(self, X, y):
        if self.inferStds:
            self.centers, self.stds = fcm(X, self.k)
        else:
            self.centers, _ = fcm(X, self.k)
            dMax = max(np.abs(c1 - c2) for c1 in self.centers for c2 in self.centers)
            self.stds = np.repeat(dMax / np.sqrt(2 * self.k), self.k)

        for _ in range(self.epochs):
            for i in range(X.shape[0]):
                a = np.array(
                    [self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)]
                )
                F = a.T.dot(self.w) + self.b
                loss = (y[i] - F).flatten() ** 2
                print("Loss: {0:.2f}".format(loss[0]))
                error = -(y[i] - F).flatten()
                self.w = self.w - self.lr * a * error
                self.b = self.b - self.lr * error

    def predict(self, X):
        y_pred = []
        for i in range(X.shape[0]):
            a = np.array(
                [self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)]
            )
            F = a.T.dot(self.w) + self.b
            y_pred.append(F)
        return np.array(y_pred)


def main() -> None:
    NUM_SAMPLES = 200
    x = np.sort(np.random.uniform(0, 1, NUM_SAMPLES))
    y = np.cos(np.pi * 4 * x) + x**3
    rbfnet = RBFNet(lr=1e-2, k=2, infer_stds=True)
    rbfnet.fit(x, y)
    y_pred = rbfnet.predict(x)

    plt.plot(x, y, "-o", label="true")
    plt.plot(x, y_pred, "-o", label="RBF-Net")
    plt.tight_layout()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
