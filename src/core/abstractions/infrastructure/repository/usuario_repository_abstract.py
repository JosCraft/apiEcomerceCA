from abc import ABC, abstractmethod

from src.core.models.usuario_domain import UsuarioDomain


class IUsuarioRepository(ABC):
    @abstractmethod
    async def create(self, usuario: UsuarioDomain) -> UsuarioDomain:
        pass

    @abstractmethod
    async def update(self, usuario: UsuarioDomain) -> UsuarioDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def login(self, email: str, password: str) -> bool:
        pass
