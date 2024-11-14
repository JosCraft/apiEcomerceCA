from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import Response
from src.core.abstractions.services.producto_service_abstract import IProductoService
from src.core.dependency_inyection.dependency_inyection import build_prodcuto_service
from src.presentation.dto.producto_dto import ProductoDTO
from src.presentation.mappers.map_dto_domain_producto import map_domain_dto_to_producto
from src.core.models.producto_domain import ProductoDomain
import base64

producto_controller = APIRouter(prefix="/api/v1", tags=["producto"])


@producto_controller.get("/productos", response_model=list[ProductoDomain])
async def list_productos(
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    productos = await producto_service.get_all_productos()

    # Agregar el prefijo MIME a cada imagen
    for producto in productos:
        if producto.imagen:
            producto.imagen = f"data:image/jpeg;base64,{producto.imagen}"

    return productos


@producto_controller.get("/producto/{id}/imagen")
async def retrieve_producto_imagen(
        id: int,
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    producto = await producto_service.get_producto(id)
    if not producto or not producto.imagen:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Imagen for producto with ID {id} not found"
        )

    # Decodifica la imagen de base64 y responde como bytes
    imagen_bytes = base64.b64decode(producto.imagen)

    return Response(content=imagen_bytes, media_type="image/jpeg")

@producto_controller.get("/producto/{id}", response_model=ProductoDomain)
async def retrieve_producto(
        id: int,
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    producto = await producto_service.get_producto(id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto with ID {id} not found"
        )

    # Agregar el prefijo MIME para la imagen
    if producto.imagen:
        producto.imagen = f"data:image/jpeg;base64,{producto.imagen}"

    return producto


# Convertir la imagen a una cadena base64
async def convertir_imagen_a_base64(imagen: UploadFile) -> str:
    imagen_bytes = await imagen.read()  # Lee la imagen como bytes
    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')  # Convierte los bytes a base64
    return imagen_base64


@producto_controller.post("/producto", response_model=ProductoDomain, status_code=status.HTTP_201_CREATED)
async def create_producto(
        nombre: str = Form(...),
        descripcion: str = Form(...),
        precio: float = Form(...),
        descuento: float = Form(...),
        stock: int = Form(...),
        idcategoria: int = Form(...),
        imagen: UploadFile = File(...),
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    # Convertir la imagen a base64
    imagen_base64 = await convertir_imagen_a_base64(imagen)

    # Crear el DTO para el producto
    producto_dto = ProductoDTO(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        descuento=descuento,
        imagen=imagen_base64,
        stock=stock,
        idCategoria=idcategoria
    )

    # Mapear el DTO a ProductoDomain y crear el producto
    producto = map_domain_dto_to_producto(producto_dto)
    return await producto_service.create_producto(producto)


@producto_controller.put("/producto/{id}", response_model=ProductoDomain)
async def update_producto(
        id: int,
        nombre: str = Form(...),
        descripcion: str = Form(...),
        precio: float = Form(...),
        descuento: float = Form(...),
        stock: int = Form(...),
        idCategoria:int =Form(...),
        imagen: UploadFile = File(...),
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    existing_producto = await producto_service.get_producto(id)
    if not existing_producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto with ID {id} not found"
        )

    # Convertir la imagen a base64
    imagen_base64 = await convertir_imagen_a_base64(imagen)

    # Crear el DTO para el producto
    producto_dto = ProductoDTO(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        descuento=descuento,
        imagen=imagen_base64,
        stock=stock,
        idCategoria=idCategoria
    )

    # Mapear el DTO a ProductoDomain y actualizar el producto
    producto = map_domain_dto_to_producto(producto_dto)
    return await producto_service.update_producto(id, producto)


@producto_controller.delete("/producto/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_producto(
        id: int,
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    existing_producto = await producto_service.get_producto(id)
    if not existing_producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto with ID {id} not found"
        )
    await producto_service.delete_producto(id)
    return {"message": f"Producto with ID {id} successfully deleted"}
