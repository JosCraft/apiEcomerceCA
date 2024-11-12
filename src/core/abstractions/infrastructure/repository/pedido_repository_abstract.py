from abc import ABC, abstractmethod
from src.core.models.pedido_domain import PedidoDomain

class IPedidoRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> PedidoDomain:
        pass

    @abstractmethod
    async def create(self, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def update(self, pedido: PedidoDomain) -> PedidoDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    async def get_all(self) -> list[PedidoDomain]:
        pass
