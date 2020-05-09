def solution(numbers):
  counter_index = -1
  i = 0
  size = len(numbers)
  result = [None] * size
  counter = []

  while i < size:
    index = numbers[i]
    if counter_index < index:
      add_indexes(counter, counter_index, index)
      counter_index = index

    counter[index] = counter[index] + 1
    i = i + 1

  j = 1
  counter_size = len(counter)
  while j < counter_size:
    counter[j] = counter[j] + counter[j - 1]
    j = j + 1

  k = len(numbers) - 1
  while k >= 0:
    item = numbers[k]
    counter[item] = counter[item] - 1
    index = counter[item]
    result[index] = item
    k = k - 1

  return result

def add_indexes(array, existing_index, index):
  while existing_index <= index:
    existing_index = existing_index + 1
    array.append(0)
