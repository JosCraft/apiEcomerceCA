from pydantic import BaseModel
from typing import Optional
class clienteDTO(BaseModel):
    nombre: str
    direccion: Optional[str]
    telefono: Optional[int]
    email: str
    password: str