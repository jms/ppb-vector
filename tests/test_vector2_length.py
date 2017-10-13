import unittest
from math import sqrt
from ppb_vector import Vector2


class TestVector2Length(unittest.TestCase):
    def test_vector2_length(self):
        test_vector = Vector2(45, 60)
        x, y = 45, 60
        length = sqrt(x * x + y * y)
        self.assertEqual(test_vector.length, length)
