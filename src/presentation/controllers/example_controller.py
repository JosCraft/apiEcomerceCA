from fastapi import APIRouter, Depends, HTTPException, Response

from src.core.abstractions.services.example_service_abstract import IExampleService
from src.core.dependency_inyection.dependency_inyection import build_example_service

example_controller = APIRouter(prefix="/api/v1", tags=["example"])


@example_controller.get("/example")
async def get_example(
        example_service: IExampleService = Depends(build_example_service)
):
    try:
        example = example_service.get_example()
        return example
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))