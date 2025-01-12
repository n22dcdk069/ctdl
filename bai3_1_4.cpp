#include <iostream>
#include <vector>

using namespace std;

// Hàm trộn hai mảng con đã được sắp xếp
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1; // Kích thước mảng con trái
    int n2 = right - mid;     // Kích thước mảng con phải

    // Tạo các mảng tạm thời
    vector<int> L(n1), R(n2);

    // Sao chép dữ liệu vào mảng tạm L và R
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i]; 
    }
    for (int j = 0; j < n2; j++) { // Sửa lỗi: j bắt đầu từ 0
        R[j] = arr[mid + 1 + j];
    }

    // Trộn hai mảng L và R vào arr[left..right]
    int i = 0, j = 0;
    int k = left; // Vị trí gộp vào arr
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    // Sao chép các phần tử còn lại của L (nếu có)
    while (i < n1) {
        arr[k++] = L[i++];
    }

    // Sao chép các phần tử còn lại của R (nếu có)
    while (j < n2) {
        arr[k++] = R[j++];
    }
}

// Hàm Merge Sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        // Tìm điểm giữa để chia đôi mảng
        int mid = left + (right - left) / 2; 

        // Sắp xếp đệ quy nửa bên trái
        mergeSort(arr, left, mid);

        // Sắp xếp đệ quy nửa bên phải
        mergeSort(arr, mid + 1, right);

        // Trộn hai nửa đã sắp xếp
        merge(arr, left, mid, right);
    }
}

int main() {
    vector<int> arr = {5, 2, 9, 1, 5, 6};

    mergeSort(arr, 0, arr.size() - 1);

    cout << "Kết quả Merge Sort: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}