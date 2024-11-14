from abc import ABC, abstractmethod
from src.core.models.cliente_domain import ClienteDomain


class IClienteService(ABC):

    @abstractmethod
    async def get_cliente(self, idCliente: int) -> ClienteDomain:
        pass

    @abstractmethod
    async def create_cliente(self, cliente: ClienteDomain) -> ClienteDomain:
        pass

    @abstractmethod
    async def update_cliente(self, idCliente: int, cliente: ClienteDomain) -> ClienteDomain:
        pass

    @abstractmethod
    async def delete_cliente(self, idCliente: int) -> None:
        pass

    @abstractmethod
    async def get_all_clientes(self) -> list[ClienteDomain]:
        pass

    @abstractmethod
    async def get_cliente_by_email(self, email:str,cliente: ClienteDomain) -> ClienteDomain:
        pass
