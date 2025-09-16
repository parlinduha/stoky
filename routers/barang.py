from fastapi import APIRouter, Depends
from controllers.BarangController import BarangController
from schemas.barang_schema import BarangCreate, BarangResponse
from config.db import get_db
from models.user import User
from utils.auth import get_current_active_user, check_staff, check_admin

class BarangRouter:
    def __init__(self):
        self.router = APIRouter()
        self.barang_controller = BarangController()
        self.setup_routes()

    def setup_routes(self):
        self.router.add_api_route(
            "/", 
            self.get_all_barang, 
            methods=["GET"],
            response_model=list[BarangResponse]  # Sesuaikan dengan response model yang tepat
        )
        self.router.add_api_route(
            "/{barang_id}", 
            self.get_barang_by_id, 
            methods=["GET"],
            response_model=BarangCreate  # Sesuaikan dengan response model yang tepat
        )
        self.router.add_api_route(
            "/", 
            self.create_barang, 
            methods=["POST"],
            response_model=BarangCreate  # Sesuaikan dengan response model yang tepat
        )
        self.router.add_api_route(
            "/{barang_id}", 
            self.update_barang, 
            methods=["PUT"],
            response_model=BarangCreate  # Sesuaikan dengan response model yang tepat
        )
        self.router.add_api_route(
            "/{barang_id}", 
            self.delete_barang, 
            methods=["DELETE"]
        )
    
    async def get_all_barang(
        self, 
        db = Depends(get_db),
    ):
        return self.barang_controller.get_all(db)

    async def get_barang_by_id(
        self, 
        barang_id: int,
        db = Depends(get_db),
        user: User = Depends(get_current_active_user)
    ):
        return self.barang_controller.get_by_id(barang_id, db, user)
    
    async def create_barang(
        self, 
        barang: BarangCreate,
        db = Depends(get_db)
    ):
        return self.barang_controller.create(barang, db)
    
    async def update_barang(
        self, 
        barang_id: int, 
        barang: BarangCreate,
        db = Depends(get_db),
        user: User = Depends(check_staff)
    ):
        return self.barang_controller.update(barang_id, barang, db, user)
    
    async def delete_barang(
        self, 
        barang_id: int,
        db = Depends(get_db),
        user: User = Depends(check_admin)
    ):
        return self.barang_controller.delete(barang_id, db, user)

# Create instance
barang_router = BarangRouter()
router = barang_router.router
