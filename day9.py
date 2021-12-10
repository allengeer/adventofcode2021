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


def is_basin(bottom_grid, point):
    return bottom_grid[point[1]][point[0]] < 9


def explore_basin(truth_table, bottom_grid, points):
    if len(points) >= 1:
        truth_table[points[0][1]][points[0][0]] = is_basin(bottom_grid, points[0])
        orthogonal_dirs = np.array([np.subtract(points[0], (0, -1)), np.subtract(points[0], (0, 1)), np.subtract(points[0], (-1, 0)),np.subtract(points[0], (1, 0))])
        valid_points = orthogonal_dirs[list(map(lambda y: valid_coordinate(bottom_grid, y), orthogonal_dirs))]
        unexplored_points = valid_points[list(map(lambda y: truth_table[y[1]][y[0]], valid_points))]


def solve2():
    bottom = utils.read_file_matrix("inputs/day9_1.txt", dtype=str)
    bottom_grid = np.array([list(map(int, line)) for line in bottom])
    truth_table = np.zeros(bottom_grid.shape)
    # acc = 0
    # for (i, j), element in np.ndenumerate(bottom_grid):
    #     if not truth_table[j][i]:

    return ""