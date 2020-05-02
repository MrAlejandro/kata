import unittest

from Solution import solution
from Implementation import implementation

class TestBubbleSort(unittest.TestCase):
  def test_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_implementation(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = implementation(numbers_to_sort)

    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
