import utils
import statistics
import numpy as np


# test_array = utils.read_file_list_of_strings("inputs/test_file.txt")
# test_matrix = utils.read_file_matrix("inputs/test_file.txt", dtype=str)


def name():
    return "Day 4"


def call_number(number, cards):
    for card in cards:
        for row in card:
            for col in row:
                if col[0] == number:
                    col[1] = True
                    break


def check_card(card):
    marked = [list(map(lambda x: x[1], row)) for row in card]
    for row in marked:
        if np.all(row):
            return True
    for col in np.array(marked).transpose():
        if np.all(col):
            return True


def card_score(number, card):
    return number * sum([sum(map(lambda x: x[0], filter(lambda x: not x[1], row))) for row in card])


def solve1():
    with open("inputs/day4_1.txt") as f:
        numbers = (list(map(lambda x: int(x), f.readline().split(","))))
        line = f.readline()
        line = f.readline()
        i = 0
        cards = [[]]
        while line:
            if line == "\n":
                i += 1
                cards.append([])
            else:
                cards[i].append(list(map(lambda x: [int(x), False], line.strip().split())))
            line = f.readline()

    for number in numbers:
        call_number(number, cards)
        for card in cards:
            if check_card(card):
                return card_score(number, card)


def solve2():
    with open("inputs/day4_1.txt") as f:
        numbers = (list(map(lambda x: int(x), f.readline().split(","))))
        line = f.readline()
        line = f.readline()
        i = 0
        cards = [[]]
        while line:
            if line == "\n":
                i += 1
                cards.append([])
            else:
                cards[i].append(list(map(lambda x: [int(x), False], line.strip().split())))
            line = f.readline()

    last_win = None
    last_no = None
    for number in numbers:
        call_number(number, cards)
        for card in cards:
            if check_card(card):
                last_win = card
                last_no = number
                cards.remove(card)

    return card_score(last_no, last_win)
