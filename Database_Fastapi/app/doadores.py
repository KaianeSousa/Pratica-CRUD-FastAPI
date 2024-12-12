from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.DoadorBase])
def listar_doadores(db: Session = Depends(get_db)):
    return db.query(models.Doador).all()

@router.get("/{doador_id}", response_model=schemas.DoadorBase)
def pesquisar_doador_por_id(doador_id: int, db: Session = Depends(get_db)):
    doador = crud.get_doador(db, doador_id)
    if not doador:
        raise HTTPException(status_code=404, detail="Doador não encontrado")
    return doador

@router.post("/adicionar", response_model=schemas.DoadorBase)
def adicionar_doador(doador: schemas.DoadorBase, db: Session = Depends(get_db)):
    if doador.idade < 16 or doador.idade > 69:
        raise HTTPException(status_code=400, detail="Doador deve ter entre 16 e 69 anos")
    return crud.create_doador(db=db, doador=doador)

@router.put("/atualizar/{doador_id}", response_model=schemas.DoadorBase)
def atualizar_doador(doador_id: int, doador: schemas.DoadorBase, db: Session = Depends(get_db)):
    doador_existente = crud.get_doador(db, doador_id)
    if not doador_existente:
        raise HTTPException(status_code=404, detail="Doador não encontrado")
    return crud.update_doador(db=db, id=doador_id, doador=doador)

@router.delete("/deletar/{doador_id}")
def deletar_doador(doador_id: int, db: Session = Depends(get_db)):
    doador_existente = crud.get_doador(db, doador_id)
    if not doador_existente:
        raise HTTPException(status_code=404, detail="Doador não encontrado")
    crud.delete_doador(db=db, id=doador_id)
    return {"message": f"Doador {doador_id} deletado com sucesso"}
