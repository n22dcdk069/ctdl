function binary_search(arr, target)
    left = 1         # Chỉ số đầu tiên của mảng
    right = length(arr)  # Chỉ số cuối cùng của mảng
  
    while left <= right 
      mid = div(left + right, 2)  # Tính chỉ số giữa mảng
  
      if arr[mid] == target      # Nếu phần tử ở giữa bằng target
        return mid                # Trả về chỉ số mid
      elseif arr[mid] < target   # Nếu phần tử ở giữa nhỏ hơn target
        left = mid + 1           # Di chuyển left sang giữa + 1
      else                       # Nếu phần tử ở giữa lớn hơn target
        right = mid - 1          # Di chuyển right sang giữa - 1
      end
    end
  
    return -1  # Trả về -1 nếu không tìm thấy target
  end
  
  arr = [1, 3, 5, 7, 9, 11]
  println(binary_search(arr, 7))  # Output: 4