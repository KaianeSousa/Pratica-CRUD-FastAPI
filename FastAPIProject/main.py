
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

class Recebedor(BaseModel):
    id: int
    nome: str
    idade: int
    tipo_sanguineo: str
    necessidades_de_sangue: str

doadores: List[Doador] = []
recebedores: List[Recebedor] = []

@app.get("/doadores", response_model=Dict[str, Union[str, List[Doador]]])
@app.get("/doadores/{doador_id}")
def listar_doadores(doador_id: Optional[int] = None):
    if doador_id is None:
        if not doadores:
            raise HTTPException(status_code=404, detail="Nenhum doador encontrado.")
        return {"mensagem": "Lista de todos os doadores disponíveis:", "doadores": doadores}

    doador = next((d for d in doadores if d.id == doador_id), None)
    if doador:
        return {"mensagem": "Doador encontrado com sucesso:", "doador": doador}
    raise HTTPException(status_code=404, detail="Doador não encontrado")

@app.get("/recebedores", response_model=Dict[str, Union[str, List[Recebedor]]])
@app.get("/recebedores/{recebedor_id}")
def listar_recebedores(recebedor_id: Optional[int] = None):
    if recebedor_id is None:
        if not recebedores:
            raise HTTPException(status_code=404, detail="Nenhum recebedor encontrado.")
        return {"mensagem": "Lista de todos os recebedores disponíveis:", "recebedores": recebedores}

    recebedor = next((r for r in recebedores if r.id == recebedor_id), None)
    if recebedor:
        return {"mensagem": "Recebedor encontrado com sucesso:", "recebedor": recebedor}
    raise HTTPException(status_code=404, detail="Recebedor não encontrado")

@app.post("/doadores/adicionar", response_model=Dict[str, Union[str, Doador]])
def adicionar_doador(doador: Doador):
    if any(d.id == doador.id for d in doadores):
        raise HTTPException(status_code=400, detail=f"Já existe um doador com este ID: {doador.id}")
    if not (16 <= doador.idade <= 69):
        raise HTTPException(status_code=400, detail="Idade inválida! O doador deve ter entre 16 e 69 anos.")
    doadores.append(doador)
    return {"mensagem": "Doador cadastrado com sucesso:", "doador": doador}

@app.post("/recebedores/adicionar", response_model=Dict[str, Union[str, Recebedor]])
def adicionar_recebedor(recebedor: Recebedor):
    if any(r.id == recebedor.id for r in recebedores):
        raise HTTPException(status_code=400, detail=f"Já existe um recebedor com este ID: {recebedor.id}")
    if recebedor.idade < 1:
        raise HTTPException(status_code=400, detail="Idade inválida! O recebedor deve ter pelo menos 1 ano.")
    recebedores.append(recebedor)
    return {"mensagem": "Recebedor cadastrado com sucesso:", "recebedor": recebedor}

@app.put("/doadores/atualizar/{doador_id}", response_model=Dict[str, Union[str, Doador]])
def atualizar_doador(doador_id: int, doador_atualizado: Doador):
    for index, doador in enumerate(doadores):
        if doador.id == doador_id:
            if not (16 <= doador_atualizado.idade <= 69):
                raise HTTPException(status_code=400, detail="Idade inválida! O doador deve ter entre 16 e 69 anos.")
            doadores[index] = doador_atualizado
            return {"mensagem": "Dados do doador atualizados com sucesso:", "doador": doador_atualizado}
    raise HTTPException(status_code=404, detail="Doador não encontrado")

@app.put("/recebedores/atualizar/{recebedor_id}", response_model=Dict[str, Union[str, Recebedor]])
def atualizar_recebedor(recebedor_id: int, recebedor_atualizado: Recebedor):
    for index, recebedor in enumerate(recebedores):
        if recebedor.id == recebedor_id:
            recebedores[index] = recebedor_atualizado
            return {"mensagem": "Dados do recebedor atualizados com sucesso:", "recebedor": recebedor_atualizado}
    raise HTTPException(status_code=404, detail="Recebedor não encontrado")

@app.delete("/doadores/{doador_id}")
def deletar_doador(doador_id: int):
    for index, doador in enumerate(doadores):
        if doador.id == doador_id:
            del doadores[index]
            return {"detail": "Doador removido com sucesso"}
    raise HTTPException(status_code=404, detail="Doador não encontrado")

@app.delete("/recebedores/{recebedor_id}")
def deletar_recebedor(recebedor_id: int):
    for index, recebedor in enumerate(recebedores):
        if recebedor.id == recebedor_id:
            del recebedores[index]
            return {"detail": "Recebedor removido com sucesso"}
    raise HTTPException(status_code=404, detail="Recebedor não encontrado")


class Doacao(BaseModel):
    doador_id: int
    recebedor_id: int

@app.post("/doacao", response_model=Dict[str, str])
def realizar_doacao(doacao: Doacao):
    doador = next((d for d in doadores if d.id == doacao.doador_id), None)
    recebedor = next((r for r in recebedores if r.id == doacao.recebedor_id), None)

    if not doador:
        raise HTTPException(status_code=404, detail="Doador não encontrado")
    if not recebedor:
        raise HTTPException(status_code=404, detail="Recebedor não encontrado")

    tabelaDeCompatibilidade = {
        "O-": {"doa_para": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], "recebe_de": ["O-"]},
        "O+": {"doa_para": ["A+", "B+", "AB+", "O+"], "recebe_de": ["O+", "O-"]},
        "A-": {"doa_para": ["A+", "A-", "AB+", "AB-"], "recebe_de": ["A-", "O-"]},
        "A+": {"doa_para": ["A+", "AB+"], "recebe_de": ["A+", "A-", "O+", "O-"]},
        "B-": {"doa_para": ["B+", "B-", "AB+", "AB-"], "recebe_de": ["B-", "O-"]},
        "B+": {"doa_para": ["B+", "AB+"], "recebe_de": ["B+", "B-", "O+", "O-"]},
        "AB-": {"doa_para": ["AB+", "AB-"], "recebe_de": ["A-", "B-", "AB-", "O-"]},
        "AB+": {"doa_para": ["AB+"], "recebe_de": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},
        "Rh-nulo": {"doa_para": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Rh-nulo"], "recebe_de": ["Rh-nulo"]},
    }

    tipo_doador = doador.tipo_sanguineo
    tipo_recebedor = recebedor.tipo_sanguineo

    if tipo_recebedor not in tabelaDeCompatibilidade[tipo_doador]["doa_para"]:
        raise HTTPException(
            status_code=400,
            detail=f"Incompatibilidade: {tipo_doador} não pode doar para {tipo_recebedor}"
        )
    if tipo_doador not in tabelaDeCompatibilidade[tipo_recebedor]["recebe_de"]:
        raise HTTPException(
            status_code=400,
            detail=f"Incompatibilidade: {tipo_recebedor} não pode receber de {tipo_doador}"
        )

    return {"mensagem": f"Doação compatível de {doador.nome} para {recebedor.nome}"}
