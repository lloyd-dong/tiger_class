import matplotlib.pyplot as plt
from numpy.random import default_rng
from Animal import Animal, Vector
import Config
from logging.handlers import RotatingFileHandler
import logging
import os.path
from Grid import Grid

def alive_animals(animals: []) -> []:
    return [a for a in animals if a.alive]


def init_animals(sheep, wolves):
    rnd = default_rng()
    positions = [Vector(p[0], p[1]) for p in
                 zip(rnd.choice(int(Config.MAP_SCOPE / Config.RADIUS_REPEL), size=2 * Config.N, replace=False)
                        * Config.RADIUS_REPEL,
                     rnd.uniform(0, Config.MAP_SCOPE, 2 * Config.N))]
    speed = [Vector(p[0], p[1]) for p in zip(rnd.uniform(0, Config.INIT_SPEED, 2 * Config.N),
                                             rnd.uniform(0, Config.INIT_SPEED, 2 * Config.N))]
    for i in range(Config.N):
        sheep.append(Animal("sheep", i, pos=positions[i], speed=speed[i], shape="+"))
        # wolves.append(Animal("wolf", N + i, pos=positions[N + i], speed=speed[N + i], shape="D"))


def draw(animals):
    plt.figure(1)  # 选择图表1
    x = [s.pos.x for s in alive_animals(animals)]
    y = [s.pos.y for s in alive_animals(animals)]
    plt.scatter(x, y, marker=animals[0].shape)
    plt.show()


def init_logger(logger_name="root", base_dir='', log_file_name=""):
    # LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    formatter = logging.Formatter(LOG_FORMAT)
    log_file_name = "{}.log".format(logger_name) if not log_file_name else log_file_name

    handler_Console = logging.StreamHandler()
    handler_Console.setFormatter(formatter)
    handler_Console.setLevel(logging.DEBUG)

    if not base_dir:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(base_dir, log_file_name)
    handler_F = RotatingFileHandler(log_path, maxBytes=200 * 1024, backupCount=5)
    handler_F.setFormatter(formatter)
    handler_F.setLevel(logging.INFO)

    logger = logging.getLogger(logger_name)
    logger.addHandler(handler_Console)
    logger.addHandler(handler_F)
    logger.setLevel(logging.DEBUG)
    return logger


def init_alignment_grid():
    global Alignment_Grid
    Alignment_Grid = Grid(Config.RADIUS_ALIGNMENT, Config.MAP_SCOPE)


def update_alignment(animals):
    Alignment_Grid.update_pos([(s.pos.x, s.pos.y) for s in animals])
    for idx, s in enumerate(animals):
        closest_point, nearby_points = Alignment_Grid.get_closest_and_nearby(s.pos, idx)
        s.set_alignment_points(closest_point, nearby_points)
        if closest_point not in Sheep_Around:
            Sheep_Around[closest_point] = set()
        Sheep_Around[closest_point].add(s)


Alignment_Grid = None
Sheep_Around = {}
Distance_Map = {}
logger = init_logger("chase", log_file_name="chase.log")
