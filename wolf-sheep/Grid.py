import util
from scipy import spatial
import numpy as np


class Grid:
    _row = 0
    _col = 0
    _grid_size = 1
    _max_scope = 1
    is_last_row_close_to_border = False
    _KDTree = None

    def __init__(self, grid_size =1, max_scope = util.MAP_SCOPE):
        self._grid_size = grid_size
        self._max_scope = max_scope
        # given periodic map, "max_scope - 1" to avoid the last row overlap with first row
        # when max_scope exact divided by grid_size
        self._row = int((max_scope - 1)/grid_size)
        self._col = self._row
        is_last_row_close_to_border = max_scope - grid_size * self._row < grid_size/2

        x, y = np.mgrid[0:(self._row + 1), 0:(self._col + 1)]
        _KDTree = spatial.KDTree(list(zip(x.ravel(), y.ravel())))


