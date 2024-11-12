from abc import ABC, abstractmethod
from src.core.models.cliente_domain import ClienteDomain

class IClienteRepository(ABC):

    @abstractmethod
    async def get(self, id: int) -> ClienteDomain:
        pass

    @abstractmethod
    async def create(self, cliente: ClienteDomain) -> int:
        pass

    @abstractmethod
    async def update(self, idCliente: int, cliente: ClienteDomain) -> bool:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_all(self) -> list[ClienteDomain]:
        pass
