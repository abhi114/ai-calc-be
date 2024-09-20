from contextlib import asynccontextmanager; #This function is a decorator that can be used to define a factory function for with statement context managers, without needing to create a class or separate __enter__() and __exit__() methods.
from fastapi import FastAPI #FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
from fastapi.middleware.cors import CORSMiddleware
import uvicorn #Uvicorn is an ASGI web server implementation for Python.
from constants import SERVER_URL,PORT,ENV
from apps.calculator.route import router as calculator_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    return {"message": "Server is running"}

app.include_router(calculator_router,prefix='/calculate',tags=['calculate'])
if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=10000,reload=(ENV=='dev'))