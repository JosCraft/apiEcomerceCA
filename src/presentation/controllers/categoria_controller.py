from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import Response
from src.core.abstractions.services.categoria_service_abstract import ICategoriaService
from src.core.dependency_inyection.dependency_inyection import build_categoria_service
from src.presentation.dto.categoria_dto import CategoriaDTO
from src.presentation.mappers.map_dto_domain_categoria import map_domain_dto_to_categoria
from src.core.models.categoria_domain import CategoriaDomain
import base64

categoria_controller = APIRouter(prefix="/api/v1", tags=["categoria"])


@categoria_controller.get("/categoria", response_model=list[CategoriaDomain])
async def list_categoria(
    categoria_service: ICategoriaService = Depends(build_categoria_service)
):
    return await categoria_service.get_all_categoria()


@categoria_controller.get("/categoria/{id}", response_model=CategoriaDomain)
async def retrieve_categoria(
    id: int,
    categoria_service: ICategoriaService = Depends(build_categoria_service)
):
    categoria = await categoria_service.get_categoria(id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria with ID {id} not found"
        )
    return categoria


@categoria_controller.post("/categoria", response_model=CategoriaDomain, status_code=status.HTTP_201_CREATED)
async def create_categoria(
    categoria_dto: CategoriaDTO,
    categoria_service: ICategoriaService = Depends(build_categoria_service)
):
    categoria = map_domain_dto_to_categoria(categoria_dto)
    return await categoria_service.create_categoria(categoria)


@categoria_controller.put("/categoria/{id}", response_model=CategoriaDomain)
async def update_categoria(
    id: int,
    categoria_dto: CategoriaDTO,
    categoria_service: ICategoriaService = Depends(build_categoria_service)
):
    existing_categoria = await categoria_service.get_categoria(id)
    if not existing_categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria with ID {id} not found"
        )
    categoria = map_domain_dto_to_categoria(categoria_dto)
    return await categoria_service.update_categoria(id, categoria)


@categoria_controller.delete("/categoria/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria(
    id: int,
    categoria_service: ICategoriaService = Depends(build_categoria_service)
):
    existing_categoria = await categoria_service.get_categoria(id)
    if not existing_categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria with ID {id} not found"
        )
    await categoria_service.delete_categoria(id)
    return {"message": f"Categoria with ID {id} successfully deleted"}
