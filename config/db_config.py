import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field  # Import Field untuk validasi

# Muat variabel lingkungan dari file .env
load_dotenv()


class Settings(BaseSettings):
    # Definisikan variabel-variabel yang diperlukan
    dbhost: str = Field(..., env="DBHOST")
    dbport: str = Field(..., env="DBPORT")
    dbname: str = Field(..., env="DBNAME")
    dbuser: str = Field(..., env="DBUSER")
    dbpassword: str = Field(..., env="DBPASSWORD")
    secret_key: str = Field(default="your_secret_key", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Hitung DATABASE_URL berdasarkan variabel di atas
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.dbuser}:{self.dbpassword}@{self.dbhost}:{self.dbport}/{self.dbname}"

# Buat instance settings
settings = Settings()