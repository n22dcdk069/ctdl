import gdown
import string

# Hàm đếm số lần xuất hiện các từ trong file
def word_count(file_path):
    word_count_dict = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip().lower()  # Loại bỏ khoảng trắng và chuyển về chữ thường
                line = line.translate(str.maketrans('', '', string.punctuation))  # Loại bỏ dấu câu
                words = line.split()  # Tách dòng thành các từ

                for word in words:
                    if word in word_count_dict:
                        word_count_dict[word] += 1
                    else:
                        word_count_dict[word] = 1
        return word_count_dict

    except FileNotFoundError:
        print("File không tồn tại.")
        return {}

# Đường dẫn tải file từ Google Drive
url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'downloaded_file.txt'  # Tên file sau khi tải

# Tải file từ Google Drive
gdown.download(url, output, quiet=False)

# Đếm từ trong file đã tải
result = word_count(output)
print(result)