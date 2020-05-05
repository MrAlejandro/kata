import unittest

from RecursiveSolution import recursive_solution
from Solution import build_heap, delete_item, solution
from Implementation import implementation

class TestHeapSort(unittest.TestCase):
  def test_delete_item(self):
    heap = [10, 9, 5, 7, 8, 4, 1, 6, 3, 1, 3, 2, 2, 1, 1, 5]
    actual = delete_item(heap, 14)
    expected = [10, 9, 5, 7, 8, 4, 5, 6, 3, 1, 3, 2, 2, 1, 1]

    self.assertEqual(actual, expected)
    self.assertTrue(actual == build_heap(actual))

    heap = [10, 9, 5, 7, 8, 4, 1, 6, 3, 1, 3, 2, 2, 1, 1, 5]
    actual = delete_item(heap, 1)
    expected = [10, 8, 5, 7, 5, 4, 1, 6, 3, 1, 3, 2, 2, 1, 1]

    self.assertEqual(actual, expected)
    self.assertTrue(actual == build_heap(actual))

  def test_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_recursive_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = recursive_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_implementation(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = implementation(numbers_to_sort)

    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
