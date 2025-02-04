from fastapi import APIRouter, HTTPException, Depends
from app.schemas import LoginSchema
from app.auth import gerar_token, verificar_senha
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import Usuario

router = APIRouter()

@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    
    if not usuario or not verificar_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = gerar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}
