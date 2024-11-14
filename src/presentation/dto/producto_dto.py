from pydantic import BaseModel


class ProductoDTO(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    descuento: float
    imagen: str
    stock: int
    idCategoria:int