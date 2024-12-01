from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union, Dict, Optional

app = FastAPI()


class Doador(BaseModel):
    id: int
    nome: str
    idade: int
    tipo_sanguineo: str
    data_da_ultima_doacao: str


doadores: List[Doador] = []


@app.get("/doadores", response_model=Union[Dict[str, Union[str, List[Doador]]], Dict[str, Union[str, Doador]]])
@app.get("/doadores/{doador_id}")
def listar_doadores(doador_id: Optional[int] = None):
    if doador_id is None:
        if not doadores:
            raise HTTPException(status_code=404, detail="Nenhum doador encontrado.")
        return {"mensagem": "Lista de todos os doadores disponíveis:", "doadores": doadores}

    for doador in doadores:
        if doador.id == doador_id:
            return {"mensagem": "Doador encontrado com sucesso:", "doador": doador}

    raise HTTPException(status_code=404, detail="Doador não encontrado")


@app.post("/doadores/adicionar", response_model=Dict[str, Union[str, Doador]])
def adicionar_doador(doador: Doador):
    for existente in doadores:
        if existente.id == doador.id:
            raise HTTPException(status_code=400, detail=f"Já existe um doador com este ID: {doador.id}")
    if doador.idade < 16 or doador.idade > 69:
        raise HTTPException(status_code=400, detail="Idade inválida! O doador deve ter entre 16 e 69 anos.")
    doadores.append(doador)
    return {"mensagem": "Doador cadastrado com sucesso:", "doador": doador}


@app.put("/doadores/atualizar/{doador_id}", response_model=Dict[str, Union[str, Doador]])
def atualizar_doador(doador_id: int, doador_atualizado: Doador):
    for index, doador in enumerate(doadores):
        if doador.id == doador_id:
            if doador_atualizado.idade < 16 or doador_atualizado.idade > 69:
                raise HTTPException(status_code=400, detail="Idade inválida! O doador deve ter entre 16 e 69 anos.")
            doadores[index] = doador_atualizado
            return {"mensagem": "Dados do doador atualizados com sucesso:", "doador": doador_atualizado}
    raise HTTPException(status_code=404, detail="Doador não encontrado")


@app.delete("/doadores/{doador_id}")
def deletar_doador(doador_id: int):
    for index, doador in enumerate(doadores):
        if doador.id == doador_id:
            del doadores[index]
            return {"detail": "Doador removido com sucesso"}
    raise HTTPException(status_code=404, detail="Doador não encontrado")
