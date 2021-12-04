import utils
import statistics
import numpy as np


# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 3"


def solve1():
    reading = utils.read_file_matrix("inputs/day3_1.txt", dtype=str)
    reading = np.array([list(r) for r in reading])
    gamma = "".join(str(i) for i in [statistics.mode(row) for row in reading.astype(int).transpose()])
    epslion = "".join(str(int(not bool(i))) for i in [statistics.mode(row) for row in reading.astype(int).transpose()])
    return int(gamma, 2) * int(epslion, 2)


def solve2():
    reading = utils.read_file_matrix("inputs/day3_1.txt", dtype=str)
    reading = np.array([list(r) for r in reading])
    o2rating = 0
    co2rating = 0
    for i in range(len(reading[0])):
        oxyfilter = [max(statistics.multimode(row)) for row in reading.astype(int).transpose()][i]
        reading = np.array(list(filter(lambda x: int(x[i]) == oxyfilter,
                                       reading)))
        if len(reading) == 1:
            o2rating = int("".join(reading[0]), 2)
            break

    reading = utils.read_file_matrix("inputs/day3_1.txt", dtype=str)
    reading = np.array([list(r) for r in reading])
    for i in range(len(reading[0])):
        co2filter = [ int(not bool(max(statistics.multimode(row)))) for row in reading.astype(int).transpose()][i]
        reading = np.array(list(filter(lambda x: int(x[i]) == co2filter,
                                       reading)))
        if len(reading) == 1:
            co2rating = int("".join(reading[0]), 2)
            break

    return co2rating * o2rating
