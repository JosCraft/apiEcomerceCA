from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.example_service_abstract import IExampleService
from src.core.dependency_inyection.dependency_inyection import build_example_service

example_controller = APIRouter(prefix="/api/v1", tags=["example"])


@example_controller.get("/exameple/getExample/asdasasdasf/")
async def get_example(
        example_service: IExampleService = Depends(build_example_service)
        id : int
        nombre: str
):
    try:
        recidibo = dto(id=id, nombre=nombre)

        example = example_service.create(mapper(recidibo))
        return example
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

