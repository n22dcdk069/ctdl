def linear_search(arr, target):
  index = 0
  while index < len(arr):
    if arr[index] == target:
      return index
    index += 1
  return -1

arr = [4, 2, 5, 1, 3]
print(linear_search(arr, 5))  # Output: 2