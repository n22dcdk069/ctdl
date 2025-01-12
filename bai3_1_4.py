def merge(arr, left, mid, right):
  n1 = mid - left + 1  # Kích thước mảng con trái
  n2 = right - mid      # Kích thước mảng con phải

  # Tạo các mảng tạm thời
  L = arr[left:left + n1]
  R = arr[mid + 1:mid + 1 + n2]

  i = 0  # Chỉ số hiện tại của mảng L
  j = 0  # Chỉ số hiện tại của mảng R
  k = left  # Chỉ số hiện tại của mảng arr

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  # Sao chép các phần tử còn lại của L (nếu có)
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  # Sao chép các phần tử còn lại của R (nếu có)
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

def merge_sort(arr, left, right):
  if left < right:
    mid = (left + right) // 2  # Tìm điểm giữa để chia đôi mảng

    # Sắp xếp đệ quy nửa bên trái
    merge_sort(arr, left, mid)

    # Sắp xếp đệ quy nửa bên phải
    merge_sort(arr, mid + 1, right)

    # Trộn hai nửa đã sắp xếp
    merge(arr, left, mid, right)

if __name__ == "__main__":
  arr = [5, 2, 9, 1, 5, 6]
  merge_sort(arr, 0, len(arr) - 1)
  print("Kết quả Merge Sort:", arr)