from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

# IMPORTACIÓN DE ROUTES
from routes.auth_routes import router as auth_router
from routes.category_routes import router as category_router
from routes.book_routes import router as book_router
from routes.history_routes import router as history_router
from routes.user_routes import router as user_router
from routes.favorite_routes import router as favorite_router
from routes.event_routes import router as event_router
from routes.event_reservation_routes import router as event_reservation_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTRO DE ROUTES
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(book_router)
app.include_router(user_router)
app.include_router(history_router)
app.include_router(favorite_router)
app.include_router(event_router)
app.include_router(event_reservation_router)