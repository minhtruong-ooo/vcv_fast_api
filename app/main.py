from fastapi import FastAPI
from app.api import hello

app = FastAPI()

# Include routes
app.include_router(hello.router, prefix="/api")