from pydantic import BaseModel

class ContratoFuncionarios(BaseModel):
    id : int
    nome : str
    idade : int
    datanascimento : str
    email : str
    cargo : str
    departamento : str
