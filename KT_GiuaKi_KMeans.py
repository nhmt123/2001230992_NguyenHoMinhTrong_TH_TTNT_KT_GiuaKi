import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from matplotlib.colors import ListedColormap
import sys

# --- HÀM VISUALIZE  ---
def visualize_kmeans(X_raw, labels, centers, k, selected_cols):
    plt.figure(figsize=(12, 8))
    
    # --- Xử lý PCA cho Dữ liệu Đa chiều  ---
    if X_raw.shape[1] > 2:
        pca = PCA(n_components=2)
        X_plot = pca.fit_transform(X_raw)
        centers_plot = pca.transform(centers)
        explained = pca.explained_variance_ratio_.sum() * 100
        print(f"Đang vẽ biểu đồ 2D bằng PCA (giải thích {explained:.1f}% biến thiên)")
    else:
        X_plot = X_raw
        centers_plot = centers
        
    unique_labels = np.unique(labels)
    num_unique_labels = len(unique_labels)

    # --- ĐỊNH NGHĨA MÀU  ---
    # Chọn Colormap có dải màu rộng (gist_rainbow)
    try:
        cmap_name = 'gist_rainbow'
        # Sử dụng 256 màu để đảm bảo đủ màu ngay cả khi K lớn
        cmap_full = plt.cm.get_cmap(cmap_name, 256) 
    except AttributeError:
        cmap_full = plt.colormaps['gist_rainbow']
        
    # Tạo danh sách K màu cách đều
    indices = np.linspace(0.01, 0.99, num_unique_labels, endpoint=True) 
    
    # Lấy màu từ cmap
    final_colors = [cmap_full(i) for i in indices]

    if num_unique_labels == 2:
        final_colors = [cmap_full(0.05), cmap_full(0.55)]

    # --- Vẽ Sơ đồ ---
    for i, label in enumerate(unique_labels):
        data = X_plot[labels == label]
        
        # Lấy màu đã được lọc và tăng độ tương phản
        plt.scatter(data[:, 0], data[:, 1],
                    label=f'Cụm {label} ({len(data)} khách)',
                    s=80, alpha=0.8, color=final_colors[i])
        
    plt.scatter(centers_plot[:, 0], centers_plot[:, 1],
                color='black', marker='X', s=300,
                label='Tâm cụm (Centroid)',
                edgecolors='white', linewidth=2)
    
    # --- Tiêu đề và Chú thích ---
    plt.title(f'K-Means: {k} cụm - Dùng {len(selected_cols)} đặc trưng: {", ".join(selected_cols)}')
    plt.xlabel('Trục chính 1' if X_raw.shape[1] > 2 else selected_cols[0])
    plt.ylabel('Trục chính 2' if X_raw.shape[1] > 2 else selected_cols[1])
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# --- CHƯƠNG TRÌNH CHÍNH ---
def run_kmeans_for_customer():
    file_path = 'du_lieu_khach_hang.xlsx'
    
    # --- TẢI DỮ LIỆU ---
    try:
        df_original = pd.read_excel(file_path)
        print(f"Đã tải file thành công!")
        print(f"   Số khách hàng: {len(df_original)}")
        print(f"   Số cột: {len(df_original.columns)}")
        
        # Lấy danh sách cột số (numeric) để phân cụm
        numeric_cols = df_original.select_dtypes(include=['number']).columns.tolist()
        
        if len(numeric_cols) < 2:
            print("LỖI: File cần ít nhất 2 cột số để thực hiện phân cụm.")
            sys.exit()
        
        print("\n" + "="*60)
        print("DANH SÁCH CÁC CỘT TRONG FILE")
        print("="*60)
        for i, col in enumerate(df_original.columns):
            status = " (số - có thể dùng)" if col in numeric_cols else " (không dùng được cho phân cụm)"
            print(f"  {i+1:2}. {col}{status}")
        print("="*60)
        
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file '{file_path}' trong thư mục hiện tại.")
        sys.exit()
    except Exception as e:
        print(f"LỖI khi đọc file: {e}")
        sys.exit()

    # --- NGƯỜI DÙNG CHỌN CỘT ---
    print("\nCHỌN CỘT ĐỂ PHÂN CỤM")
    print("Nhập tên các cột cần dùng, cách nhau bằng dấu phẩy.")
    print("Ví dụ: Cân nặng (kg), Chiều cao (cm), Thu nhập tháng, Tuổi")
    
    selected_input = input("\nNhập tên cột: ").strip()
    
    if not selected_input:
        print("Bạn chưa nhập gì. Thoát chương trình.")
        sys.exit()
    
    selected_cols = [col.strip() for col in selected_input.split(',')]
    
    # Kiểm tra tính hợp lệ
    valid_cols = []
    for col in selected_cols:
        if col in df_original.columns:
            if col in numeric_cols:
                valid_cols.append(col)
            else:
                print(f"   Cảnh báo: '{col}' không phải cột số --> bỏ qua.")
        else:
            print(f"   LỖI: Không tìm thấy cột '{col}' --> bỏ qua.")
    
    if len(valid_cols) < 2:
        print("LỖI: Cần chọn ít nhất 2 cột số hợp lệ để phân cụm.")
        sys.exit()
    
    print(f"\nĐã chọn {len(valid_cols)} cột để phân cụm:")
    for col in valid_cols:
        print(f"   • {col}")
    
    # Tạo DataFrame chỉ với các cột đã chọn
    df = df_original[valid_cols].copy()
    X_raw = df.values
    
    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X = scaler.fit_transform(X_raw)

    # --- TÌM K TỐI ƯU ---
    print("\nĐang tìm số cụm K tối ưu (có thể mất vài giây)...")
    wcss = []
    silhouette_scores = []
    max_k = min(10, len(X) - 1)
    K_range = range(2, max_k + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    
    # Vẽ Elbow Curve
    plt.figure(figsize=(10, 5))
    plt.plot(K_range, wcss, 'bo-')
    plt.title('Elbow Method - Tìm K tối ưu')
    plt.xlabel('Số cụm K')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.grid(True)
    plt.show()
    
    # K tối ưu theo Silhouette Score
    optimal_k = K_range[np.argmax(silhouette_scores)]
    best_silhouette = max(silhouette_scores)
    
    print(f"\nGỢI Ý: K tối ưu = {optimal_k} (Silhouette Score = {best_silhouette:.3f})")

    # --- NHẬP K TỪ NGƯỜI DÙNG ---
    try:
        user_k = input(f"\nNhập số cụm K bạn muốn (gợi ý {optimal_k}, hoặc số khác): ").strip()
        k = int(user_k) if user_k else optimal_k
        if k < 2 or k > len(X):
            print(f"K phải từ 2 đến {len(X)}. Tự động dùng K = {optimal_k}")
            k = optimal_k
    except:
        k = optimal_k
    
    print(f"\nĐang chạy K-Means với K = {k} cụm...")

    # --- CHẠY K-MEANS ---
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(X)
    labels = kmeans.labels_
    centers_scaled = kmeans.cluster_centers_
    centers = scaler.inverse_transform(centers_scaled)  # Chuyển về đơn vị gốc để dễ hiểu

    # --- TÓM TẮT KẾT QUẢ ---
    df_original['ID Cụm'] = labels
    
    print("\n" + "="*80)
    print("KẾT QUẢ PHÂN CỤM")
    print("="*80)
    
    summary = df_original.groupby('ID Cụm')[valid_cols].mean().round(2)
    summary['Số lượng khách'] = df_original['ID Cụm'].value_counts().sort_index()
    summary = summary[['Số lượng khách'] + valid_cols]
    
    print(summary)
    print("="*80)

    # --- VISUALIZE ---
    print("\nĐang hiển thị biểu đồ phân cụm...")
    print("Đóng cửa sổ biểu đồ để tiếp tục.")
    visualize_kmeans(X_raw, labels, centers, k, valid_cols)

    # --- LƯU KẾT QUẢ ---
    try:
        df_original.to_excel(file_path, index=False)
        print(f"\nĐÃ LƯU KẾT QUẢ!")
        print(f"   → Thêm cột 'ID Cụm' vào file '{file_path}'")
        print(f"   → Mỗi khách hàng giờ có nhãn cụm từ 0 đến {k-1}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

    print("\nCảm ơn bạn đã sử dụng chương trình phân cụm khách hàng!")
    print("Chương trình kết thúc.")

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    run_kmeans_for_customer()