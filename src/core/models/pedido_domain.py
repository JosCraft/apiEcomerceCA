from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PedidoDomain(BaseModel):

    idPedido: Optional[int] = None
    fecha: date
    estado: str
    total: float
    idCliente: int