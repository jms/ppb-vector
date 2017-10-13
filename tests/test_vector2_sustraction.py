import unittest
from ppb_vector import Vector2


class TestVector2Subtraction(unittest.TestCase):
    def test_subtraction_vectors(self):
        test_vector1 = Vector2(3, 3)
        test_vector2 = Vector2(1, 1)
        result = test_vector1 - test_vector2
        self.assertEqual(result, Vector2(2, 2))

    def test_subtraction_vector_tuple(self):
        test_vector = Vector2(3, 3)
        test_tuple = (2, 1)
        result = test_vector - test_tuple
        self.assertEqual(result, Vector2(1, 2))

    def test_subtraction_vector_list(self):
        test_vector = Vector2(3, 3)
        test_list = [2, 1]
        result = test_vector - test_list
        self.assertEqual(result, Vector2(1, 2))

    def test_subtraction_vector_dict(self):
        test_vector = Vector2(3, 3)
        test_dict = {'x': 2, 'y': 1}
        result = test_vector - test_dict
        self.assertEqual(result, Vector2(1, 2))
