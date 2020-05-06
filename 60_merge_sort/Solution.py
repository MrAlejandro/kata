import math

def solution(numbers):
  size = len(numbers)
  merge_sort(numbers, 0, size)

  return numbers

def merge_sort(array, start, end):
  if (end - start) < 2:
    return

  middle = (start + end) // 2
  merge_sort(array, start, middle)
  merge_sort(array, middle, end)
  merge(array, start, middle, end)

def merge(array, start, middle, end):
  left = array[start:middle]
  right = array[middle:end]
  left.append(math.inf)
  right.append(math.inf)

  i = start
  j = k = 0

  while i < end:
    if left[j] > right[k]:
      array[i] = right[k]
      k = k + 1
    else:
      array[i] = left[j]
      j = j + 1

    i = i + 1
