from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime


class DesignaDomain(BaseModel):
    idDeliverie:int
    idPedido:int
    ubicacion:str
