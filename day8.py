import utils
import numpy as np
import math
import hashlib
import random

def name():
    return "Day 8"

def cache(key, cache):
    if key not in cache:
        cache[key] = sum(range(key+1))
    return cache[key]

def get_map(patterns):
    one = np.array(list(list(filter(lambda x: len(x)==2, patterns))[0]))
    seven = np.array(list(list(filter(lambda x: len(x)==3, patterns))[0]))
    four = np.array(list(list(filter(lambda x: len(x)==4, patterns))[0]))
    lights = {}
    for reading in patterns:
        for seglight in list(reading):
            if seglight not in lights:
                lights[seglight] = 0
            lights[seglight] += 1
    for k, v in lights.items():
        if v == 9:
            lights[k] = 'f'
        elif v == 4:
            lights[k] = 'e'
        elif v == 6:
            lights[k] = 'b'
        elif v == 8:
            if k in seven and k in one:
                lights[k] = 'c'
            else:
                lights[k] = 'a'
        elif v == 7:
            if k in four:
                lights[k] = 'd'
            else:
                lights[k] = 'g'

    return lights


def translate(reading, wire_map):
    return [wire_map[x] for x in reading]


def segments_to_int(reading):
    if "".join(sorted(reading)) == "abcefg":
        return 0
    elif "".join(sorted(reading)) == "cf":
        return 1
    elif "".join(sorted(reading)) == "acdeg":
        return 2
    elif "".join(sorted(reading)) == "acdfg":
        return 3
    elif "".join(sorted(reading)) == "bcdf":
        return 4
    elif "".join(sorted(reading)) == "abdfg":
        return 5
    elif "".join(sorted(reading)) == "abdefg":
        return 6
    elif "".join(sorted(reading)) == "acf":
        return 7
    elif "".join(sorted(reading)) == "abcdefg":
        return 8
    else:
        return 9

def solve1():
    segment_readings = utils.read_file_matrix("inputs/day8_1.txt", dtype=str, delimiter=" ")
    input_readings = [segment_reading[:10] for segment_reading in segment_readings]
    output_readings = [segment_reading[11:] for segment_reading in segment_readings]
    return sum(len(list(filter(lambda x: len(x) <= 4 or len(x) == 7, reading))) for reading in output_readings)


def solve2():
    segment_readings = utils.read_file_matrix("inputs/day8_1.txt", dtype=str, delimiter=" ")
    input_readings = [segment_reading[:10] for segment_reading in segment_readings]
    output_readings = [segment_reading[11:] for segment_reading in segment_readings]
    val = 0
    for i, readings in enumerate(input_readings):
        wire_map = get_map(readings)
        val += int("".join(map(lambda x: str(segments_to_int(translate(list(x), wire_map))), output_readings[i])))
    return val