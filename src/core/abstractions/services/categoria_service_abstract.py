from abc import ABC, abstractmethod
from src.core.models.categoria_domain import CategoriaDomain


class ICategoriaService(ABC):

    @abstractmethod
    async def get_all_categoria(self) -> list[CategoriaDomain]:
        pass

    @abstractmethod
    async def get_categoria(self, idCategoria: int) -> CategoriaDomain:
        pass
    @abstractmethod
    async def create_categoria(self, categoria: CategoriaDomain) -> CategoriaDomain:
        pass

    @abstractmethod
    async def update_categoria(self, categoria: CategoriaDomain) -> CategoriaDomain:
        pass

    @abstractmethod
    async def delete_categoria(self, idCategoria: int) -> None:
        pass