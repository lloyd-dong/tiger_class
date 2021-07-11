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
sheep_points = None
wolf_points = None

def init():
    global sheep_points, wolf_points, Alignment_Grid, Chase_Grid
    util.init_animals(Sheep, Wolves)
    Animals.extend(Wolves)
    Animals.extend(Sheep)
    Alignment_Grid = Grid.Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)
    Chase_Grid = Grid.Grid(Config.RADIUS_SIGHT, Config.MAP_SCOPE)

    shp = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "sheep"])
    sheep_points.set_data(shp.T)
    wlv = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "wolf"])
    wolf_points.set_data(wlv.T)
    return sheep_points, wolf_points


def animate(i: int):
    global fig, ax, sheep_points, wolf_points, Animals
    for _ in range(Config.PACE):
        Alignment_Grid.update_index(Animals)
        Chase_Grid.update_index(Animals)
        for a in Animals:
            a.move(Config.DELTA_T, Alignment_Grid, Chase_Grid)
        Animals = util.alive_animals(Animals)

    shp = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "sheep"])
    sheep_points.set_data(shp.T)
    wlv = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "wolf"])
    wolf_points.set_data(wlv.T)
    return sheep_points, wolf_points



def main():
    global fig, ax, sheep_points, wolf_points
    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=(0, Config.MAP_SCOPE), ylim=(0, Config.MAP_SCOPE))
    sheep_points, = ax.plot([], [], '+', ms=4)
    wolf_points, = ax.plot([], [], 'D', ms=4)

    ani = animation.FuncAnimation(fig, animate, frames=int(Config.MAX_ITERATION / Config.PACE),
                            repeat=False, interval=100, blit=True, init_func=init)
    plt.show()


def _debug():
    global fig, ax, sheep_points, wolf_points, Animals, Alignment_Grid, Chase_Grid
    with plt.ion():
        fig = plt.figure()
        ax = fig.add_subplot(111, xlim=(0, Config.MAP_SCOPE), ylim=(0, Config.MAP_SCOPE))
        sheep_points, = ax.plot([], [], '+', ms=4)
        wolf_points, = ax.plot([], [], 'D', ms=4)
        init()
        plt.draw()
        plt.pause(1)

        for _ in range(100):
            for _ in range(Config.PACE):
                Alignment_Grid.update_index(Animals)
                Chase_Grid.update_index(Animals)
                for a in Animals:
                    a.move(Config.DELTA_T, Alignment_Grid, Chase_Grid)
                Animals = util.alive_animals(Animals)

            shp = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "sheep"])
            sheep_points.set_data(shp.T)
            wlv = np.array([[s.pos.x, s.pos.y] for s in Animals if s.type == "wolf"])
            wolf_points.set_data(wlv.T)
            plt.draw()
            plt.pause(0.2)




if __name__ == "__main__":
    # main()
    _debug()
