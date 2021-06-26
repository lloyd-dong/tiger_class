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
Animals = []

def init():
    global alignment_tree

    util.init_animals(Sheep, Wolves)
    Animals.extend(Sheep)
    Animals.extend(Wolves)

    alignment_tree = Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)


if __name__ == "__main__":
    init()
    sheep_around_point = {}

    for i in range(100):
        sheep = util.alive_animals(Sheep)
        if i % 10 == 0:
            util.draw(sheep)
        sheep_pos = np.array( [(s.pos.x, s.pos.y) for s in sheep])
        nearby_points = alignment_tree.query(sheep_pos)[1]
        for idx, s in enumerate(sheep):
            s.set_alignment_points(nearby_points[idx])
            s._get_nearby_points(nearby_points[idx]) => array of 9 points
            sheep_around_point[nearby_points[idx]] = sheep_around_point.get(nearby_points[i], set()).add(s.id)

        for s in sheep:
            s.move(Config.DELTA_T, sheep_around_point)
