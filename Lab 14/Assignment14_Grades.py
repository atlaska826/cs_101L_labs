import unittest
import Grades
import math


class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, "The total function should return 0")

    def test_average_one(self):
        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.33333, 5)

    def test_average_two(self):
        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4)

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result, math.nan)

    def test_median_returns_two(self):
        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, "The median function should return 2")

    def test_median_returns_average_two_three(self):
        result = Grades.median([5, 2, 1, 3])
        self.assertEqual(result, 2.5, "The median function should return 2.5")

    def test_median_raises_error_if_len_0(self):
        with self.assertRaises(ValueError, msg="The median function should raise ValueError"):
            result = Grades.median([])


if __name__ == "__main__":
    unittest.main()
