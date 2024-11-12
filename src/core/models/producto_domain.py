from typing import Optional

from pydantic import BaseModel

class ProductoDomain(BaseModel):
    idProducto: Optional[int] = None
    nombre: str
    descripcion: str
    precio: float
    descuento: float
    imagen: bytes
    stock: int