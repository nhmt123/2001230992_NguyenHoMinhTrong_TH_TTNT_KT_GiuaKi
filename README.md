# KNN - Phân loại Khách hàng theo Thể hình

---

## Thông tin 

| Thông tin | Chi tiết |
|-----------|----------|
| **Họ Tên** | Nguyễn hồ Minh Trọng |
| **Mã sinh viên** | 2001230992 |
| **Đồ án** | Kiểm tra Giữa kỳ - Thuật toán KNN |
| **Ngôn ngữ** | Python 3.x |
| **Thư viện chính** | NumPy, Pandas, Matplotlib |

---

## Giới thiệu

Đây là dự án giữa kỳ về thuật toán **K-Nearest Neighbors (KNN)** để phân loại khách hàng dựa trên cân nặng và chiều cao. Chương trình sử dụng KNN tự định nghĩa (không dùng thư viện có sẵn) để dự đoán thể hình của khách hàng.

---

## Mục đích

- Hiểu và cài đặt thuật toán KNN từ đầu
- Áp dụng KNN vào bài toán phân loại thực tế  
- Trực quan hóa kết quả phân loại

---

## Dữ liệu

File dữ liệu: `du_lieu_khach_hang.xlsx`

**Các thuộc tính:**
- **Cân nặng** (kg)
- **Chiều cao** (cm)  
- **Phân loại:** Thân hình Lớn, Thân hình Nhỏ, Thân hình Trung Bình

---

## Cài đặt

### Yêu cầu thư viện

```bash
pip install numpy pandas matplotlib scikit-learn openpyxl
```

### Cấu trúc thư mục

```
project/
│
├── 1765805037394_KT_GiuaKi_KNN.py
├── du_lieu_khach_hang.xlsx
└── README.md
```

---

## 🚀 Cách sử dụng

### 1. Chạy chương trình:

```bash
python 1765805037394_KT_GiuaKi_KNN.py
```

### 2. Nhập thông tin theo hướng dẫn:

- Tên khách hàng
- Cân nặng (kg)
- Chiều cao (cm)
- Giá trị K (số láng giềng muốn xét)

### 3. Xem kết quả:

- Kết quả phân loại hiển thị trên console
- Biểu đồ trực quan hóa tự động mở ra
- Dữ liệu mới được lưu vào file Excel

---

## 💡 Ví dụ chạy

### Input:

```
Nhập Tên khách hàng: Khách 1
Nhập Cân nặng (kg): 95
Nhập Chiều cao (cm): 175
Chọn trọng số K: 5
```

### Output:

```
--- KẾT QUẢ DỰ ĐOÁN ---
   Tên khách hàng: Khách 1
   Cân nặng: 95.0 kg, Chiều cao: 175.0 cm
   Trọng số K đã chọn: 5
   Phân loại dự đoán: **Thân hình Lớn**
```

---

## 🧮 Cách hoạt động

### 1. Thuật toán KNN tự định nghĩa

```python
def KNN(X_train, X_test, y_train, k):
```

**Các bước thực hiện:**

1. Tính khoảng cách **Euclidean** từ điểm mới đến tất cả điểm trong tập huấn luyện
2. Sắp xếp các khoảng cách theo thứ tự tăng dần
3. Chọn **K láng giềng gần nhất**
4. Đếm số lượng mỗi lớp trong K láng giềng
5. Trả về lớp có số lượng nhiều nhất (**voting**)

**Công thức khoảng cách Euclidean:**

```
d(p,q) = √[(p₁-q₁)² + (p₂-q₂)²]
```

Trong đó:
- `p` là điểm cần phân loại
- `q` là điểm trong tập huấn luyện

---

### 2. Hàm trực quan hóa

```python
def visualize_knn(X_train, y_train, new_point, k, prediction):
```

**Chức năng:**
- Vẽ scatter plot cho các điểm dữ liệu huấn luyện
- Mỗi lớp có **màu sắc khác nhau**
- Điểm mới được đánh dấu bằng **hình thoi màu đỏ**
- Hiển thị kết quả dự đoán trên tiêu đề

---

### 3. Chương trình chính

```python
def run_knn_for_customer():
```

**Quy trình xử lý:**

1. ✅ Tải dữ liệu từ file Excel
2. ✅ Nhận input từ người dùng
3. ✅ Thực hiện phân loại bằng KNN
4. ✅ Hiển thị kết quả và biểu đồ
5. ✅ Lưu kết quả vào file Excel

---

## 📈 Kết quả Demo

### Ví dụ với K=5

| Thông tin | Giá trị |
|-----------|---------|
| **Cân nặng** | 95 kg |
| **Chiều cao** | 175 cm |
| **K** | 5 |
| **Kết quả** | Thân hình Lớn |

Biểu đồ hiển thị:
- 🟣 **Thân hình Lớn** (màu tím)
- 🔵 **Thân hình Nhỏ** (màu xanh lục)
- 🟡 **Thân hình Trung Bình** (màu vàng)
- 🔴 **Điểm test** (hình thoi đỏ)

---

## 🎨 Đặc điểm nổi bật

| Tính năng | Mô tả |
|-----------|-------|
| ✅ **KNN tự code** | Không sử dụng `sklearn.KNeighborsClassifier` trong phần tính toán chính |
| ✅ **Trực quan hóa** | Biểu đồ scatter plot với matplotlib |
| ✅ **Lưu trữ dữ liệu** | Tự động cập nhật file Excel với dữ liệu mới |
| ✅ **Xử lý lỗi** | Kiểm tra file, validate input, xử lý exception |
| ✅ **Tùy chỉnh K** | Người dùng có thể chọn giá trị K phù hợp |

---

## 📝 Lưu ý quan trọng

> ⚠️ **Giá trị K:** Nên chọn số lẻ để tránh trường hợp hòa khi voting

> ⚠️ **Kích thước K:** Không nên quá nhỏ (overfitting) hoặc quá lớn (underfitting)

> ⚠️ **File dữ liệu:** Đảm bảo `du_lieu_khach_hang.xlsx` tồn tại trước khi chạy

> ⚠️ **Kết thúc chương trình:** Đóng cửa sổ biểu đồ để kết thúc

---

## 🔍 Cải tiến có thể thực hiện

- [ ] Chuẩn hóa dữ liệu (normalization/standardization)
- [ ] Thêm tính năng cross-validation
- [ ] Tính toán accuracy trên tập test
- [ ] Tối ưu hóa với vectorization thay vì vòng lặp
- [ ] Thêm các metric đánh giá (precision, recall, F1-score)
- [ ] Hỗ trợ nhiều thuộc tính hơn
- [ ] Weighted KNN (trọng số theo khoảng cách)

---

## 📚 Công thức và Lý thuyết

### Độ chính xác (Accuracy)

```
Accuracy = Số mẫu dự đoán đúng / Tổng số mẫu
```

### Chọn K tối ưu

- **K nhỏ (1-3):** Nhạy cảm với nhiễu, có thể overfitting
- **K trung bình (5-10):** Cân bằng tốt cho hầu hết bài toán
- **K lớn:** Ổn định nhưng có thể underfitting

### Thuật toán bỏ phiếu (Voting)

```
Predicted_Class = argmax(count(class_i))
```

Trong đó `class_i` là các lớp xuất hiện trong K láng giềng gần nhất.
