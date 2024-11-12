from abc import ABC, abstractmethod
from src.core.models.detallePedido_domain import DetallePedidoDomain

class IDetallePedidoRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def create(self, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def update(self, id: int, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def get_all(self) -> list[DetallePedidoDomain]:
        pass


