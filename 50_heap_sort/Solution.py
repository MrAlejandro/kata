import math

def solution(numbers):
  heap = build_heap(numbers)
  size = len(numbers)
  i = size - 1

  while i > 0:
    size = size - 1
    swap(numbers, 0, i)
    drawn(numbers, 0, size)
    i = i - 1

  return numbers

def build_heap(array):
  size = len(array)
  start_index = math.floor((size - 1) / 2) # the greatest element's index that has children

  while start_index >= 0:
    drawn(array, start_index, size)
    start_index = start_index - 1

  return array

def drawn(array, index, size):
  left_index = left_child_index(index)
  right_index = right_child_index(index)
  largest_index = index

  if left_index < size and array[left_index] > array[largest_index]:
    largest_index = left_index

  if right_index < size and array[right_index] > array[largest_index]:
    largest_index = right_index

  if not largest_index == index:
    swap(array, index, largest_index)
    drawn(array, largest_index, size)

def swap(array, i1, i2):
  tmp = array[i1]
  array[i1] = array[i2]
  array[i2] = tmp

def parent(index):
  return math.floor((index - 1) / 2)

def left_child_index(index):
  return index * 2 + 1

def right_child_index(index):
  return index * 2 + 2
