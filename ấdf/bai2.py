def count_chars(word):
    # Khởi tạo dictionary rỗng để lưu kết quả
    char_count = {}

    # Duyệt qua từng ký tự trong từ
    for char in word:
        # Kiểm tra nếu ký tự đã có trong dictionary
        if char in char_count:
            # Nếu có, tăng số lần xuất hiện lên 1
            char_count[char] += 1
        else:
            # Nếu chưa có, thêm vào dictionary với giá trị bằng 1
            char_count[char] = 1
    
    # In kết quả
    for char, count in char_count.items():
        print(f"{char}: {count}")

# Nhập từ từ người dùng
word = input("Nhập một từ: ")

# Gọi hàm và xuất kết quả
count_chars(word)
