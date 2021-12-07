import utils
import numpy as np
import math
import hashlib
import random

def name():
    return "Day 7"

def solve1():
    crabs = utils.read_file_matrix("inputs/day7_1.txt", dtype=int,delimiter=",")
    fuel = []
    for i in range(max(crabs)):
        fuel.append(sum(map(lambda x: abs(x-i), crabs)))
    return min(fuel)

def calc(key, cache):
    if key not in cache:
        cache[key] = sum(range(key+1))
    return cache[key]

def solve2():
    crabs = utils.read_file_matrix("inputs/day7_1.txt", dtype=int, delimiter=",")
    fuel = []
    cache = {}
    for i in range(max(crabs)):
        fuel.append(sum(map(lambda x: calc(abs(x - i), cache), crabs)))
    return min(fuel)