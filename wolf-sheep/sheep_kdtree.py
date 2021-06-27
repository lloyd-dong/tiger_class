# init sheep's position randomly, avoid overlap
# init sheep's speed randomly within INIT_SPEED
# sheep move together with a random direction ∆
# sheep can't overlap
# move with updated kdtree to check if overlap
import time

import util
import Config
import Animal

Sheep = []
Wolves = []


def init():
    util.init_animals(Sheep, Wolves)
    util.init_alignment_grid()


def main():
    init()

    for i in range(100):
        sheep = util.alive_animals(Sheep)
        if i % 4 == 0:
            util.draw(sheep)
            time.sleep(1)

        util.update_alignment(sheep)
        for s in sheep:
            s.move(Config.DELTA_T)
        util.Sheep_Around = {}
        Animal.Distance_Map = {}


if __name__ == "__main__":
    main()
