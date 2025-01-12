def partition(arr, low, high):
  pivot = arr[high]  # Chọn pivot là phần tử cuối
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]

  # Đưa pivot vào vị trí chính xác
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quick_sort(arr, low, high):
  if low < high:
    p = partition(arr, low, high)

    # Gọi đệ quy cho 2 mảng con
    quick_sort(arr, low, p - 1)  # Sửa lỗi tại đây: p - 1 thay vì p
    quick_sort(arr, p + 1, high)


arr = [5, 2, 9, 1, 5, 6]
quick_sort(arr, 0, len(arr) - 1)
print("Ket qua Quick Sort:", arr)  # Output: [1, 2, 5, 5, 6, 9]