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
from scipy.spatial.distance import pdist, squareform, cdist
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
    row = points.marker[0]
    # dm = pdist(points, lambda p1, p2: np.sum(
    #     min( (p1[0] - p2[0])**2, (pm - abs(p1[1] - p2[1])) **2 ),
    #     np.amin([(p1 - p2) ** 2, (pm - np.abs(p1 - p2)) ** 2], axis=0))
    #            )
    dm_x = pdist(list(zip(points[:, 0], np.zeros(row))), lambda p0, p1: np.sum(np.amin([(p0-p1)**2, (boundary -abs(p0-p1))**2], axis=0)))
    dm_y = pdist(list(zip(points[:, 1], np.zeros(row))), lambda p0, p1: np.sum(np.amin([(p0-p1)**2, (boundary -abs(p0-p1))**2], axis=0)))
    return dm_x + dm_y
    # dm = pdist(points, lambda p1, p2: np.sum( (p1-p2)**2))


def once_ctype(points):
    dm = pdist(points, 'sqeuclidean')

piont_number = 20
boundary = 2.0
points = rnd.uniform(0, boundary, piont_number * 2).reshape(piont_number,2)



def square_distance(p1, p2):
    x_dis = abs(p1[0] - p2[0])
    y_dis = abs(p1[1] - p2[1])
    return (min(x_dis, boundary - x_dis) ** 2 +
            min(y_dis, boundary - y_dis) ** 2)

def test_cdist():
    points = np.array([[1, 0.1], [1, 1.8], [0.1, 1], [1.8, 1]])
    dm = cdist([[0,0]],points,square_distance)
    pass

def test_periodic_dist():
    points = np.array([[1, 0.1], [1, 1.8], [0.1, 1], [1.8, 1]])
    dm = once_lambda(points)
    print(dm)
    dm_2 = pdist(points, square_distance)
    # assert( dm == dm_2)

    points = np.array([[0.1, 0.1], [1.8, 0.1], [1.8, 1.8]])
    dm = once_lambda(points)
    print(dm)
    dm_2 = pdist(points, square_distance)
    pass


def perform_test():
    ROUND=1000
    start = time.time()
    for i in range(ROUND):
        once_ctype(points)
    c_end = time.time() -start
    print(f"ctype: {c_end}")

    start = time.time()
    for i in range(ROUND):
        once_lambda(points)
    l_end = time.time() - start
    print(f"lambda: {l_end}, times: {l_end/c_end}")

    start = time.time()
    for i in range(ROUND):
        odm = pdist(points, square_distance)
    s_end = time.time() - start
    print(f"squre: {s_end}, times: {s_end/c_end}")

# test_periodic_dist()
# perform_test()

def iter_in_scope():
    radius = 0.5
    D = squareform(pdist(points, square_distance))
    ind1, ind2 = np.where(D < radius)
    unique = (ind1 < ind2)
    ind1 = ind1[unique]
    ind2 = ind2[unique]
    print(f"found {len(ind1)} pair of points")
    # for i1, i2 in zip(ind1, ind2):
    #     print(f" {i1}:{i2},  {points[i1]} , {points[i2]}, dist : {D[i1,i2]}")

    D = squareform(pdist(points, 'sqeuclidean'))
    ind1, ind2 = np.where(D < radius)
    unique = (ind1 < ind2)
    ind1 = ind1[unique]
    ind2 = ind2[unique]
    print(f"found {len(ind1)} pair of points")


# iter_in_scope()
test_cdist()