# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap

import util
import Config
import numpy as np
from Grid import Grid

Sheep = []
Wolves = []


def init():
    global alignment_grid
    util.init_animals(Sheep, Wolves)
    alignment_grid = Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)


if __name__ == "__main__":
    init()
    sheep_around = {}

    for i in range(100):
        sheep = util.alive_animals(Sheep)
        if i % 10 == 0:
            util.draw(sheep)

        alignment_grid.update_pos([(s.pos.x, s.pos.y) for s in sheep])
        for idx, s in enumerate(sheep):
            closest_point, nearby_points = alignment_grid.get_closest_and_nearby(s.pos, idx)
            s.set_alignment_points(closest_point, nearby_points)
            sheep_around[closest_point] = sheep_around.get(closest_point, set()).add(s)

        for s in sheep:
            s.move(Config.DELTA_T, sheep_around)
