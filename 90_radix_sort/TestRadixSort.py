import unittest

from Solution import solution
from Implementation import implementation

class TestRadixSort(unittest.TestCase):
  def test_solution(self):
    numbers_to_sort = [1000, 100, 90, 80, 70, 60, 50, 40, 30, 30, 20, 10, 1]
    expected = [1, 10, 20, 30, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
    actual = solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_implementation(self):
    numbers_to_sort = [1000, 100, 90, 80, 70, 60, 50, 40, 30, 30, 20, 10, 1]
    expected = [1, 10, 20, 30, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
    actual = implementation(numbers_to_sort)

    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
