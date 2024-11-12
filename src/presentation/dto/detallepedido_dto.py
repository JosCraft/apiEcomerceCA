from pydantic import BaseModel

class DetallePedidoDTO(BaseModel):
    idPedido: int
    idProducto: int
    cantidad: int
    subtotal: float