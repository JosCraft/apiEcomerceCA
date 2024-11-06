from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

@dataclass
class ExampleDTO:
    name: str
    age: int
    email: Optional[str] = None
