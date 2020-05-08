def classic_solution(numbers):
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
  pivot_index = (first + last) // 2
  pivot = array[pivot_index]
  i = first - 1
  j = last + 1

  while True:
    while True:
      j = j - 1
      if array[j] <= pivot:
        break

    while True:
      i = i + 1
      if array[i] >= pivot:
        break

    if i >= j:
      return j

    swap(array, i, j)

def swap(array, first, second):
  tmp = array[first]
  array[first] = array[second]
  array[second] = tmp
