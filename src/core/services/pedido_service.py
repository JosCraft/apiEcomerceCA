from src.core.abstractions.infrastructure.repository.pedido_repository_abstract import IPedidoRepository
from src.core.abstractions.services.pedido_service_abstract import IPedidoService
from src.core.models.pedido_domain import PedidoDomain


class PedidoService(IPedidoService):

    def __init__(self, pedido_repository: IPedidoRepository):
        self.pedido_repository = pedido_repository

    async def get_pedido(self, idPedido: int) -> PedidoDomain:
        return await self.pedido_repository.get(idPedido)

    async def create_pedido(self, pedido: PedidoDomain) -> PedidoDomain:
        return await self.pedido_repository.create(pedido)

    async def update_pedido(self, idPedido: int, pedido: PedidoDomain) -> PedidoDomain:
        return await self.pedido_repository.update(idPedido, pedido)

    async def delete_pedido(self, idPedido: int) -> None:
        return await self.pedido_repository.delete(idPedido)

    async def get_all_pedidos(self) -> list[PedidoDomain]:
        return await self.pedido_repository.get_all()

