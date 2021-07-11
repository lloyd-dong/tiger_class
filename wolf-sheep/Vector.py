import Config
import numpy as np
from math import cos, sin, sqrt


class Vector:
    def __init__(self, x, y, max_scope=Config.MAP_SCOPE):
        self.x = x
        self.y = y
        self.max_scope = max_scope

    def change_direction(self, degree):
        theta = np.deg2rad(degree)
        rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
        self.x, self.y = np.dot(rot, [self.x, self.y])

    def square_distance(self, another_one):
        x_dis = abs(self.x - another_one.x)
        y_dis = abs(self.y - another_one.y)
        return (min(x_dis, self.max_scope - x_dis) ** 2 +
                min(y_dis, self.max_scope - y_dis) ** 2)

    def distance(self, another_one):
        return sqrt(self.square_distance(another_one))

    def move(self, speed, delta_t: float) -> None:  # speed is also a vector
        # self.x = (self.x + speed.x * delta_t) % self.max_scope  # periodic boundary
        # self.y = (self.y + speed.y * delta_t) % self.max_scope  # periodic boundary
        self.x = (self.x + speed.x * cos(speed.y) * delta_t) % self.max_scope  # periodic boundary
        self.y = (self.y + speed.x * sin(speed.y) * delta_t) % self.max_scope  # periodic boundary
