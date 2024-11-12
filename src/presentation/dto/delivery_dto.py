from pydantic import BaseModel

class DeliveryDTO(BaseModel):
    nombre: str
    turno: str
    email: str
    estado: str
    ubicacion: str
    password: str