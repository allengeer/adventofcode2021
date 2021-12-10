import utils
import numpy as np
import math
import operator
import sys
np.set_printoptions(threshold=sys.maxsize)


def name():
    return "Day 10"

opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]
points = [3, 57, 1197, 25137]


def opener(char):
    return char in opens


def closer(char):
    return char in closes


def matcher(char):
    return closes[opens.index(char)]


def pointer(char):
    return points[closes.index(char)]


def stack_points(stack):
    return sum(map(lambda x: closes.index(x) + 1, stack))


def score_corrupt(instr):
    stack = []
    for i in list(instr):
        if opener(i):
            stack.append(matcher(i))
        else:
            closer = stack.pop()
            if i == closer:
                pass
            else:
                return pointer(i)
    return 0


def score_incomplete(instr):
    stack = []
    for i in list(instr):
        if opener(i):
            stack.append(matcher(i))
        else:
            closer = stack.pop()
            if i == closer:
                pass
            else:
                return 0
    acc = 0
    stack.reverse()
    for i, e in enumerate(stack):
        acc = acc * 5 + closes.index(e) + 1
    return acc


def solve1():
    instructions = utils.read_file_matrix("inputs/day10_1.txt", dtype=str)
    tt = list(map(score_corrupt, instructions))
    return sum(tt)


def solve2():
    instructions = utils.read_file_matrix("inputs/day10_1.txt", dtype=str)
    tt = list(filter(lambda x: x> 0, list(map(score_incomplete, instructions))))
    tt.sort()
    return tt[math.floor(len(tt)/2)]