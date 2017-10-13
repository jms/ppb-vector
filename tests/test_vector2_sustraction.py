import pytest
from ppb_vector import Vector2


def test_subtraction_vectors():
    test_vector1 = Vector2(3, 3)
    test_vector2 = Vector2(1, 1)
    result = test_vector1 - test_vector2
    assert result == Vector2(2, 2)


def test_subtraction_vector_tuple():
    test_vector = Vector2(3, 3)
    test_tuple = (2, 1)
    result = test_vector - test_tuple
    assert result == Vector2(1, 2)


def test_subtraction_vector_list():
    test_vector = Vector2(3, 3)
    test_list = [2, 1]
    result = test_vector - test_list
    assert result == Vector2(1, 2)


def test_subtraction_vector_dict():
    test_vector = Vector2(3, 3)
    test_dict = {'x': 2, 'y': 1}
    result = test_vector - test_dict
    assert result == Vector2(1, 2)
