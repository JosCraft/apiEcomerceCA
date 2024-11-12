from pydantic import BaseModel
from typing import Optional
class DeliveryDomain(BaseModel):
    idDelivery: Optional[int] = None
    nombre: str
    turno: str
    email: str
    estado: str
    ubicacion: str
    password: str

