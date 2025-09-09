from fastapi import APIRouter
from controllers.BarangController import BarangController

class BarangRouter:
    def __init__(self):
        self.router = APIRouter()
        self.barang_controller = BarangController()
        self.setup_routes()

    def setup_routes(self):
        self.router.add_api_route("/", self.barang_controller.get_all, methods=["GET"])
        self.router.add_api_route("/{id}", self.barang_controller.get_by_id, methods=["GET"])
        