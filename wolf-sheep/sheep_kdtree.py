# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap

import numpy as np
from Animal import Animal, Vector
from Config import N, MAP_SCOPE, INIT_SPEED, RADIUS_REPEL
from until import draw

Sheep = []


def init():
    positions = [Vector(p[0], p[1]) for p in zip(np.random.randint(0, MAP_SCOPE/(2 * RADIUS_REPEL), 2 * N) * 2 * RADIUS_REPEL,
                                                 np.random.randint(0, MAP_SCOPE/(2 * RADIUS_REPEL), 2 * N) * 2 * RADIUS_REPEL)]
    speed = [Vector(p[0], p[1]) for p in zip(np.random.randint(0, INIT_SPEED, N),
                                            np.random.randint(0, INIT_SPEED, N))]
    for i in range(N):
        Sheep.append(Animal("sheep", i, pos=positions[i], speed=speed[i], shape="+"))
        # Wolves.append(Animal("wolf", N + i, pos=positions[N + i], speed=speed[i], shape="D"))


if __name__ == "__main__":
    init()
    draw(Sheep)
