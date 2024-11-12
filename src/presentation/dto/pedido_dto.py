from pydantic import BaseModel, Field
from datetime import date
class PedidoDTO(BaseModel):
    fecha: date
    estado: str
    total: float
    idCliente: int