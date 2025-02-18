def levenshtein(source, target):
    # Bước 1: Khởi tạo ma trận D với kích thước (len(source)+1) x (len(target)+1)
    m = len(source) + 1
    n = len(target) + 1
    D = [[0] * n for _ in range(m)]
    
    # Bước 2: Hoàn thiện hàng và cột đầu tiên
    for i in range(m):
        D[i][0] = i  # Số phép xóa cần thiết
    for j in range(n):
        D[0][j] = j  # Số phép thêm cần thiết
    
    # Bước 3: Tính toán các giá trị còn lại trong ma trận
    for i in range(1, m):
        for j in range(1, n):
            if source[i - 1] == target[j - 1]:
                cost = 0  # Nếu ký tự trùng nhau, không cần thay thế
            else:
                cost = 1  # Nếu khác nhau, cần thay thế

            D[i][j] = min(D[i - 1][j] + 1,        # Xóa
                          D[i][j - 1] + 1,        # Thêm
                          D[i - 1][j - 1] + cost) # Thay thế
    
    # Bước 4: Quay lại và tìm đường đi ngắn nhất (quay lại tìm các phép biến đổi)
    i, j = m - 1, n - 1
    actions = []
    while i > 0 or j > 0:
        current_cost = D[i][j]
        if i > 0 and D[i - 1][j] + 1 == current_cost:
            actions.append(f"Delete '{source[i - 1]}'")
            i -= 1
        elif j > 0 and D[i][j - 1] + 1 == current_cost:
            actions.append(f"Insert '{target[j - 1]}'")
            j -= 1
        else:
            if source[i - 1] != target[j - 1]:
                actions.append(f"Substitute '{source[i - 1]}' with '{target[j - 1]}'")
            i -= 1
            j -= 1

    actions.reverse()
    return D[m - 1][n - 1], actions


# Nhập chuỗi source và target từ người dùng
source = input("Nhập chuỗi source: ")
target = input("Nhập chuỗi target: ")

# Tính toán khoảng cách Levenshtein và các hành động
distance, actions = levenshtein(source, target)

# In kết quả
print(f"\nKhoảng cách Levenshtein: {distance}")
print("Các hành động chỉnh sửa:")
for action in actions:
    print(action)
