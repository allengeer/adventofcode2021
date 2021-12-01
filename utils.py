import numpy as np


def read_file_list_of_strings(filename):
    with open(filename) as f:
        return f.readlines()


def read_file_matrix(filename, dtype=int, delimiter=" "):
    return np.loadtxt(filename, dtype=dtype, delimiter=delimiter)
