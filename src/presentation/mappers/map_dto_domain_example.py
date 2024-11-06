from src.core.models.example_domain import ExampleDomain

from src.presentation.dto.example_dto import ExampleDTO


def map_example_dto_to_domain(example_dto: ExampleDTO) -> ExampleDomain:
    return ExampleDomain(
        name=example_dto.name,
        age=example_dto.age,
        email=example_dto.email
    )
