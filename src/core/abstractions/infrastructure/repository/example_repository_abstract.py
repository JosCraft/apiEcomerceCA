from abc import ABC, abstractmethod

from src.core.models.example_domain import ExampleDomain


class IExampleRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> ExampleDomain:
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
