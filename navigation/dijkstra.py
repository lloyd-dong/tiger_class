# road = {
#     1: ((2, 2), (3, 4)),
#     2: ((4, 7), (3, 1)),
#     3: ((5, 3),),
#     4: ((6, 1),),
#     5: ((4, 2), (6, 5)),
# }


road = {
    1: ((2, 50), (3, 45),(4,10)),
    2: ((4, 15), (3, 10)),
    3: ((5, 30),),
    4: ((1,-100), (5, 15),),
    5: ((2, 20), (3,35)),
    6: ((5,3),)
}


class Route:
    def __init__(self, start):
        self.start = start
        self.end = start
        self.path = [start]
        self.cost = 0

    def __str__(self):
        return "cost: {}, path: {}".format(self.cost, self.path)

    def _move_forward(self, _edge):
        _r = Route(self.start)
        _r.end = _edge[0]
        _r.path = self.path.copy()
        _r.path.append(_edge[0])
        _r.cost = self.cost + _edge[1]
        return _r

    def move_forward(self, edges, iterated_points):
        _new_routes = set()
        for edge in edges:
            if edge[0] in iterated_points:
                print("{} already visited for Route {}".format(edge[0], self))
                continue
            _r1 = self._move_forward(edge)
            _new_routes.add(_r1)

        iterated_points.add(self.end)
        return _new_routes


def find_route(start, end, routs):
    for rout in routs:
        if rout.start == start and rout.end == end:
            return rout
    return False


def relax(new_routes, routes):
    for _r in new_routes:
        r0 = find_route(_r.start, _r.end, routes)
        if not r0:
            routes.add(_r)
        elif r0.cost > _r.cost:
            print("{} has been replaced by {} during relaxation".format(r0, _r))
            routes.remove(r0)
            routes.add(_r)
        else:
            print("{} was dropped during relaxation".format(_r))


def get_edges(_road, start_point):
    return _road[start_point]


def main():
    s = 1
    e = 6
    r = Route(s)
    routes = {r}
    iterated_points = set()
    is_over = False
    round_num = 0

    while not is_over:

        new_routes = r.move_forward(get_edges(road, r.end), iterated_points)
        routes.remove(r)
        relax(new_routes, routes)
        if len(routes) > 0:
            r = min(routes, key=lambda x: x.cost)
        is_over = len(routes) == 0 or e == r.end

        print("\n".join([str(sr) for sr in routes]))
        round_num += 1
        print("------ {} -------".format(round_num))


if __name__ == '__main__':
    main()
