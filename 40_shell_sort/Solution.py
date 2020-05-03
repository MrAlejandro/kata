def solution(numbers):
  n = len(numbers)
  gap = next_gap(n)

  while True: # gap decrement loop
    index = 0

    while index < gap: # gap start elemnt loop
      j = index + gap

      while j < n: # insertion sort loop
        current_value = numbers[j]
        i = j - gap

        while i >= 0 and numbers[i] > current_value:
          numbers[i + gap] = numbers[i]
          i = i - gap

        numbers[i + gap] = current_value
        j = j + gap

      index = index + 1

    if gap == 1:
      break

    gap = next_gap(gap)

  return numbers

def next_gap(current_gap):
  return round(current_gap / 2) or 1
