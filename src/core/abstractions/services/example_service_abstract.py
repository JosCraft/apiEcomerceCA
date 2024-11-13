from abc import ABC, abstractmethod

from src.core.models.example_domain import ExampleDomain


class IExampleService(ABC):
    @abstractmethod
    async def get_example(self) -> ExampleDomain:
        pass

    @abstractmethod
    async def create_example(self, example: ExampleDomain) -> ExampleDomain:
        pass

    @abstractmethod
    async def update_example(self, example: ExampleDomain) -> ExampleDomain:
        pass

    @abstractmethod
    async def delete_example(self, example_id: int) -> None:
        pass

    @abstractmethod
    async def get_all_examples(self) -> list[ExampleDomain]:
        pass
