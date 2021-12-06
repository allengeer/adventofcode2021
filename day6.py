import utils
import numpy as np
import matplotlib.pyplot as plt
import math


def name():
    return "Day 6"


def iterate(latern_fish, new_fish):
    if latern_fish == 0:
        new_fish.append(8)
        return 6
    else:
        return latern_fish - 1


def solve1():
    latern_fish = utils.read_file_matrix("inputs/day6_1.txt", dtype=int,delimiter=",")
    for i in range(0,80):
        new_fish = []
        latern_fish = list(map(lambda x: iterate(x, new_fish), latern_fish)) + new_fish
    return len(latern_fish)


def solve2():
    latern_fish = utils.read_file_matrix("inputs/day6_1.txt", dtype=int, delimiter=",")
    counts = np.bincount(latern_fish, minlength=9)
    for day in range(0,256):
        counts = np.roll(counts,-1)
        counts[6] += counts[8]
    return sum(counts)