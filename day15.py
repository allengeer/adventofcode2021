import utils
import numpy as np
import heapq as hq

# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 15"


def heur_risk(path, grid):
    return sum(map(lambda x: grid[x[1]][x[0]], path))


def heur_distance(path, grid):
    return sum(map(lambda x: grid[x[1]][x[0]], path))


def valid_coordinate(grid, point):
    return 0 <= point[0] < grid.shape[0] and 0 <= point[1] < grid.shape[1]


def path_end(path, grid):
    return path[1][-1][0] == grid.shape[0]-1 and path[1][-1][1] == grid.shape[1]-1


def solve1():
    grid = np.genfromtxt("inputs/day15_1.txt", delimiter=1)
    paths = []
    hq.heappush(paths, (0, [[0,0]]))

    path = hq.heappop(paths)
    visited = []

    while not path_end(path, grid):
        current_path_risk = path[0]
        last_point = path[1][-1]
        orthogonal_dirs = [np.subtract(last_point, (0, -1)).tolist(), np.subtract(last_point, (0, 1)).tolist(), np.subtract(last_point, (-1, 0)).tolist(), np.subtract(last_point, (1, 0)).tolist()]
        valid_dirs = list(filter(lambda x: valid_coordinate(grid, x) and x not in path[1] and x not in visited, orthogonal_dirs))
        for dir in valid_dirs:
            visited = visited + [dir]
            hq.heappush(paths, (current_path_risk + grid[dir[1]][dir[0]], path[1] + [dir]))
        path = hq.heappop(paths)
    return path[0]


def solve2():
    grid = np.genfromtxt("inputs/day15_1.txt", delimiter=1)
    return ""
