```
stoky/
├── __pycache__/
├── config/
│   ├── __init__.py
│   └── db.py         # Database configuration
├── controllers/
│   ├── AuthController.py
│   └── BarangController.py
├── main.py           # Main application
├── models/
│   ├── __init__.py
│   ├── user.py       # User model
│   └── barang.py     # Item model
├── routes/
│   ├── __init__.py
│   ├── auth.py       # Authentication routes
│   └── barang.py     # Item routes
├── schemas.py        # Pydantic schemas
├── utils/
│   ├── __init__.py
│   ├── auth.py       # Authentication utilities
│   └── database.py   # Database utilities
└── requirements.txt  # Dependencies
```


## 🚀 Instalasi

1. Clone repository:

   ```bash
        git clone https://github.com/parlinduha/stoky.git
        cd stoky
    ```
2. Buat virtual environment:

    ```bash
        python -m venv venv
    ```
3. Aktifkan virtual environment:
    * Linux/MacOS

        ```bash
            source venv/bin/activate
        ```
    * Windows (PowerShell/Command Prompt)

        ```bash
            .\\venv\\Scripts\\activate
        ```
    * Windows (CMD .bat)

        ```bash
            ./venv/Script/activate.bat
        ```
4. Install dependencies:

    ```bash
        pip install -r requirements.txt
    ```

▶️ Menjalankan Aplikasi
1. Dengan FastAPI CLI:

    ```bash
        fastapi dev main.py 
    ```

2. Dengan Uvicorn (opsional):

    ```bash
        uvicorn main:app   --reload (Optional)
    ```

Aplikasi akan berjalan di:
    👉 http://127.0.0.1:8000

    👉 Dokumentasi Swagger: http://127.0.0.1:8000/docs

    🛠️ Migrasi Database (Alembic)

1. Inisialisasi Alembic:

    ```bash
        alembic init alembic 
    ```

2. Buat revision baru (misalnya untuk menambahkan transaksi):

    ```bash
        alembic revision --autogenerate -m "add transaksi"
    ```

3. Terapkan migrasi ke database:

    ```bash
        alembic upgrade head
    ```
📌 Catatan

Pastikan sudah mengatur konfigurasi database di config/db.py sebelum menjalankan migrasi.

Gunakan environment variables untuk menyimpan kredensial database agar lebih aman.