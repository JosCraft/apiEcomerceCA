from src.core.abstractions.infrastructure.repository.example_repository_abstract import IExampleRepository
from src.core.abstractions.services.example_service_abstract import IExampleService
from src.core.models.example_domain import ExampleDomain

class ExampleService(IExampleService):
    def __init__(self, example_repository: IExampleRepository):
        self.example_repository = example_repository

    async def get_example(self, id: int) -> ExampleDomain:
        return await self.example_repository.get_example(id)
