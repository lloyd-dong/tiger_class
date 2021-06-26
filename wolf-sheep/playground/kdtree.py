import numpy as np
from scipy import spatial
x, y = np.mgrid[0:5, 2:8]
tree = spatial.KDTree(list(zip(x.ravel(),y.ravel())))
# print(tree.data)
pts = np.array([[0,0], [2.1, 2.9]])
r1 = tree.query(pts)

r2 = tree.query(pts[1])
r3 = tree.query(pts[1], k=10, distance_upper_bound=1)
pass