from pydantic import BaseModel


class ProductoDTO(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    descuento: float
    imagen: bytes
    stock: int
    idCategoria:int