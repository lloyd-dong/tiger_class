# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap

import numpy as np
from numpy.random import default_rng
from Animal import Animal, Vector
from Config import N, MAP_SCOPE, INIT_SPEED, RADIUS_REPEL, MAX_ITERATION, DELTA_T
from until import draw, alive_animals

Sheep = []


def init():
    rnd = default_rng()
    positions = [Vector(p[0], p[1]) for p in
                 zip(rnd.choice(int(MAP_SCOPE / RADIUS_REPEL), size=2 * N, replace=False) * RADIUS_REPEL,
                     rnd.uniform(0, MAP_SCOPE, 2 * N))]
    speed = [Vector(p[0], p[1]) for p in zip(np.random.randint(0, INIT_SPEED, N),
                                             np.random.randint(0, INIT_SPEED, N))]
    for i in range(N):
        Sheep.append(Animal("sheep", i, pos=positions[i], speed=speed[i], shape="+"))
        # Wolves.append(Animal("wolf", N + i, pos=positions[N + i], speed=speed[i], shape="D"))


if __name__ == "__main__":
    init()
    for i in range(100):
        if i % 10 == 0:
            draw(Sheep)
        for s in alive_animals(Sheep):
            s.move(DELTA_T)
