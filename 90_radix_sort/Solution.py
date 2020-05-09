import math

def solution(numbers):
  max_value = numbers[0]
  size = len(numbers)
  i = 1

  while i < size:
    if numbers[i] > max_value:
      max_value = numbers[i]
    i += 1

  digits_in_max_value = int(math.log10(max_value))+1
  digit_from_right = 1
  result = numbers

  while digit_from_right <= digits_in_max_value:
    result = counting_sort(result, digit_from_right)
    digit_from_right += 1

  return result

def counting_sort(numbers, digit):
  counter_index = -1
  i = 0
  size = len(numbers)
  result = [None] * size
  counter = []

  while i < size:
    index = calculate_index(numbers[i], digit)
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
    item_index = calculate_index(item, digit)
    counter[item_index] -= 1
    index = counter[item_index]
    result[index] = item
    k = k - 1

  return result

def calculate_index(item, digit):
  return abs(item) // (10**(digit-1)) % 10

def add_indexes(array, existing_index, index):
  while existing_index <= index:
    existing_index = existing_index + 1
    array.append(0)
