import unittest
import ppb_vector


class TestVector2Subtraction(unittest.TestCase):
    def test_subtraction_vectors(self):
        test_vector1 = ppb_vector.Vector2(3, 3)
        test_vector2 = ppb_vector.Vector2(1, 1)

        result = test_vector1 - test_vector2
        self.assertEqual(result, ppb_vector.Vector2(2, 2))

    def test_subtraction_vector_tuple(self):
        test_vector = ppb_vector.Vector2(3, 3)
        test_tuple = (2, 1)
        result = test_vector - test_tuple
        self.assertEqual(result, ppb_vector.Vector2(1, 2))

    def test_subtraction_vector_list(self):
        test_vector = ppb_vector.Vector2(3, 3)
        test_list = [2, 1]
        result = test_vector - test_list
        self.assertEqual(result, ppb_vector.Vector2(1, 2))

    def test_subtraction_vector_dict(self):
        test_vector = ppb_vector.Vector2(3, 3)
        test_dict = {'x': 2, 'y': 1}
        result = test_vector - test_dict
        self.assertEqual(result, ppb_vector.Vector2(1, 2))
