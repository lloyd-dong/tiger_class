import math

import matplotlib.pyplot as plt
from numpy.random import default_rng
from Animal import Animal
from Vector import Vector
import Config
from Grid import Grid


def alive_animals(animals: []) -> []:
    return [a for a in animals if a.alive]


def init_animals(sheep, wolves):
    rnd = default_rng()
    positions = [Vector(p[0], p[1]) for p in
                 zip(rnd.choice(int(Config.MAP_SCOPE/ Config.RADIUS_REPEL), size=2 * Config.N, replace=False)
                     * Config.RADIUS_REPEL,
                     rnd.uniform(0, Config.MAP_SCOPE, 2 * Config.N))]
    speed = [Vector(Config.INIT_SPEED, p) for p in rnd.uniform(0, 2 * math.pi, 2 * Config.N)]
    for i in range(Config.N):
        wolves.append(Animal("wolf", i, pos=positions[i], speed=speed[i], shape="D"))
        sheep.append(Animal("sheep", Config.N + i, pos=positions[Config.N + i], speed=speed[Config.N + i], shape="+"))


def draw(animals):
    plt.figure(1)  # 选择图表1
    x = [s.pos.x for s in alive_animals(animals)]
    y = [s.pos.y for s in alive_animals(animals)]
    plt.scatter(x, y, marker=animals[0].shape)
    plt.show()


def init_alignment_grid():
    global Alignment_Grid
    Alignment_Grid = Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)


def update_alignment(animals:[Animal]):
    Alignment_Grid.find_nearby_grid([(s.pos.x, s.pos.y) for s in animals])
    for idx, s in enumerate(animals):
        closest_point, nearby_points = Alignment_Grid.get_closest_and_nearby(s.pos, idx)
        s.set_alignment_points(closest_point, nearby_points)
        if closest_point not in Config.Sheep_Around:
            Config.Sheep_Around[closest_point] = set()
        Config.Sheep_Around[closest_point].add(s)

Alignment_Grid:Grid = None
