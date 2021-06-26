import matplotlib.pyplot as plt
from numpy.random import default_rng
from Animal import Animal, Vector
from Config import N, MAP_SCOPE, INIT_SPEED, RADIUS_REPEL, MAX_ITERATION, DELTA_T, RADIUS_ALIGNMENT


def alive_animals( animals :[] ) -> []:
    return [a for a in animals if a.alive]


def init_animals(sheep, wolves):
    rnd = default_rng()
    positions = [Vector(p[0], p[1]) for p in
                 zip(rnd.choice(int(MAP_SCOPE / RADIUS_REPEL), size=2 * N, replace=False) * RADIUS_REPEL,
                     rnd.uniform(0, MAP_SCOPE, 2 * N))]
    speed = [Vector(p[0], p[1]) for p in zip(rnd.uniform(0, INIT_SPEED, 2 * N),
                                             rnd.uniform(0, INIT_SPEED, 2 * N))]
    for i in range(N):
        sheep.append(Animal("sheep", i, pos=positions[i], speed=speed[i], shape="+"))
        # wolves.append(Animal("wolf", N + i, pos=positions[N + i], speed=speed[N + i], shape="D"))


def draw(animals):
    plt.figure(1)  # 选择图表1

    x = [s.pos.x for s in alive_animals(animals)]
    y = [s.pos.y for s in alive_animals(animals)]
    plt.scatter(x, y, marker=animals[0].shape)
    plt.show()


def unit_test():
    assert (Vector(0,3).distance( Vector(4,0)) ==5)

    # w1 = Animal("wolf", 1, pos= Vector(10,10), speed = Vector(3,1))
    # assert( w1.pos.x == 10 and w1.pos.y == 10)
    # w1.move(1)
    # assert( w1.pos.x == 13 and w1.pos.y == 11) given alignment effect, it's not

    v1 = Vector(1, 1)
    v2 = Vector(MAX_SCOPE -2, MAX_SCOPE -3)
    assert ( v1.distance(v2) == 5)

    print("all passed")