road = {
    1: ((2, 2), (3, 4)),
    2: ((4, 7), (3, 1)),
    3: ((5, 3),),
    4: ((6, 1),),
    5: ((4, 2), (6, 5)),
}


road = {
    1: ((2, 50), (3, 45), (4, 10)),
    2: ((4, 15), (3, 10)),
    3: ((5, 30),),
    4: ((1,10), (5, 15),),
    5: ((2, 20),),
    6: ((5,3),)
}


class Route:
    def __init__(self, start):
        self.start = start
        self.end = start
        self.path = [start]
        self.cost = 0

    def copy(self):
        new_one = Route(self.start)
        new_one.end = self.end
        new_one.cost = self.cost
        new_one.path = self.path.copy()
        return new_one

    def __str__(self):
        return "cost: {}, path: {}".format(self.cost, self.path)

    def move_forward(self, _edge):
        _r = self.copy()
        _r.end = _edge[0]
        _r.path.append(_edge[0])
        _r.cost += _edge[1]
        return _r


def find_route(start, end, routs):
    for rout in routs:
        if rout.start == start and rout.end == end:
            return rout
    return False

def sort_set(routes):
    l = []
    l.extend(routes)
    l.sort(key=lambda x: x.cost)
    return l

s = 1
e = 6
routes = {Route(s)}
found = False
del_set = set()

while not found:
    add_set = set()
    sorted_routs = sort_set(routes)
    previous_route_cost = float('inf')
    for r in sorted_routs:
        if r in del_set or r.cost > previous_route_cost:
            continue
        previous_route_cost = r.cost
        del_set.add(r)
        edges = road[r.end]
        for edge in edges:
            if edge[0] in r.path:
                continue
            r1 = r.move_forward(edge)
            r0 = find_route(r1.start, r1.end, routes.union(del_set))
            if not r0:
                add_set.add(r1)
            elif r0.cost > r1.cost:
                del_set.add(r0)
                add_set.add(r1)

    routes.difference_update(del_set)
    routes.update(add_set)
    if len(routes) == 0:
        print("no way")
        exit()
    found = all({r.end == e for r in routes}) and len({r.cost for r in routes}) == 1
print(len(routes))
print(routes.pop())
