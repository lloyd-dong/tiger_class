import numpy as np


def a_fun(name, **kwargs):
    print(name)
    print(kwargs.get("has_me", "not set"))


# a_fun("hi", is_me="abc")

for p in zip(np.random.randint(0, 10, 3) * 10, np.random.randint(0, 10, 3) * 10):
    print(p[0])