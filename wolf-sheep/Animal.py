import math
from Config import INIT_SPEED, MAP_SCOPE

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_one):
        return math.sqrt( min((self.x - another_one.x) ** 2, (MAP_SCOPE - abs(self.x - another_one.x))**2 )
                          + min((self.y - another_one.y) **2, (MAP_SCOPE - abs(self.y - another_one.y))**2 ))

    def move(self, speed, delta_t: float) -> None: # speed is also a vector
        self.x = (self.x + speed.x * delta_t) % MAP_SCOPE  # periodic boundary
        self.y = (self.y + speed.y * delta_t) % MAP_SCOPE  # periodic boundary

    def inverse(self):
        self.x *= -1
        self.y *= -1


class Animal:
    def __init__(self, name, _id, **kwargs):
        self.name = name  # wolf or sheep
        self.id = _id
        self.alive = True
        self.pos = kwargs["pos"]  # this is a vector, and must have, throw exception of not set
        self.speed = kwargs.get("speed", INIT_SPEED)  # this is a vector
        self.shape = kwargs.get("shape", "v")  # the marker to plot, e.g. wolf 'D', sheep '+'

    def distance(self, other_animal  ):
        return self.pos.distance( other_animal.pos )

    def calculate_align_pulse(self, herd : [], force_0: Vector) -> Vector:
        nearby_herd = [ h for h in herd if self.distance(h) <= R_ALIGHNMENT ]
        self.speed.x = sum( [h.speed.x for h in nearby_herd])
        self.speed.y = sum( [h.speed.y for h in nearby_herd])

        # close_herd =  [ h for h in herd if self.distance(h) <= RADIUS_REPEL ]
        # todo
        return force_0
    def calculate_chase_escape(self, herd:[], force_0:Vector) -> Vector:
        close_herd =  [ h for h in herd if self.distance(h) <= R_SIGHT ]
        caught_herd = [ h for h in close_herd if self.distance(h) <= R_CAUGHT ]
        if ( len(caught_herd) >0 ):
            if (self.name == "sheep"):
                self.alive = False
                print(f"sheep-{self.id} is dead")
                return Vector(0,0)
            else:
                for h in caught_herd:
                    h.alive = False
                    print(f"sheep-{h.id} is dead")
                close_herd = list(set(close_herd) - set(caught_herd))
        #todo
        return force_0

    def calculate_force(self, herd : [], force_0: Vector) -> Vector:
        if (self.name == herd[0].name) :
            return self.calculate_align_pulse( herd, force_0)
        else:
            force = self.calculate_chase_escape( herd, force_0)
            if ( self.name == "sheep" ):
                force.inverse()
        return force

    def update_speed(self, delta_t):
        force = self.calculate_force( Wolves, Vector(0,0))
        force = self.calculate_force( alive_animals( Sheep), force)
        gaussian = np.random.normal(0,1,2)
        # del_t for force and gaussian are different
        self.speed.x = self.speed.x + force.x * delta_t + gaussian[0] * delta_t
        self.speed.y = self.speed.y + force.y * delta_t + gaussian[1] * delta_t
        pass

    def move(self, delta_t : float ):
        self.update_speed(delta_t)
        self.pos.move(self.speed, delta_t)
