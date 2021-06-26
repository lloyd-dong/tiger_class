from scipy import spatial
import numpy as np
import Animal


class Grid:
    _row = 0
    _col = 0
    _grid_size = 1
    _max_scope = 1
    is_last_row_close_to_border = False
    _KDTree = None
    _grid_data = None
    nearby_points = None


    def __init__(self, grid_size =1, max_scope = 10):
        self._grid_size = grid_size
        self._max_scope = max_scope
        # given periodic map, "max_scope - 1" to avoid the last row overlap with first row
        # when max_scope exact divided by grid_size
        self._row = int((max_scope - 1)/grid_size)
        self._col = self._row
        is_last_row_close_to_border = max_scope - grid_size * self._row < grid_size/2

        x, y = np.mgrid[0:(self._row + 1), 0:(self._col + 1)]
        self._KDTree = spatial.KDTree(list(zip(x.ravel(), y.ravel())))
        self._grid_data = self._KDTree.data

    def update_pos(self, sheep):
        sheep_pos = np.array([(s.pos.x, s.pos.y) for s in sheep])
        nearby = self._KDTree.query(sheep_pos)
        self.nearby_points = nearby[1]

    def get_closest_and_nearby(self, pos: Animal.Vector, sheep_idx):
        idx = self.nearby_points[sheep_idx]
        if pos.x - self._grid_data[idx].x > self._grid_size/2:
            idx = idx - self._col
        if pos.y - self._grid_data[idx].y > self._grid_size/2:
            idx = idx - self._row * (self._col - 1)

        nearby_points = set()
        r = idx / self._col
        c = idx % self._row
        for i_r in range(-1, 2):
            for i_c in range(-1, 2):
                new_r = (r + self._row + i_r) % self._row
                new_c = (c + self._col + i_c) % self._col
                nearby_points.add(new_r * self._col + new_c)
                if self.is_last_row_close_to_border:
                    if c == 0 or c == self._col - 1:
                        new_c = 1
                    if r == 0 or r == self._row - 1:
                        new_r = 1
                    nearby_points.add(new_r * self._col + new_c)

        return idx, nearby_points


