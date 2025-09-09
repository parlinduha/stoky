from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class BarangBase(BaseModel):
    nama: str
    deskripsi: str
    jumlah: int
    harga: float

class BarangCreate(BarangBase):
    pass

class BarangResponse(BarangBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True