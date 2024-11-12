from abc import ABC, abstractmethod
from src.core.models.producto_domain import ProductoDomain


class IProductoRepository(ABC):

    @abstractmethod
    async def get_all(self) -> list[ProductoDomain]:
        pass

    @abstractmethod
    async def get(self, id: int) -> ProductoDomain:
        pass

    @abstractmethod
    async def create(self, producto: ProductoDomain) -> ProductoDomain:
        pass

    @abstractmethod
    async def update(self, producto: ProductoDomain) -> ProductoDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass
