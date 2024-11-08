from abc import ABC, abstractmethod

from src.core.models.pedido_domain import PedidoDomain


class IPedidoRepository(ABC):

    @abstractmethod
    async def create(self, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def update(self, id:int, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

