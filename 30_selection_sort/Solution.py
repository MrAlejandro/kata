def solution(numbers):
  n = len(numbers)
  i = 0

  while i < n:
    min_value_index = i
    j = i + 1

    while j < n:
      if numbers[j] < numbers[min_value_index]:
        min_value_index = j
      j = j + 1

    if i != min_value_index:
      tmp = numbers[i]
      numbers[i] = numbers[min_value_index]
      numbers[min_value_index] = tmp

    i = i + 1

  return numbers
