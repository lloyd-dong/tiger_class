import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def a_fun(name, *a1, **kwargs):
    print(name)
    print(a1[0])
    print(kwargs.get("has_me", "not set"))
# a_fun("hi", "h2", "h3", is_me="abc")
# hi
# h2
# not set


# for p in zip(np.random.randint(0, 10, 3) * 10, np.random.randint(0, 10, 3) * 10):
#     print(p)
import numpy as np
from scipy.spatial.distance import pdist, squareform
import time
from numpy.random import default_rng


def poc():
    points = np.array([
        [0.5, 0.5],
        [-0.5, 0.5],
        [-0.2, 0.2]
    ])

    pm = [1.2, 1.2]
    dm = pdist(points, lambda p1, p2: np.sum(
        np.amin([(p1 - p2) ** 2, (pm - np.abs(p1 - p2)) ** 2], axis=0)))
    print(dm)

rnd = default_rng()

def once_lambda(points):
    pm = [1.2, 1.2]
    # dm = pdist(points, lambda p1, p2: np.sum(
    #     np.amin([(p1 - p2) ** 2, (pm - np.abs(p1 - p2)) ** 2], axis=0)))
    dm = pdist(points, lambda p1, p2: np.sum( (p1-p2)**2))


def once_ctype(points):
    dm = pdist(points, 'sqeuclidean')

row= 6
points = rnd.uniform(-0.6, 0.6, row*2).reshape(row,2)

start = time.time()
for i in range(10000):
    once_ctype(points)
end = time.time()
print(f"ctype: {end - start}")

start = time.time()
for i in range(10000):
    once_lambda(points)
end = time.time()
print(f"lambda: {end - start}")
