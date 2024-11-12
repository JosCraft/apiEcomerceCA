
from abc import ABC, abstractmethod
from src.core.models.producto_domain import ProductoDomain


class IProductoService(ABC):

    @abstractmethod
    async def get_all_productos(self) -> list[ProductoDomain]:
        pass

    @abstractmethod
    async def get_producto(self, idProducto: int) -> ProductoDomain:
        pass
    @abstractmethod
    async def create_producto(self, producto: ProductoDomain) -> ProductoDomain:
        pass

    @abstractmethod
    async def update_producto(self, producto: ProductoDomain) -> ProductoDomain:
        pass

    @abstractmethod
    async def delete_producto(self, idProducto: int) -> None:
        pass

