def solution(numbers):
  n = len(numbers)

  while n > 1:
    i = 1
    while i < n:
      if numbers[i] < numbers[i-1]:
        tmp = numbers[i]
        numbers[i] = numbers[i-1]
        numbers[i-1] = tmp

      i = i + 1

    n = n - 1

  return numbers
