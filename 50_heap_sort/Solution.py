import math

def delete_item(heap, index):
  last_index = len(heap) - 1
  swap(heap, index, last_index)
  heap.pop()

  parent_index = parent(index)
  if heap[parent_index] < heap[index]:
    arise(heap, index)
  else:
    size = len(heap)
    drown(heap, index, size)

  return heap

def arise(array, index):
  parent_index = parent(index)
  while parent_index in array and array[parent_index] < array[index]:
    swap(array, index, parent_index)
    arise(array, parent_index)

def solution(numbers):
  heap = build_heap(numbers)
  size = len(numbers)
  i = size - 1

  while i > 0:
    size = size - 1
    swap(numbers, 0, i)
    drown(numbers, 0, size)
    i = i - 1

  return numbers

def build_heap(array):
  size = len(array)
  start_index = math.floor((size - 1) / 2) # the greatest element's index that has children

  while start_index >= 0:
    drown(array, start_index, size)
    start_index = start_index - 1

  return array

def drown(array, index, size):
  while index < size:
    left_index = left_child_index(index)
    right_index = right_child_index(index)
    largest_index = index

    if left_index < size and array[left_index] > array[largest_index]:
      largest_index = left_index

    if right_index < size and array[right_index] > array[largest_index]:
      largest_index = right_index

    if largest_index == index:
      break

    swap(array, index, largest_index)
    index = largest_index

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
