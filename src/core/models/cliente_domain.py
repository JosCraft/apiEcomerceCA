from pydantic import BaseModel
from typing import Optional

class ClienteDomain(BaseModel):
    idCliente: Optional[int] = None
    nombre: str
    direccion: str
    telefono: int
    email: str
    password: str

