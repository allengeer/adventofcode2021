import utils
import numpy as np
# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 14"

mycache = {}

def cache(cache, key, value = None):
    if key not in cache:
        cache[key] = value
    return cache[key]

def iterate(polymer, rules):
    return "".join([first + rules[first+second] for first, second in zip(list(polymer), list(polymer)[1:])])+polymer[-1]


def solve1():
    rules = dict(np.genfromtxt("inputs/day14_1.txt", dtype='str', delimiter=" -> "))
    polymer_template = "CNBPHFBOPCSPKOFNHVKV"
    for i in range(10):
        polymer_template = iterate(polymer_template, rules)
    unique, counts = np.unique(list(polymer_template), return_counts=True)
    return max(counts) - min(counts)

def count_word(dict, w, x):
    if w not in dict:
        dict[w] = 0
    dict[w] += x

def solve2():
    rules = dict(np.genfromtxt("inputs/day14_1.txt", dtype='str', delimiter=" -> "))
    pair_counts = {k: 0 for k in rules.keys()}
    polymer_template = "CNBPHFBOPCSPKOFNHVKV"
    for first, second in zip(list(polymer_template), list(polymer_template)[1:]):
        pair_counts[first+second] += 1
    word_counts = {}

    for l in list(polymer_template):
        count_word(word_counts, l, 1)

    for i in range(40):
        new_counts = {k: 0 for k in rules.keys()}
        for pair in pair_counts.keys():
            new_counts[pair[0] + rules[pair]] += pair_counts[pair]
            new_counts[rules[pair] + pair[1]] += pair_counts[pair]
            count_word(word_counts, rules[pair], pair_counts[pair])
        pair_counts = new_counts
    return word_counts[max(word_counts, key=word_counts.get)] - word_counts[min(word_counts, key=word_counts.get)]
