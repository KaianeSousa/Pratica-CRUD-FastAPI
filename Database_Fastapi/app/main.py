from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app import doadores, recebedores, doacoes

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doadores.router, tags=["Doadores"], prefix="/doadores")
app.include_router(recebedores.router, tags=["Recebedores"], prefix="/recebedores")
app.include_router(doacoes.router, tags=["Doações"], prefix="/doacoes")

@app.get("/app/healthchecker")
def root():
    return {"message": "API funcionando com sucesso!"}
