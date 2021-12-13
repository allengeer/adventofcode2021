import utils
import numpy as np
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 13"


def solve1():
    points = np.genfromtxt("inputs/day13_1.txt", delimiter=",", dtype=int)
    folds = np.genfromtxt("inputs/day13_2.txt", delimiter="=", dtype=str)
    grid = np.zeros((1311,1311), dtype=int)
    for point in points:
        grid[point[1]][point[0]] = 1


    if folds[0][0] == "x":
        left = grid[:,0:int(folds[0][1])]
        right = np.fliplr(grid[:,(int(folds[0][1]) + 1):(int(folds[0][1]) + 1 + len(left[0]))])
        grid = left + right
    else:
        top = grid[0:int(folds[0][1])]
        bottom = np.flipud(grid[(int(folds[0][1]) + 1):(int(folds[0][1]) + 1 + len(top))])
        grid = top+bottom
    return (grid > 0).sum()


def solve2():
    points = np.genfromtxt("inputs/day13_1.txt", delimiter=",", dtype=int)
    folds = np.genfromtxt("inputs/day13_2.txt", delimiter="=", dtype=str)
    grid = np.zeros((1311, 1311), dtype=int)
    for point in points:
        grid[point[1]][point[0]] = 1

    for fold in folds:
        if fold[0] == "x":
            left = grid[:, 0:int(fold[1])]
            right = np.fliplr(grid[:, (int(fold[1]) + 1):(int(fold[1]) + 1 + len(left[0]))])
            grid = left + right
        else:
            top = grid[0:int(fold[1])]
            bottom = np.flipud(grid[(int(fold[1]) + 1):(int(fold[1]) + 1 + len(top))])
            grid = top + bottom
    grid[grid > 0] = 1
    grid = grid.astype(str)
    grid[grid == '1'] = "#"
    grid[grid == '0'] = " "
    for row in grid:
        print("".join(row))
    return ""
