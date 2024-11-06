from fastapi import Depends

from src.core.services.example_service import ExampleService

from src.infrastructure.repository.dependency_inyection.dependency_inyection import get_db_connection

from src.infrastructure.repository.implementations.example_repository import ExampleRepository


def build_example_service(
        db_connection=Depends(get_db_connection)
):
    return ExampleService(ExampleRepository(db_connection))

