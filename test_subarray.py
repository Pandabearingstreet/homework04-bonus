import pytest
import numpy as np

try:
    import subarray
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'subarray.py'!"

MODULE = subarray

@pytest.fixture
def dummy_array():
    return np.arange(1, 31).reshape((5, 6))


def test_simple_case(dummy_array):
    arg_sets = [
        dict(shape=(3, 3), center=(2, 2), fill=None),
    ]

    targets = [
        [[8, 9, 10], [14, 15, 16], [20, 21, 22]]
    ]

    for args, target in zip(arg_sets, targets):

        result = MODULE.subarray(array=dummy_array, **args)

        assert isinstance(result, np.ndarray)
        assert result.tolist() == target, 'Test run returned wrong result!'

def test_even_number_of_rows_or_cols(dummy_array):
    arg_sets = [
        dict(shape=(4, 3), center=(2, 2), fill=None),
        dict(shape=(3, 4), center=(2, 2), fill=None),
        dict(shape=(4, 4), center=(2, 2), fill=None),
    ]

    targets = [
        [[8, 9, 10], [14, 15, 16], [20, 21, 22], [26, 27, 28]],
        [[8, 9, 10, 11], [14, 15, 16, 17], [20, 21, 22, 23]],
        [[8, 9, 10, 11], [14, 15, 16, 17], [20, 21, 22, 23], [26, 27, 28, 29]],
    ]

    for args, target in zip(arg_sets, targets):

        result = MODULE.subarray(array=dummy_array, **args)

        assert isinstance(result, np.ndarray)
        assert result.tolist() == target, 'Test run returned wrong result!'

def test_fill_without_overlap(dummy_array):
    arg_sets = [
        dict(shape=(3, 3), center=(2, 2), fill=0),
    ]

    targets = [
        [[8, 9, 10], [14, 15, 16], [20, 21, 22]],
    ]

    for args, target in zip(arg_sets, targets):

        result = MODULE.subarray(array=dummy_array, **args)

        assert isinstance(result, np.ndarray)
        assert result.tolist() == target, 'Test run returned wrong result!'

def test_overlaps_without_fill(dummy_array):
    arg_sets = [
        dict(shape=(3, 5), center=(2, 0), fill=None),
        dict(shape=(3, 5), center=(2, 5), fill=None),
        dict(shape=(5, 3), center=(0, 2), fill=None),
        dict(shape=(5, 3), center=(4, 2), fill=None),
        dict(shape=(9, 9), center=(2, 2), fill=None),
    ]

    targets = [
        [[7, 8, 9], [13, 14, 15], [19, 20, 21]],
        [[10, 11, 12], [16, 17, 18], [22, 23, 24]],
        [[2, 3, 4], [8, 9, 10], [14, 15, 16]],
        [[14, 15, 16], [20, 21, 22], [26, 27, 28]],
        [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]],
    ]

    for args, target in zip(arg_sets, targets):

        result = MODULE.subarray(array=dummy_array, **args)

        assert isinstance(result, np.ndarray)
        assert result.tolist() == target, 'Test run returned wrong result!'

def test_overlaps_with_fill(dummy_array):
    arg_sets = [
        dict(shape=(3, 5), center=(2, 0), fill=0),
        dict(shape=(3, 5), center=(2, 5), fill=0),
        dict(shape=(5, 3), center=(0, 2), fill=0),
        dict(shape=(5, 3), center=(4, 2), fill=0),
        dict(shape=(9, 9), center=(2, 2), fill=0),
    ]

    targets = [
        [[0, 0, 7, 8, 9], [0, 0, 13, 14, 15], [0, 0, 19, 20, 21]],
        [[10, 11, 12, 0, 0], [16, 17, 18, 0, 0], [22, 23, 24, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [2, 3, 4], [8, 9, 10], [14, 15, 16]],
        [[14, 15, 16], [20, 21, 22], [26, 27, 28], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 4, 5, 6, 0], [0, 0, 7, 8, 9, 10, 11, 12, 0], [0, 0, 13, 14, 15, 16, 17, 18, 0], [0, 0, 19, 20, 21, 22, 23, 24, 0], [0, 0, 25, 26, 27, 28, 29, 30, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ]

    for args, target in zip(arg_sets, targets):

        result = MODULE.subarray(array=dummy_array, **args)

        assert isinstance(result, np.ndarray)
        assert result.tolist() == target, 'Test run returned wrong result!'
