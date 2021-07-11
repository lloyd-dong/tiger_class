import numpy as np
from Logger import logger
import math
import Grid
import Config


class Animal:
    Distance_Map = {}

    def __init__(self, ani_type: str, _id: int, **kwargs):
        self.type: str = ani_type  # wolf or sheep
        self.chaser: str = "sheep" if (ani_type == "wolf") else "wolf"
        self.chase_direction = 1 if (ani_type == "wolf") else -1
        self.id: int = _id
        self.alive: bool = True
        self.pos = kwargs["pos"]  # this is a vector, and must have, throw exception of not set
        self.speed = kwargs.get("speed", Config.INIT_SPEED)  # this is a vector
        self.marker: str = kwargs.get("marker", "v")  # the marker to plot, e.g. wolf 'D', sheep '+'
        self.align_grid: Grid.Grid = None
        self.chase_grid: Grid.Grid = None
        logger.debug(f"{self.id} is born at {self.pos.x:.2f}, {self.pos.y:.2f}, speed {self.speed.y / math.pi * 180 :.2f}")

    def square_distance(self, other):
        if self.id == other.id:
            return 0
        key = (min(self.id, other.id), max(self.id, other.id))
        if key not in Animal.Distance_Map:
            Animal.Distance_Map[key] = self.pos.square_distance(other.pos)
        return Animal.Distance_Map[key]

    def update_speed_in_herd(self, delta_t: float):
        logger.debug(f"{self.id} speed 0 is {self.speed.y / math.pi * 180 :.2f}")
        nearby_grids = self.align_grid.get_nearby_grids(self.id)
        raw_nearby_herd = set()
        for idx in nearby_grids:
            raw_nearby_herd = set.union(raw_nearby_herd, self.align_grid.get_animals_neary(idx, self.type))
        nearby_herd = [h for h in raw_nearby_herd
                       if h.alive and self.square_distance(h) <= Config.RADIUS_ALIGNMENT_SQUARE]
        if len(nearby_herd) < 2:  # include itseft, so at least 1
            return
        logger.debug(f"{len(nearby_herd) - 1 } animals exist nearby")
        nearby_herd_speed_direction = [h.speed.y for h in nearby_herd]
        self.speed.y = (np.mean(nearby_herd_speed_direction)
                        + Config.ANGLE_DIRECTION * Config.rnd.uniform(-1.0, 1)) % math.pi
        logger.debug(f"{self.id} alignment speed is  {self.speed.y / math.pi * 180 :.2f}")
        self.update_speed_repel(nearby_herd, delta_t)

    def update_speed_repel(self, nearby_herd, delta_t: float):
        repel_herd = [n for n in nearby_herd if self.id != n.id and
                      self.square_distance(n) <= Config.RADIUS_REPEL_SQURE]
        if len(repel_herd) == 0:
            return
        logger.debug(f"{len(nearby_herd)} animals are too close")
        repel_speed = np.sum([[abs(n.pos.x - self.pos.x) / self.square_distance(n),
                               abs(n.pos.y - self.pos.y) / self.square_distance(n)]
                              for n in repel_herd],
                             axis=0) \
                      * delta_t * Config.Beta

        x = self.speed.x * math.cos(self.speed.y) - repel_speed[0]
        y = self.speed.x * math.sin(self.speed.y) - repel_speed[1]
        self.speed.x = math.sqrt(x ** 2 + y ** 2)
        self.speed.y = np.angle( x + 1j * y)
        logger.info(f"{self.id} repel speed is {self.speed.y / math.pi * 180 :.2f}")

    def update_speed_chase(self):
        raw_chase_herd = set()
        nearby_grids = self.chase_grid.get_nearby_grids(self.id)
        for idx in nearby_grids:
            raw_chase_herd = set.union(raw_chase_herd, self.chase_grid.get_animals_neary(idx, self.chaser))
        chase_herd = [h for h in raw_chase_herd
                      if h.alive and self.square_distance(h) <= Config.RADIUS_SIGHT_SQURE]
        if len(chase_herd) ==0:
            return
        logger.debug(f"{self.id} see {len(chase_herd)} animals")

        caught_events = [c for c in chase_herd if self.square_distance(c) <= Config.RADIUS_CAUGHT_SQURE]
        if len(caught_events) > 0:
            logger.debug(f" caught {len(chase_herd)} animals")
            if self.type == "sheep":
                self.alive = False
                logger.info(f"{self.id} was caught")
                return
            else:
                for s in caught_events:
                    s.alive = False
                    chase_herd.remove(s)
                    logger.info(f"{self.id} caught {s.id}")
        
        chase_herd_direction = np.angle([(h.pos.x - self.pos.x) + 1j* (h.pos.y - self.pos.y)
                                for h in chase_herd])
        self.speed.y += np.mean(chase_herd_direction) * self.chase_direction  # the +1/-1
        self.speed.y = self.speed.y % math.pi
        logger.debug(f"{self.id} chase speed is {self.speed.y / math.pi * 180 :.2f}")

    def update_speed(self, delta_t, ):
        self.update_speed_in_herd(delta_t)
        self.update_speed_chase()

    def move(self, delta_t: float, align_grid: Grid.Grid, chase_grid: Grid.Grid):
        if not self.alive:
            return
        self.align_grid = align_grid
        self.chase_grid = chase_grid
        self.update_speed(delta_t)
        self.pos.move(self.speed, delta_t)
        logger.debug(f"{self.id} moved to {self.pos.x:.2f}, {self.pos.y:.2f}")
