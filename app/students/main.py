from fastapi import FastAPI
from routers.student_router import router as student_router

app = FastAPI(title="Taller Evaluado 001")

app.include_router(student_router)