from pydantic import BaseModel
from typing import Optional


class ExampleDomain(BaseModel):
    id: Optional[int] = None
    nombre: str
    medida: str




