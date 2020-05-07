def reverse_solution(numbers):
  first = 0
  last = len(numbers) - 1
  quick_sort(numbers, first, last)

  return numbers

def quick_sort(array, first, last):
  if first < last:
    pivot = partition(array, first, last)
    quick_sort(array, first, pivot-1)
    quick_sort(array, pivot+1, last)

def partition(array, first, last):
  pivot = array[last]
  i = first - 1
  j = first

  while j < last:
    if array[j] >= pivot:
      i = i + 1
      swap(array, i, j)

    j = j + 1

  swap(array, i+1, last)
  return i + 1

def swap(array, first, last):
  tmp = array[first]
  array[first] = array[last]
  array[last] = tmp
