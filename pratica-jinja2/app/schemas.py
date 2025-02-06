from pydantic import BaseModel
from typing import List, Optional

class Admin(BaseModel):
    nome: str
    email: str
    senha: str

    class Config:
        from_attribute = True
        populate_by_name = True
        from_attributes = True

class DoadorBase(BaseModel):
    nome: str
    idade: int
    tipo_sanguineo: str
    data_da_ultima_doacao: str

    class Config:
        from_attribute = True
        populate_by_name = True
        from_attributes = True

class RecebedorBase(BaseModel):
    nome: str
    idade: int
    tipo_sanguineo: str
    necessidades_de_sangue: str

    class Config:
        from_attribute = True
        populate_by_name = True
        from_attributes = True
