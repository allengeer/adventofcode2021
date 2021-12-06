import utils
import numpy as np
import matplotlib.pyplot as plt

def name():
    return "Day 5"


def parse_line(list_of_str):
    return (tuple(map(int, list_of_str[0].split(","))), tuple(map(int,list_of_str[2].split(","))))


def is_orthogonal(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def dy(line):
    return line[1][1] - line[0][1]


def dx(line):
    return line[1][0] - line[0][0]


def slope(line):
    return dy(line)/dx(line)


def walk_the_line(line, grid):
    if dy(line) == 0:
        min_x = min(line[0][0], line[1][0])
        max_x = max(line[0][0], line[1][0])
        for i in range(min_x, max_x+1):
            grid[line[0][1]][i] += 1

    elif dx(line) == 0:
        min_y = min(line[0][1], line[1][1])
        max_y = max(line[0][1], line[1][1])
        for i in range(min_y, max_y+1):
            grid[i][line[0][0]] += 1
    else:
        left = line[0] if line[0][0] < line[1][0] else line[1]
        right = line[1] if line[0][0] < line[1][0] else line[0]
        for x in range(left[0], right[0]+1):
            y = left[1] + (x-left[0]) * slope((right,left))
            if y.is_integer():
                grid[left[1] + int((x-left[0]) * slope((left,right)))][x] += 1



def solve1():
    lines = utils.read_file_matrix("inputs/day5_1.txt", dtype=str)
    lines_parsed = list(map(parse_line, lines))
    orthogonal_lines = list(filter(is_orthogonal, lines_parsed))
    grid = np.zeros((1000,1000))
    z = list(map(lambda x: walk_the_line(x, grid), orthogonal_lines))
    x = np.where(grid > 1)
    return (grid > 1).sum()


def solve2():
    lines = utils.read_file_matrix("inputs/day5_1.txt", dtype=str)
    lines_parsed = list(map(parse_line, lines))
    grid = np.zeros((1001, 1001))
    z = list(map(lambda x: walk_the_line(x, grid), lines_parsed))
    x = np.where(grid > 1)
    plt.gray()
    plt.imshow(grid)
    plt.gca().invert_yaxis()
    plt.show()
    return (grid > 1).sum()
