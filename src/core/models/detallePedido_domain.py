from pydantic import BaseModel
from typing import Optional

class DetallePedidoDomain(BaseModel):
    idDetalle: Optional[int] = None
    idPedido: int
    idProducto: int
    cantidad: int
    subtotal: float