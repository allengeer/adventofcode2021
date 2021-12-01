import utils
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 1"


def solve1():
    input_list = utils.read_file_matrix("inputs/day1_1.txt", dtype=int)
    count = 0
    prev = input_list[0]
    for reading in input_list[1:]:
        if reading > prev:
            count += 1
        prev = reading
    return count


def solve2():
    input_list = utils.read_file_matrix("inputs/day1_1.txt", dtype=int)
    count = 0
    for i in range(len(input_list) - 3):
        window_a = input_list[i] + input_list[i+1] + input_list[i+2]
        window_b = input_list[i+1] + input_list[i + 2] + input_list[i + 3]
        if window_b > window_a:
            count += 1

    return count
