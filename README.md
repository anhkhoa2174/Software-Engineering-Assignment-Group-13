# Software Engineering Assignment - Group 13

## Project Setup Instructions

### 1. Clone Repository
- Clone repository từ GitHub bằng lệnh sau:
    ```bash
    git clone https://github.com/anhkhoa2174/Software-Engineering-Assignment-Group-13
    ```
- **Lưu ý**: Nếu sử dụng folder dạng `.zip` tải về, bạn chỉ cần giải nén và bỏ qua bước này.

---

### 2. Điều Hướng vào Thư Mục Dự Án
- Di chuyển vào thư mục chứa dự án đã clone:
    ```bash
    cd Software-Engineering-Assignment-Group-13
    ```

---

### 3. Di Chuyển đến Backend Server
- Điều hướng qua các thư mục theo cấu trúc sau:
    ```bash
    cd react
    cd webpack
    cd public
    cd backend
    ```

---

### 4. Khởi Động Backend Server
- Chạy file `app.py` để khởi động backend server:
    ```bash
    python app.py
    ```

---

### 5. Thông Tin Tài Khoản Truy Cập

#### SPSO Account:
- Username: `duc_huy`  
- Password: `password456`  

#### Student Accounts:
| **Username**   | **Password**   |
|----------------|----------------|
| `khoa`        | `password123`  |
| `tien_dat`    | `password789`  |

---

### 6. Cấu Hình Cơ Sở Dữ Liệu (PostgreSQL)
- Nhóm sử dụng **PostgreSQL** cho cơ sở dữ liệu.  
- Script khởi tạo database nằm trong folder `db` với file **`cnpm.sql`**.  

- Để cài đặt cơ sở dữ liệu, chạy lệnh sau:
    ```bash
    psql -U <username> -d <database_name> -f db/cnpm.sql
    ```
    - Thay `<username>` bằng tên tài khoản PostgreSQL của bạn.  
    - Thay `<database_name>` bằng tên cơ sở dữ liệu mà bạn muốn tạo.

---

### 7. Ghi Chú
- Đảm bảo bạn đã cài đặt **Python** và **PostgreSQL** trên hệ thống của mình.  
- Nếu gặp vấn đề, vui lòng kiểm tra kết nối hoặc cấu hình trong file backend.

---

### 8. Liên Hệ
Nếu có câu hỏi hoặc cần hỗ trợ, vui lòng liên hệ nhóm:  
- **Leader**: Tran Anh Khoa  
- **Email**: khoa.trancs2174@hcmut.edu.vn
