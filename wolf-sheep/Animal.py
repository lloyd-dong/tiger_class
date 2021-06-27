import Config
import numpy as np
from numpy.random import default_rng
import util
from Logger import logger

Distance_Map = {}


class Animal:
    def __init__(self, name, _id, **kwargs):
        self.name = name  # wolf or sheep
        self.id = _id
        self.alive = True
        self.pos = kwargs["pos"]  # this is a vector, and must have, throw exception of not set
        self.speed = kwargs.get("speed", Config.INIT_SPEED)  # this is a vector
        self.shape = kwargs.get("shape", "v")  # the marker to plot, e.g. wolf 'D', sheep '+'
        logger.debug(f"{self.id} is born at {self.pos.x}, {self.pos.y}")

    # def distance(self, other_animal):
    #     return sqrt(self.square_distance(other_animal))

    def square_distance(self, other):
        if self.id == other.id:
            return 0
        key = (min(self.id, other.id), max(self.id, other.id))
        if key not in Distance_Map:
            Distance_Map[key] = self.pos.square_distance(other.pos)
        return Distance_Map[key]

    def set_alignment_points(self, idx: int, nearby: set):
        """

        :param idx: int
        :type nearby: set of idx of alignment grid
        """
        self.closest_alignment = idx
        self.nearby_alignments = nearby

    def update_speed_alignment(self):
        raw_nearby_herd = set()
        for idx in self.nearby_alignments:
            raw_nearby_herd = set.union(raw_nearby_herd, Config.Sheep_Around.get(idx, set()))
        nearby_herd_speed = [[h.speed.x, h.speed.y] for h in raw_nearby_herd
                             if self.square_distance(h) <= Config.RADIUS_ALIGNMENT_SQUARE]

        self.speed.x, self.speed.y = np.mean(nearby_herd_speed, axis=0)
        self.speed.change_direction(Config.ANGLE_DIRECTION * default_rng().uniform(-1.0, 1))

    def update_speed(self, delta_t):
        self.update_speed_alignment()
        # self.update_speed_repel(delta_t)
        # self.update_speed_chase(delta_t)

    def move(self, delta_t: float):
        self.update_speed(delta_t)
        self.pos.move(self.speed, delta_t)
        logger.info(f"{self.id} moved to {self.pos.x}, {self.pos.y}")

    # def calculate_align_pulse(self, herd : [], force_0: Vector) -> Vector:
    #     nearby_herd = [ h for h in herd if self.distance(h) <= R_ALIGHNMENT ]
    #     self.speed.x = sum( [h.speed.x for h in nearby_herd])
    #     self.speed.y = sum( [h.speed.y for h in nearby_herd])
    #
    #     # close_herd =  [ h for h in herd if self.distance(h) <= RADIUS_REPEL ]
    #     # todo
    #     return force_0
    # def calculate_chase_escape(self, herd:[], force_0:Vector) -> Vector:
    #     close_herd =  [ h for h in herd if self.distance(h) <= R_SIGHT ]
    #     caught_herd = [ h for h in close_herd if self.distance(h) <= R_CAUGHT ]
    #     if ( len(caught_herd) >0 ):
    #         if (self.name == "sheep"):
    #             self.alive = False
    #             print(f"sheep-{self.id} is dead")
    #             return Vector(0,0)
    #         else:
    #             for h in caught_herd:
    #                 h.alive = False
    #                 print(f"sheep-{h.id} is dead")
    #             close_herd = list(set(close_herd) - set(caught_herd))
    #     #todo
    #     return force_0
    #
    # def calculate_force(self, herd : [], force_0: Vector) -> Vector:
    #     if (self.name == herd[0].name) :
    #         return self.calculate_align_pulse( herd, force_0)
    #     else:
    #         force = self.calculate_chase_escape( herd, force_0)
    #         if (self.name == "sheep"):
    #             force.inverse()
    #     return force
