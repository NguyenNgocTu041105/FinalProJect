# 🛒 E-Commerce Web Application - Django & Python

Hệ thống website thương mại điện tử và trang quản trị bán hàng toàn diện được phát triển bằng **Python & Django Framework** theo kiến trúc MVT, tích hợp **Django REST Framework (DRF)**.

---

## ✨ Tính năng nổi bật

### 1. Phân hệ Bán hàng & Trải nghiệm Người dùng
- **Tìm kiếm nâng cao (Advanced Search)**: Tìm kiếm sản phẩm theo tên, danh mục và từ khóa nhanh chóng.
- **Bộ lọc đa tiêu chí (Price Filter & Category)**: Lọc sản phẩm theo khoảng giá và danh mục thương hiệu kết hợp phân trang dữ liệu (Pagination).
- **Giỏ hàng & Đặt hàng**: Thêm/xóa/cập nhật giỏ hàng và đặt hàng trực tuyến.
- **Email tự động**: Tự động gửi email thông báo chi tiết đơn hàng đến khách hàng sau khi thanh toán.

### 2. Phân hệ Quản trị & CMS (Admin & Blog)
- **Quản lý sản phẩm**: Thêm, sửa, xóa sản phẩm, nhiều ảnh đại diện và quản lý trạng thái kho hàng.
- **Blog & Tin tức**: Hệ thống tin tức tích hợp trình soạn thảo nội dung phong phú **CKEditor 5**.
- **Đánh giá & Bình luận (Rating & Comments)**: Hệ thống chấm điểm sao và bình luận đa cấp độ cho bài viết.
- **Bảo mật & Phân quyền (Authentication & RBAC)**: Đăng ký, đăng nhập, bảo vệ CSRF và quy trình khôi phục mật khẩu qua Email Token an toàn.

### 3. Tích hợp RESTful API
- Xây dựng các API endpoint bằng **Django REST Framework (DRF)** với Serializers chuẩn hóa, sẵn sàng mở rộng cho ứng dụng di động hoặc Frontend SPA.

---

## 🛠️ Công nghệ sử dụng

- **Backend**: Python 3, Django, Django REST Framework (DRF)
- **Frontend**: Django Templates, HTML5/CSS3, JavaScript, Bootstrap
- **Thư viện nổi bật**: `django-ckeditor-5`, `Pillow`, `rest_framework`
- **Email Service**: SMTP Gmail
- **Database**: SQLite / PostgreSQL

---

## 🚀 Hướng dẫn cài đặt & Khởi chạy

### 1. Cài đặt môi trường
```bash
# Clone repository về máy
git clone https://github.com/NguyenNgocTu041105/FinalProJect.git
cd FinalProJect/shop_admin

# Cài đặt các thư viện cần thiết
pip install django djangorestframework django-ckeditor-5 pillow
```

### 2. Khởi chạy máy chủ
```bash
python manage.py migrate
python manage.py runserver
```
Truy cập ứng dụng tại: `http://127.0.0.1:8000/`
Trang quản trị: `http://127.0.0.1:8000/admin/`

---

## 👤 Tác giả
- **Nguyễn Ngọc Tú** - Sinh viên ngành Hệ thống Thông tin Quản lý, Trường Đại học Duy Tân
- GitHub: [@NguyenNgocTu041105](https://github.com/NguyenNgocTu041105)
