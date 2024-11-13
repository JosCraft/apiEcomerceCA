from abc import ABC, abstractmethod

from src.core.models.example_domain import ExampleDomain


class IPedidoRepository(ABC):
    @abstractmethod
    async def get_all_by_id(self, id: int) -> ExampleDomain:
        pass

    @abstractmethod
    async def create(self, example: ExampleDomain) -> ExampleDomain:
        pass

    @abstractmethod
    async def update(self, example: ExampleDomain) -> ExampleDomain:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass
