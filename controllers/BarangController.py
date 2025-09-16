from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from utils.database import get_db
from models.barang import Barang
from schemas.barang_schema import BarangCreate, BarangResponse
from utils.auth import get_current_active_user, check_admin, check_staff, check_supervisor
from models.user import User

class BarangController:
        
    def create(self, barang: BarangCreate, db: Session = Depends(get_db)):
        """Create a new barang"""
        db_barang = Barang(**barang.dict())
        db.add(db_barang)
        db.commit()
        db.refresh(db_barang)
        return db_barang

    def get_all(
        self,
        db: Session = Depends(get_db)
    ):
        """Get all barang with pagination"""
        return db.query(Barang).all()

    def get_by_id(
        self,
        barang_id: int,
        db: Session = Depends(get_db),
        user: User = Depends(get_current_active_user)
    ):
        """Get barang by ID"""
        db_barang = db.query(Barang).filter(Barang.id == barang_id).first()
        if db_barang is None:
            raise HTTPException(status_code=404, detail="Barang not found")
        return db_barang

    def update(
        self,
        barang_id: int,
        barang: BarangCreate,
        db: Session = Depends(get_db),
        user: User = Depends(check_staff)
    ):
        """Update barang by ID"""
        db_barang = db.query(Barang).filter(Barang.id == barang_id).first()
        if db_barang is None:
            raise HTTPException(status_code=404, detail="Barang not found")
        
        for var, value in barang.dict().items():
            setattr(db_barang, var, value)
        
        db.commit()
        db.refresh(db_barang)
        return db_barang

    def delete(
        self,
        barang_id: int,
        db: Session = Depends(get_db),
        user: User = Depends(check_admin)
    ):
        """Delete barang by ID"""
        db_barang = db.query(Barang).filter(Barang.id == barang_id).first()
        if db_barang is None:
            raise HTTPException(status_code=404, detail="Barang not found")
        
        db.delete(db_barang)
        db.commit()
        return {"message": "Barang deleted successfully"}