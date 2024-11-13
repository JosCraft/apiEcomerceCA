from pydantic import BaseModel
from typing import Optional

class CategoriaDomain(BaseModel):
    idCategoria: Optional[int] = None
    nombreCategoria:str
