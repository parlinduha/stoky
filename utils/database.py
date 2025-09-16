from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config.db_config import settings  # Import settings


class Database:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = settings.database_url
        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            pool_size=20,  # Jumlah koneksi yang dibuka secara default
            max_overflow=40,  # Jumlah maksimum koneksi yang dapat dibuka selain pool_size
            pool_timeout=30,  # Waktu maksimum untuk menunggu koneksi
            pool_recycle=1800  # Waktu untuk merecycle koneksi (dalam detik)
        )
        self.SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))
        self.Base = declarative_base()

    def get_db(self):
        db = self.SessionLocal()

        try:
            # print(f"db connection")
            yield db
        finally:
            # print(f"db closed")
            db.close()

# Inisialisasi instance Database
db_instance = Database()

# Gunakan instance Database untuk mendapatkan engine, SessionLocal, Base, dan get_db
engine = db_instance.engine
SessionLocal = db_instance.SessionLocal
Base = db_instance.Base
get_db = db_instance.get_db
