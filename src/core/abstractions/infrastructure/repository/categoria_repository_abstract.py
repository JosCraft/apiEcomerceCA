from abc import ABC, abstractmethod
from src.core.models.categoria_domain import CategoriaDomain


class ICategoriaRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[CategoriaDomain]:
        pass

    @abstractmethod
    async def get(self, id: int) -> CategoriaDomain:
        pass

    @abstractmethod
    async def create(self, categoria: CategoriaDomain) -> CategoriaDomain:
        pass

    @abstractmethod
    async def update(self, categoria: CategoriaDomain) -> CategoriaDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass