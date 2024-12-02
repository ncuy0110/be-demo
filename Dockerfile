# Sử dụng image chính thức của Python làm base image
FROM python:3.12.7-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container (nếu bạn có file requirements.txt)
COPY requirements.txt .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn của dự án vào container
COPY . .

# Mở port mà ứng dụng FastAPI sẽ chạy trên đó
EXPOSE 8000

# Lệnh để chạy ứng dụng với Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

