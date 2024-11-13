from src.core.abstractions.infrastructure.repository.categoria_repository_abstract import ICategoriaRepository
from src.core.abstractions.services.categoria_service_abstract import ICategoriaService
from src.core.models.categoria_domain import CategoriaDomain


class ProductoService(ICategoriaService):

    def __init__(self, categoria_repository: ICategoriaRepository):
        self.categoria_repository = categoria_repository

    async def get_producto(self, idCategoria: int) -> CategoriaDomain:
        return await self.categoria_repository.get(idCategoria)

    async def create_producto(self, categoria: CategoriaDomain) -> CategoriaDomain:
        return await self.categoria_repository.create(categoria)

    async def update_producto(self, idCategoria: int, categoria: CategoriaDomain) -> CategoriaDomain:
        return await self.categoria_repository.update(idCategoria, categoria)

    async def delete_producto(self, idCategoria: int) -> None:
        return await self.categoria_repository.delete(idCategoria)

    async def get_all_productos(self) -> list[CategoriaDomain]:
        return await self.categoria_repository.get_all()