def partition(mang, thap, cao):
  pivot = mang[cao]  # Chọn phần tử cuối cùng làm pivot
  i = thap - 1  # Chỉ số của phần tử nhỏ hơn pivot

  for j in range(thap, cao):
    if mang[j] <= pivot:
      i = i + 1
      mang[i], mang[j] = mang[j], mang[i]  # Hoán đổi mang[i] và mang[j]

  mang[i + 1], mang[cao] = mang[cao], mang[i + 1]  # Đặt pivot vào đúng vị trí
  return i + 1


def quick_sort(mang, thap, cao):
  if thap < cao:
    p = partition(mang, thap, cao)  # Tìm vị trí pivot
    quick_sort(mang, thap, p - 1)  # Sắp xếp phần bên trái của pivot
    quick_sort(mang, p + 1, cao)  # Sắp xếp phần bên phải của pivot


if __name__ == "__main__":
  mang = [5, 2, 9, 1, 5, 6]
  quick_sort(mang, 0, len(mang) - 1)
  print("Kết quả Quick Sort:", mang)