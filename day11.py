import utils
import numpy as np
import math
import operator
import sys
import functools

np.set_printoptions(threshold=sys.maxsize)


def name():
    return "Day 11"


def valid_coordinate(grid, point):
    return 0 <= point[0] < grid.shape[0] and 0 <= point[1] < grid.shape[1]


def adjacent_cells(grid, point):
    surrounding_cells = np.array([np.subtract(point, (1, 1)), np.subtract(point, (-1, -1)), np.subtract(point, (1, -1)),
                                  np.subtract(point, (-1, 1)), np.subtract(point, (0, -1)), np.subtract(point, (0, 1)),
                                  np.subtract(point, (-1, 0)), np.subtract(point, (1, 0))])
    return list(filter(lambda x: valid_coordinate(grid, x), surrounding_cells))


def flash(grid, point):
    grid[point[0]][point[1]] = 11
    for p in adjacent_cells(grid, point):
        if grid[p[0]][p[1]] <= 9:
            grid[p[0]][p[1]] += 1
    return


def solve1():
    octopuses = np.array(list(map(list, utils.read_file_matrix("inputs/day11_1.txt", dtype=str)))).astype(int)
    flash_count = 0
    for i in range(100):
        # Set the flash table to empty
        flash_table = np.zeros(octopuses.shape)
        # Increment the counters
        octopuses += 1
        # Count the number of new flashes
        new_flashes = len(octopuses == 10)
        # As long as there are new flashes
        while new_flashes > 0:
            # Mark the flashes in the Flash Table
            flash_table[octopuses == 10] = True
            # Increment the surrounding cells
            for point in np.argwhere(octopuses == 10):
                flash(octopuses, point)
            # Count the number of new flashes
            new_flashes = len(octopuses[octopuses == 10])
        # Reset all values >9 to 0
        octopuses[octopuses > 9] = 0
        flash_count += len(flash_table[flash_table == True])

    return flash_count


def solve2():
    octopuses = np.array(list(map(list, utils.read_file_matrix("inputs/day11_1.txt", dtype=str)))).astype(int)
    flash_count = 0
    for i in range(1000):
        # Set the flash table to empty
        flash_table = np.zeros(octopuses.shape)
        # Increment the counters
        octopuses += 1
        # Count the number of new flashes
        new_flashes = len(octopuses == 10)
        # As long as there are new flashes
        while new_flashes > 0:
            # Mark the flashes in the Flash Table
            flash_table[octopuses == 10] = True
            # Increment the surrounding cells
            for point in np.argwhere(octopuses == 10):
                flash(octopuses, point)
            # Count the number of new flashes
            new_flashes = len(octopuses[octopuses == 10])
        # Reset all values >9 to 0
        octopuses[octopuses > 9] = 0
        flash_count += len(flash_table[flash_table == True])
        if len(flash_table[flash_table == True]) == 100:
            flash_count = i
            break

    return flash_count + 1
