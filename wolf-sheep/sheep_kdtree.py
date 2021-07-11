# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap

import numpy as np
import util
import Config
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Grid

Sheep = []
Wolves = []
Animals = []
Alignment_Grid: Grid.Grid = None
Chase_Grid: Grid.Grid = None
particles = None


def init():
    global particles, Alignment_Grid, Chase_Grid
    util.init_animals(Sheep, Wolves)
    Animals.extend(Wolves)
    Animals.extend(Sheep)
    Alignment_Grid = Grid.Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)
    Chase_Grid = Grid.Grid(Config.RADIUS_SIGHT, Config.MAP_SCOPE)

    p = np.array([[s.pos.x, s.pos.y] for s in Animals])
    particles.set_data(p.T)
    return particles,


def animate(i: int):
    global fig, ax, particles, Animals
    for _ in range(Config.PACE):
        Alignment_Grid.update_index(Animals)
        Chase_Grid.update_index(Animals)
        for a in Animals:
            a.move(Config.DELTA_T, Alignment_Grid, Chase_Grid)
        Animals = util.alive_animals(Animals)

    p = np.array([[s.pos.x, s.pos.y] for s in Animals])
    particles.set_data(p.T)
    particles.set_markersize(4)
    return particles,


def main():
    global fig, ax, particles
    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=(0, Config.MAP_SCOPE), ylim=(0, Config.MAP_SCOPE))
    particles, = ax.plot([], [], '+', ms=6)

    ani = animation.FuncAnimation(fig, animate, frames=int(Config.MAX_ITERATION / Config.PACE),
                            repeat=False, interval=100, blit=True, init_func=init)
    plt.show()


def _debug():
    global fig, ax, particles, Animals, Alignment_Grid, Chase_Grid
    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=(0, Config.MAP_SCOPE), ylim=(0, Config.MAP_SCOPE))
    particles, = ax.plot([], [], '+', ms=6)

    init()
    for _ in range(Config.PACE):
        Alignment_Grid.update_index(Animals)
        Chase_Grid.update_index(Animals)
        for a in Animals:
            a.move(Config.DELTA_T, Alignment_Grid, Chase_Grid)
        Animals = util.alive_animals(Animals)

if __name__ == "__main__":
    main()
