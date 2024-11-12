from src.core.abstractions.infrastructure.repository.producto_repository_abstract import IProductoRepository
from src.core.abstractions.services.producto_service_abstract import IProductoService
from src.core.models.producto_domain import ProductoDomain


class ProductoService(IProductoService):

    def __init__(self, producto_repository: IProductoRepository):
        self.producto_repository = producto_repository

    async def get_producto(self, idProducto: int) -> ProductoDomain:
        return await self.producto_repository.get(idProducto)

    async def create_producto(self, producto: ProductoDomain) -> ProductoDomain:
        return await self.producto_repository.create(producto)

    async def update_producto(self, idProducto: int, producto: ProductoDomain) -> ProductoDomain:
        return await self.producto_repository.update(idProducto, producto)

    async def delete_producto(self, idProducto: int) -> None:
        return await self.producto_repository.delete(idProducto)

    async def get_all_productos(self) -> list[ProductoDomain]:
        return await self.producto_repository.get_all()