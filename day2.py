import utils
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 2"


def solve1():
    instructions = utils.read_file_matrix("inputs/day2_1.txt", dtype=str)
    (x,y,z) = (0,0,0)
    for instruction, amount in instructions:
        if instruction == "forward":
            y += int(amount)
        elif instruction == "down":
            z += int(amount)
        elif instruction[0] == "up":
            z -= int(amount)

    return y*z


def solve2():
    instructions = utils.read_file_matrix("inputs/day2_1.txt", dtype=str)
    (x, y, z, aim) = (0, 0, 0, 0)
    for instruction, amount in instructions:
        if instruction == "forward":
            y += int(amount)
            z += aim * int(amount)
        elif instruction == "down":
            aim += int(amount)
        elif instruction == "up":
            aim -= int(amount)
    return y * z
