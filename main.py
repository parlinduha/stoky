from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, barang, transaksi
from config.db import engine, Base

class App:
    def __init__(self):
        self.app = FastAPI()
        self._setup_cors()
        self._setup_routes()
        self._create_tables()

    def _setup_cors(self):
        """Configure CORS middleware."""
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _setup_routes(self):
        """Include all routers."""
        self.app.include_router(auth.router)
        self.app.include_router(barang.barang_router)
        self.app.include_router(transaksi.router)

        @self.app.get("/")
        def read_root():
            return {"message": "Welcome to Stoky API"}

    def _create_tables(self):
        """Create all database tables."""
        Base.metadata.create_all(bind=engine)

    def get_app(self):
        """Return the FastAPI app instance."""
        return self.app

# Initialize the app
app = FastAPIApp().get_app()
