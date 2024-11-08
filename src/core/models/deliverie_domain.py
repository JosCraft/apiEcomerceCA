from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
class deliveriePedidoDomain(BaseModel):
    idUsuario:int
    idDeliverie:int
    servicio:str
    turno:str
    idComunidad:Optional[int] = None