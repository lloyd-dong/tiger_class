# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap
import time

import numpy as np

import util
import Config
import Animal
import matplotlib.pyplot as plt
import matplotlib.animation as animation


Sheep = []
Wolves = []


def init():
    global particles
    util.init_animals(Sheep, Wolves)
    util.init_alignment_grid()
    p = np.array([[s.pos.x, s.pos.y] for s in util.alive_animals(Sheep)])
    particles.set_data(p.T)
    return particles,


def animate(i :int):
    global fig, ax, particles
    sheep = util.alive_animals(Sheep)
    util.update_alignment(sheep)
    for s in sheep:
        s.move(Config.DELTA_T)
    util.Sheep_Around = {}
    Animal.Distance_Map = {}
    p = np.array([[s.pos.x, s.pos.y] for s in util.alive_animals(Sheep)])
    particles.set_data(p.T)
    particles.set_markersize(4)
    return particles,


def main():
    global fig, ax, particles
    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=(0, Config.MAP_SCOPE), ylim=(0, Config.MAP_SCOPE))
    particles, = ax.plot([],[],'+',ms=6)

    ani = animation.FuncAnimation(fig,animate, frames=Config.MAX_ITERATION, repeat=False,
                                  interval=100, blit=True, init_func=init)
    plt.show()


if __name__ == "__main__":
    main()
