from typing import Dict
import math
from numpy.random import default_rng

N = 2
Beta = 10
Gamma = 10
MAP_SCOPE = 1000
INIT_SPEED = 2
RADIUS_ALIGNMENT = 60
RADIUS_REPEL = 10
RADIUS_CAUGHT = 5
RADIUS_SIGHT = 100
RADIUS_ALIGNMENT_SQUARE = RADIUS_ALIGNMENT ** 2
RADIUS_REPEL_SQURE = RADIUS_REPEL ** 2
RADIUS_CAUGHT_SQURE = RADIUS_CAUGHT ** 2
RADIUS_SIGHT_SQURE = RADIUS_SIGHT ** 2


ANGLE_DIRECTION = 0  # !!! 0 for debugging math.pi/18 # +- 10 degress
DELTA_T = 1  # set as 1 for debugging, normally should be 0.01 or less
MAX_ITERATION = 10000
PACE = 10  # run 10 steps then draw once

rnd = default_rng()