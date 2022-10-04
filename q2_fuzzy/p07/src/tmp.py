import random

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

DATA_SIZE: int = 1000
EPOCH: int = 50
CLUSTERS: int = 4


def compute_l2_distance(x, centroid):
    return ((x - centroid) ** 2).sum(axis=x.ndim - 1)


def get_closest_centroid(x, centroids):
    dist = compute_l2_distance(x, centroids)
    return np.argmin(dist, axis=1)


def compute_sse(data, centroids, assigned_centroids):
    return compute_l2_distance(data, centroids[assigned_centroids]).sum() / len(data)


def main() -> None:
    data1 = np.random.normal([5, 5, 5], [4, 4, 4], [DATA_SIZE, 3])
    data2 = np.random.normal([4, 20, 20], [3, 3, 3], [DATA_SIZE, 3])
    data3 = np.random.normal([25, 20, 5], [5, 5, 5], [DATA_SIZE, 3])
    data4 = np.random.normal([30, 30, 30], [5, 5, 5], [DATA_SIZE, 3])
    data = np.concatenate((data1, data2, data3, data4), axis=0)
    np.random.shuffle(data)

    random.seed(0)

    centroids = data[random.sample(range(data.shape[0]), 4)]
    assigned_centroids = np.zeros(len(data), dtype=np.int32)

    num_centroid_dims = data.shape[1]
    sse_list = []

    for _ in range(50):
        assigned_centroids = get_closest_centroid(
            data[:, None, :],
            centroids[None, :, :],
        )

        for c in range(centroids.shape[1]):
            cluster_members = data[assigned_centroids == c]
            cluster_members = cluster_members.mean(axis=0)
            centroids[c] = cluster_members

        sse = compute_sse(data.squeeze(), centroids.squeeze(), assigned_centroids)
        sse_list.append(sse)

    fig = plt.figure()
    ax = fig.add_subplot(projection=Axes3D.name)

    for c, _ in enumerate(centroids):
        cluster_members = np.array(
            [data[i] for i in range(len(data)) if assigned_centroids[i] == c],
            dtype=TypeN,
        )

        ax.scatter(
            cluster_members[:, 0],
            cluster_members[:, 1],
            cluster_members[:, 2],
            s=0.5,
        )

    plt.figure()
    plt.xlabel("Iterations")
    plt.ylabel("SSE")
    plt.plot(range(len(sse_list)), sse_list)
    plt.show()
