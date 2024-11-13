from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import Response
from src.core.abstractions.services.categoria_service_abstract import ICategoriaService
from src.core.dependency_inyection.dependency_inyection import build_prodcuto_service
from src.presentation.dto.categoria_dto import CategoriaDTO
from src.presentation.mappers.map_dto_domain_categoria import map_domain_dto_to_categoria
from src.core.models.categoria_domain import CategoriaDomain
import base64

producto_controller = APIRouter(prefix="/api/v1", tags=["producto"])