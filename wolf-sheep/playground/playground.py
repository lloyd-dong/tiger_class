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

