import utils
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 2"


def solve1():
    instructions = utils.read_file_matrix("inputs/day2_1.txt", dtype=str)
    (x,y,z) = (0,0,0)
    for instruction in instructions:
        print(instruction)
        if instruction[0] == "forward":
            y += int(instruction[1])
        elif instruction[0] == "down":
            z += int(instruction[1])
        elif instruction[0] == "up":
            z -= int(instruction[1])

    return y*z


def solve2():
    instructions = utils.read_file_matrix("inputs/day2_1.txt", dtype=str)
    (x, y, z, aim) = (0, 0, 0, 0)
    for instruction in instructions:
        print(instruction)
        if instruction[0] == "forward":
            y += int(instruction[1])
            z += aim * int(instruction[1])
        elif instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])

    return y * z
