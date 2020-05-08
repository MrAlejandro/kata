import unittest
import random

from Solution import solution
from HoareSolution import hoare_solution
from ReverseSolution import reverse_solution
from ReverseHoareSolution import reverse_hoare_solution
from ClassicSolution import classic_solution
from RandomizedSolution import randomized_solution
from InsertionSolution import insertion_solution
from Implementation import implementation

class TestQuickSort(unittest.TestCase):
  def test_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_reverse_solution(self):
    numbers_to_sort = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    actual = reverse_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_hoare_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = hoare_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_reverse_hoare_solution(self):
    numbers_to_sort = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    actual = reverse_hoare_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_classic_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = classic_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_randomized_solution(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = randomized_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_insertion_solution(self):
    expected = list(range(1,1000))
    numbers_to_sort = expected.copy()
    random.shuffle(numbers_to_sort)
    actual = insertion_solution(numbers_to_sort)

    self.assertEqual(actual, expected)

  def test_implementation(self):
    numbers_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = implementation(numbers_to_sort)

    self.assertEqual(actual, expected)

if __name__ == "__main__":
  unittest.main()
