# K-Means - Phân cụm Khách hàng Tự động

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

Đây là dự án giữa kỳ về thuật toán **K-Means Clustering** để phân cụm khách hàng dựa trên nhiều đặc trưng có thể tùy chọn. Chương trình tự động tìm số cụm tối ưu và cho phép người dùng linh hoạt chọn các thuộc tính để phân tích.

---

## Mục đích

- Hiểu và áp dụng thuật toán **K-Means Clustering** (học không giám sát)
- Phân cụm khách hàng để phân tích hành vi và đặc điểm
- Tự động tìm số cụm K tối ưu bằng **Elbow Method** và **Silhouette Score**
- Trực quan hóa kết quả với **PCA** cho dữ liệu đa chiều
- Chuẩn hóa dữ liệu với **StandardScaler** để cải thiện độ chính xác

---

## Dữ liệu

File dữ liệu: `du_lieu_khach_hang.xlsx`

**Các cột có thể sử dụng:**
- ✅ **Cân nặng (kg)** - Số, có thể dùng
- ✅ **Chiều cao (cm)** - Số, có thể dùng
- ✅ **Tuổi** - Số, có thể dùng
- ✅ **Thu nhập tháng (VND)** - Số, có thể dùng
- ✅ **Số lần mua hàng** - Số, có thể dùng
- ✅ **Giá trị đơn hàng trung bình (VND)** - Số, có thể dùng
- ❌ **Tên khách hàng** - Không dùng được (text)
- ❌ **Giới tính** - Không dùng được (text)
- ❌ **Khu vực sống** - Không dùng được (text)

> 💡 **Lưu ý:** Chỉ các cột số mới có thể dùng cho phân cụm

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
├── KT_GiuaKi_KMeans.py
├── du_lieu_khach_hang.xlsx
└── README.md
```

---

## Cách sử dụng

### 1. Chạy chương trình:

```bash
python KT_GiuaKi_KMeans.py
```

### 2. Chọn các cột để phân cụm:

Chương trình sẽ hiển thị danh sách tất cả các cột. Nhập tên các cột cần dùng, **cách nhau bằng dấu phấy**.

**Ví dụ:**
```
Nhập tên cột: Cân nặng (kg), Chiều cao (cm)
```

Hoặc phức tạp hơn:
```
Nhập tên cột: Cân nặng (kg), Chiều cao (cm), Thu nhập tháng, Tuổi
```

### 3. Xem biểu đồ Elbow Method:

- Chương trình tự động tính toán và vẽ biểu đồ **Elbow Curve**
- Biểu đồ giúp xác định số cụm K tối ưu
- Đóng cửa sổ biểu đồ để tiếp tục

### 4. Chọn số cụm K:

```
Nhập số cụm K bạn muốn (gợi ý 2, hoặc số khác): 2
```

- Chương trình gợi ý K tối ưu dựa trên **Silhouette Score**
- Bạn có thể chọn K khác nếu muốn
- Nhấn Enter để dùng K gợi ý

### 5. Xem kết quả:

- **Bảng thống kê:** Hiển thị đặc điểm trung bình của mỗi cụm
- **Biểu đồ phân cụm:** Trực quan hóa các cụm với màu sắc khác nhau
- **File Excel:** Tự động thêm cột "ID Cụm" vào file dữ liệu

---

## Ví dụ chạy

### Input:

```
Nhập tên cột: Cân nặng (kg), Chiều cao (cm)

[Xem biểu đồ Elbow Method → Đóng cửa sổ]

GỢI Ý: K tối ưu = 2 (Silhouette Score = 0.651)
Nhập số cụm K bạn muốn (gợi ý 2, hoặc số khác): 2
```

### Output:

```
================================================================================
KẾT QUẢ PHÂN CỤM
================================================================================
ID Cụm  Số lượng khách  Cân nặng (kg)  Chiều cao (cm)
0                   23          80.22          179.48
1                   27          59.52          165.00
================================================================================

ĐÃ LƯU KẾT QUẢ!
   → Thêm cột 'ID Cụm' vào file 'du_lieu_khach_hang.xlsx'
   → Mỗi khách hàng giờ có nhãn cụm từ 0 đến 1
```

---

## Cách hoạt động

### 1. Thuật toán K-Means

**K-Means** là thuật toán phân cụm (clustering) không giám sát, chia dữ liệu thành K nhóm dựa trên độ tương đồng.

**Các bước:**

1. **Khởi tạo:** Chọn ngẫu nhiên K điểm làm tâm cụm ban đầu (centroids)
2. **Gán nhãn:** Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất
3. **Cập nhật tâm:** Tính lại tâm cụm = trung bình các điểm trong cụm
4. **Lặp lại:** Lặp bước 2-3 cho đến khi tâm không đổi hoặc đạt số vòng lặp tối đa

**Công thức khoảng cách Euclidean:**

```
d(x, c) = √[Σ(xᵢ - cᵢ)²]
```

Trong đó:
- `x` là điểm dữ liệu
- `c` là tâm cụm
- `i` là chỉ số thuộc tính

---

### 2. Chuẩn hóa dữ liệu (StandardScaler)

```python
scaler = StandardScaler()
X = scaler.fit_transform(X_raw)
```

**Tại sao cần chuẩn hóa?**

- Các thuộc tính có đơn vị khác nhau (kg, cm, VND, tuổi)
- Thuộc tính có giá trị lớn (thu nhập) sẽ ảnh hưởng nhiều hơn
- Chuẩn hóa đưa tất cả về cùng thang đo (mean=0, std=1)

**Công thức:**

```
z = (x - μ) / σ
```

Trong đó:
- `x` là giá trị gốc
- `μ` là trung bình
- `σ` là độ lệch chuẩn

---

### 3. Tìm K tối ưu

#### **Phương pháp 1: Elbow Method**

```python
wcss = []  # Within-Cluster Sum of Squares
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
```

- Vẽ đồ thị WCSS theo K
- Tìm điểm "khuỷu tay" (elbow) - nơi WCSS giảm chậm lại
- K tối ưu thường nằm ở vị trí elbow

**WCSS (Within-Cluster Sum of Squares):**

```
WCSS = Σ Σ ||x - cₖ||²
```

Trong đó:
- Tổng trên tất cả K cụm
- Tổng trên tất cả điểm x trong cụm k
- `cₖ` là tâm cụm k

#### **Phương pháp 2: Silhouette Score**

```python
silhouette_score(X, labels)
```

- Đo độ tách biệt giữa các cụm
- Giá trị từ **-1 đến 1**
  - Gần **1**: Cụm tốt, điểm gần nhau trong cụm, xa điểm cụm khác
  - Gần **0**: Cụm chồng lấn
  - **Âm**: Điểm có thể bị gán sai cụm

**Công thức:**

```
s(i) = (b(i) - a(i)) / max{a(i), b(i)}
```

Trong đó:
- `a(i)` = khoảng cách trung bình từ điểm i đến các điểm khác trong cùng cụm
- `b(i)` = khoảng cách trung bình từ điểm i đến các điểm trong cụm gần nhất khác

---

### 4. Giảm chiều với PCA

```python
pca = PCA(n_components=2)
X_plot = pca.fit_transform(X_raw)
```

**Khi nào dùng PCA?**

- Khi có **nhiều hơn 2 thuộc tính** (không thể vẽ trên 2D)
- PCA giảm xuống còn 2 chiều để vẽ biểu đồ scatter plot

**PCA là gì?**

- **Principal Component Analysis** - Phân tích thành phần chính
- Tìm 2 trục chính giải thích nhiều nhất sự biến thiên của dữ liệu
- Ví dụ: PCA giải thích 85% biến thiên → 2 trục này mang 85% thông tin

---

### 5. Hàm trực quan hóa

```python
def visualize_kmeans(X_raw, labels, centers, k, selected_cols):
```

**Chức năng:**

- Tự động xử lý **dữ liệu đa chiều** bằng PCA
- Vẽ scatter plot với **màu sắc khác nhau** cho mỗi cụm
- Hiển thị **tâm cụm (centroid)** bằng dấu X màu đen
- Ghi số lượng khách hàng trong mỗi cụm
- Hiển thị tên các thuộc tính đã chọn

---

### 6. Chương trình chính

```python
def run_kmeans_for_customer():
```

**Quy trình xử lý:**

1. ✅ Tải dữ liệu từ Excel
2. ✅ Hiển thị danh sách cột và lọc cột số
3. ✅ Cho phép người dùng chọn cột để phân cụm
4. ✅ Chuẩn hóa dữ liệu bằng StandardScaler
5. ✅ Tìm K tối ưu bằng Elbow Method và Silhouette Score
6. ✅ Chạy K-Means với K do người dùng chọn
7. ✅ Hiển thị bảng thống kê và biểu đồ
8. ✅ Lưu kết quả vào file Excel

---

## Đặc điểm nổi bật

| Tính năng | Mô tả |
|-----------|-------|
| ✅ **Tự động tìm K** | Dùng Elbow Method + Silhouette Score |
| ✅ **Chuẩn hóa dữ liệu** | StandardScaler để xử lý đơn vị khác nhau |
| ✅ **Hỗ trợ đa chiều** | PCA tự động giảm chiều để trực quan hóa |
| ✅ **Linh hoạt chọn cột** | Người dùng tự chọn thuộc tính để phân cụm |
| ✅ **Thống kê chi tiết** | Bảng tóm tắt đặc điểm từng cụm |
| ✅ **Lưu kết quả** | Tự động thêm cột "ID Cụm" vào Excel |

---
## Các chỉ số đánh giá

### 1. WCSS (Within-Cluster Sum of Squares)

- Tổng bình phương khoảng cách từ điểm đến tâm cụm
- **WCSS thấp** = các điểm trong cụm gần nhau → tốt
- Dùng để vẽ Elbow Method

### 2. Silhouette Score

- Đánh giá chất lượng phân cụm
- **0.7 - 1.0:** Cụm mạnh, rõ ràng
- **0.5 - 0.7:** Cụm hợp lý
- **0.25 - 0.5:** Cụm yếu, cần xem xét
- **< 0.25:** Không có cấu trúc cụm rõ ràng

### 3. Inertia

- Tương tự WCSS
- Giá trị `kmeans.inertia_` trong sklearn
- Càng nhỏ càng tốt (nhưng giảm khi K tăng)

---

## Lưu ý quan trọng

> **Chọn K:** Không nên quá nhỏ (mất thông tin) hoặc quá lớn (quá phức tạp)

> **Chuẩn hóa:** Bắt buộc khi các thuộc tính có đơn vị/giá trị khác nhau nhiều

> **Số cột:** Cần ít nhất 2 cột số để phân cụm

> **PCA:** Khi dùng >2 thuộc tính, biểu đồ chỉ là gần đúng (2D của không gian nhiều chiều)

> **Random state:** `random_state=42` đảm bảo kết quả lặp lại được

---

## Workflow tổng quan

```
📁 Tải dữ liệu Excel
    ↓
🔍 Hiển thị và chọn cột số
    ↓
📊 Chuẩn hóa dữ liệu (StandardScaler)
    ↓
📈 Tính WCSS và Silhouette cho K=2..10
    ↓
📉 Vẽ Elbow Method → Gợi ý K tối ưu
    ↓
👤 Người dùng chọn K
    ↓
🤖 Chạy K-Means với K đã chọn
    ↓
📊 Tính tâm cụm và gán nhãn
    ↓
📋 Hiển thị bảng thống kê
    ↓
🎨 Trực quan hóa (PCA nếu >2 chiều)
    ↓
💾 Lưu kết quả vào Excel
```

---

## Cải tiến có thể thực hiện

- [ ] Thêm các thuật toán clustering khác (DBSCAN, Hierarchical)
- [ ] Hỗ trợ xử lý missing values
- [ ] Thêm Davies-Bouldin Index để đánh giá
- [ ] Export báo cáo PDF với biểu đồ
- [ ] Hỗ trợ dữ liệu categorical (one-hot encoding)
- [ ] Tích hợp K-Means++ initialization
- [ ] Thêm mini-batch K-Means cho dữ liệu lớn
- [ ] Visualization 3D với Plotly

---

## Ứng dụng thực tế

### 1. Phân khúc khách hàng (Customer Segmentation)

- Phân nhóm khách hàng theo thu nhập, tuổi, thói quen mua hàng
- Tạo chiến lược marketing riêng cho từng nhóm

### 2. Phân tích hành vi

- Nhóm người dùng theo hành vi trên website/app
- Cá nhân hóa trải nghiệm người dùng

### 3. Phát hiện bất thường (Anomaly Detection)

- Điểm nào không thuộc cụm nào → có thể là outlier
- Phát hiện giao dịch gian lận

### 4. Nén dữ liệu (Data Compression)

- Thay mỗi điểm bằng tâm cụm gần nhất
- Giảm kích thước dữ liệu
