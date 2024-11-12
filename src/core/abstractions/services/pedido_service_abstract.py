from abc import ABC, abstractmethod
from src.core.models.pedido_domain import PedidoDomain
class IPedidoService(ABC):

    @abstractmethod
    async def get_pedido(self, idPedido: int) -> PedidoDomain:
        pass

    @abstractmethod
    async def create_pedido(self, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def update_pedido(self, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def delete_pedido(self, idPedido: int) -> None:
        pass

    @abstractmethod
    async def get_all_pedidos(self) -> list[PedidoDomain]:
        pass

