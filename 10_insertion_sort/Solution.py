def solution(numbers):
  j = 1
  first_index = 0
  last_index = len(numbers) - 1

  while j <= last_index:
    current_value = numbers[j]
    i = j - 1

    while i >= first_index and numbers[i] > current_value:
      numbers[i + 1] = numbers[i]
      i = i - 1

    numbers[i + 1] = current_value
    j = j + 1

  return numbers

def solution_in_reverse_order(numbers):
  j = 1
  first_index = 0
  last_index = len(numbers) - 1

  while j <= last_index:
    current_value = numbers[j]
    i = j - 1

    while i >= first_index and numbers[i] < current_value:
      numbers[i + 1] = numbers[i]
      i = i - 1

    numbers[i + 1] = current_value
    j = j + 1

  return numbers
