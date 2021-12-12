import utils
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 12"

edges = {}

def iterate(path):
    if path[-1] == 'end':
        return 1
    else:
        next = list(filter(lambda x: x != "start" and (x.isupper() or x.islower() and x not in path),edges[path[-1]]))
        return sum(map(lambda x: iterate(path + [x]), next))

paths = []

def iterate_twice(path):
    if path[-1] == 'end' and path not in paths:
        paths.append(path)
        return 1
    else:
        x = list(filter(lambda x: x.islower(), path))
        if len(x) == len(set(x)):
            next = list(filter(lambda x: x != "start" and (x.isupper() or x.islower() and path.count(x) <= 1),edges[path[-1]]))
        else:
            next = list(filter(lambda x: x != "start" and (x.isupper() or x.islower() and x not in path), edges[path[-1]]))
        return sum(map(lambda x: iterate_twice(path + [x]), next))


def solve1():
    for edge in utils.read_file_matrix("inputs/day12_1.txt", dtype=str, delimiter="-"):
        if edge[0] in edges:
            edges[edge[0]].append(edge[1])
        else:
            edges[edge[0]] = [edge[1]]
        if edge[1] in edges:
            edges[edge[1]].append(edge[0])
        else:
            edges[edge[1]] = [edge[0]]
    return iterate(["start"])


def solve2():
    sol = iterate_twice(["start"])
    return sol
