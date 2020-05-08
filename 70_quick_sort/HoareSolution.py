def hoare_solution(numbers):
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
  i = first
  j = last

  while i < j:
    if array[i] < pivot:
      i = i + 1
      continue

    if array[j] >= pivot:
      j = j - 1
      continue

    swap(array, i, j)
  swap(array, last, j)

  return j

def swap(array, first, second):
  tmp = array[first]
  array[first] = array[second]
  array[second] = tmp
