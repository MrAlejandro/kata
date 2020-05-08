def insertion_solution(numbers):
  first = 0
  last = len(numbers) - 1
  tail_quick_sort(numbers, first, last)

  return numbers

def tail_quick_sort(array, first, last):
  while first < last:
    pivot = partition(array, first, last)
    if pivot == -1:
      print('skipped')
      break

    tail_quick_sort(array, first, pivot-1)
    first = pivot + 1

def partition(array, first, last):
  if (last - first) <= (2 ** 6):
    insertion_sort(array, first, last)
    print('boom')
    return -1

  pivot = array[last]
  i = first - 1
  j = first

  while j < last:
    if array[j] <= pivot:
      i = i + 1
      swap(array, i, j)

    j = j + 1

  swap(array, i + 1, last)

  return i + 1

def swap(array, first, second):
  tmp = array[first]
  array[first] = array[second]
  array[second] = tmp

def insertion_sort(array, first, last):
  j = 1

  while j <= last:
    current_value = array[j]
    i = j - 1

    while i >= first and array[i] > current_value:
      array[i + 1] = array[i]
      i = i - 1

    array[i + 1] = current_value
    j = j + 1
