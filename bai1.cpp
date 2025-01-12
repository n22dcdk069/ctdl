#include <iostream>
using namespace std;

int sum_1_to_n(int n) {
  int s = 0;  // Khởi tạo biến s để lưu trữ tổng
  for (int i = 1; i <= n; i++) {  // Vòng lặp từ 1 đến n
    s += i;  // Cộng giá trị i vào tổng s
  }
  return s;  // Trả về tổng s
}

int main() {
  int n = 5; 
  cout << "Tong 1..n = " << sum_1_to_n(n) << endl;  // In ra tổng
  return 0;
}