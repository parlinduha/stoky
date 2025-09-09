from fastapi import APIRouter
from controllers.TransaksiController import TransaksiController


class TransaksiRouter:
    def __init__(self):
        self.router = APIRouter()
        self.transaksi_controller = TransaksiController()
        self.setup_routes()

    def setup_routes(self):
        self.router.add_api_route("/", self.transaksi_controller.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.transaksi_controller.get_by_id, methods=["GET"])
    
    async def get_all(self):
        return self.transaksi_controller.get_all()
    
    async def get_by_id(self, id: int):
        return self.transaksi_controller.get_by_id(id)

