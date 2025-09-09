class TransaksiController:
    def get_all(self):
        return {"message": "Get all transaksi"}
    
    def get_by_id(self, id: int):
        return {"message": f"Get transaksi by id {id}"}
    
    def create(self):
        return {"message": "Create transaksi"}
    
    def update(self, id: int):
        return {"message": f"Update transaksi by id {id}"}
    
    def delete(self, id: int):
        return {"message": f"Delete transaksi by id {id}"}