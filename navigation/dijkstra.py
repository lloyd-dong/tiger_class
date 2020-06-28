road = {
    1: ((2, 2), (3, 4)),
    2: ((4, 7), (3, 1)),
    3: ((5, 3),),
    4: ((6, 1),),
    5: ((4, 2), (6, 5)),
}


# road = {
#     1: ((2, 50), (3, 45),(4,10)),
#     2: ((4, 15), (3, 10)),
#     3: ((5, 30),),
#     4: ((1,10), (5, 15),),
#     5: ((2, 20), (3,35)),
#     6: ((5,3),)
# }

class Route:
    def __init__(self, start):
        self.start = start
        self.end = start
        self.path = [start]
        self.cost = 0

    def __str__(self):
        return "cost: {}, path: {}".format(self.cost, self.path)

    def move_forward(self, _edge):
        _r = Route(self.start)
        _r.end = _edge[0]
        _r.path = self.path.copy()
        _r.path.append(_edge[0])
        _r.cost = self.cost + _edge[1]
        return _r


def find_route(start, end, routs):
    for rout in routs:
        if rout.start == start and rout.end == end:
            return rout
    return False

s = 1
e = 6
r = Route(s)
routes = {r}
iterated_points = set()
is_over = False

while not is_over:
    print("-------------")
    print("\n".join([str(sr) for sr in routes]))

    routes.remove(r)
    iterated_points.add(r.end)
    edges = road[r.end]
    for edge in edges:
        if edge[0] in iterated_points:
            print("{} already visited for Route {}".format(edge[0], r))
            continue
        r1 = r.move_forward(edge)
        if edge[0] == e:
            print("found one {}".format(r1))
        r0 = find_route(r1.start, r1.end, routes)
        if not r0:
            routes.add(r1)
        elif r0.cost > r1.cost:
            print("{} has been replaced by {} during relaxation".format(r0, r1))
            routes.remove(r0)
            routes.add(r1)
        else:
            print("{} was dropped during relaxation".format(r1))
    if len(routes) > 0:
        r = min(routes, key=lambda x: x.cost)
    is_over = len(routes) == 0 or e == r.end

print("------ The end ------")
if len(routes) > 0:
    print("shortest route {}".format(r))
