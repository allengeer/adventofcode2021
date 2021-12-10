import utils
import numpy as np
import functools
import operator
import sys
np.set_printoptions(threshold=sys.maxsize)


def name():
    return "Day 9"


def valid_coordinate(grid, point):
    return 0 <= point[0] < grid.shape[0] and 0 <= point[1] < grid.shape[1]


def is_low(grid, point):
    orthogonal_dirs = np.array([np.subtract(point, (0, -1)), np.subtract(point, (0, 1)), np.subtract(point, (-1, 0)), np.subtract(point, (1, 0))])
    x = functools.reduce(operator.and_, map(lambda x: grid[x[1]][x[0]] > grid[point[1]][point[0]], orthogonal_dirs[list(map(lambda y: valid_coordinate(grid, y), orthogonal_dirs))] ))
    return x


def solve1():
    bottom = utils.read_file_matrix("inputs/day9_1.txt", dtype=str)
    bottom_grid = np.array([ list(map(int, line)) for line in bottom ])
    acc = 0
    for (i, j), element in np.ndenumerate(bottom_grid):
        if is_low(bottom_grid, (j, i)):
            acc += 1 + bottom_grid[i][j]
    return acc


def in_basins(basins, point):
    r = False
    for basin in basins:
        r = r or in_basin(basin, point)
    return r


def in_basin(basin, point):
    r = False
    for p in basin:
        r = r or (p[0] == point[0] and p[1] == point[1])
    return r


def explore_basin(grid, basin, point):
    if grid[point[0]][point[1]] < 9:
        if not in_basin(basin, point):
            basin.append(point)
        orthogonal_dirs = [np.subtract(point, (0, -1)), np.subtract(point, (0, 1)), np.subtract(point, (-1, 0)),np.subtract(point, (1, 0))]
        valid_dirs = list(filter(lambda y: valid_coordinate(grid, y) and not in_basin(basin, y), orthogonal_dirs))
        for direction in valid_dirs:
            explore_basin(grid, basin, direction)


def solve2():
    bottom = utils.read_file_matrix("inputs/day9_1.txt", dtype=str)
    bottom_grid = np.array([list(map(int, line)) for line in bottom])
    basins = []
    for (i, j), element in np.ndenumerate(bottom_grid):
        if not in_basins(basins, [i,j]) and element != 9:
            basin = []
            explore_basin(bottom_grid, basin, [i,j])
            basins.append(basin)
    x = list(map(len, basins))
    x.sort()
    x.reverse()
    return functools.reduce(operator.mul, x[:3])