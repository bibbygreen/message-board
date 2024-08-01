from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import board_routes


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(board_routes.router)
