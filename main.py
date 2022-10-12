def sort1(arr: list) -> list:
  change_counter = 0
  current = 0

  while True:
    if arr[current] > arr[current + 1]:
      temp = arr[current]
      arr[current] = arr[current + 1]
      arr[current + 1] = temp
      change_counter += 1
      current += 1
      continue

    if change_counter == 0 and current + 1 == len(arr) - 1:
      break

    if current + 1 == len(arr) - 1:
        current, change_counter = 0, 0
        continue
    current += 1

  return arr


if __name__ == "__main__":
  arr = [1, 2, 45, 3, 6]
  res = sort1(arr)
  print(res)