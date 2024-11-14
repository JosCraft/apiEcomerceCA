from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.responses import Response, FileResponse
from src.core.abstractions.services.producto_service_abstract import IProductoService
from src.core.dependency_inyection.dependency_inyection import build_prodcuto_service
from src.presentation.dto.producto_dto import ProductoDTO
from src.presentation.mappers.map_dto_domain_producto import map_domain_dto_to_producto
from src.core.models.producto_domain import ProductoDomain
import os
from uuid import uuid4

producto_controller = APIRouter(prefix="/api/v1", tags=["producto"])

# Definir la carpeta donde se guardarán las imágenes
IMAGES_DIR = "src/resources/imagenes"

# Crear la carpeta de imágenes si no existe
os.makedirs(IMAGES_DIR, exist_ok=True)


@producto_controller.get("/productos", response_model=list[ProductoDomain])
async def list_productos(
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    productos = await producto_service.get_all_productos()
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

    # Devolver la imagen como archivo
    imagen_path = os.path.join(IMAGES_DIR, producto.imagen)
    return FileResponse(imagen_path)


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

    # Generar URL para la imagen si existe
    if producto.imagen:
        producto.imagen = f"/api/v1/producto/{producto.id}/imagen"

    return producto


# Guardar la imagen en la carpeta de recursos y devolver el nombre del archivo
async def save_image_to_disk(imagen: UploadFile) -> str:
    filename = f"{uuid4()}.{imagen.filename.split('.')[-1]}"
    file_path = os.path.join(IMAGES_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(await imagen.read())
    return filename


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
    # Guardar la imagen en disco
    imagen_filename = await save_image_to_disk(imagen)
    print(imagen_filename)
    # Crear el DTO para el producto
    producto_dto = ProductoDTO(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        descuento=descuento,
        imagen=imagen_filename,
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
        idCategoria: int = Form(...),
        imagen: UploadFile = File(...),
        producto_service: IProductoService = Depends(build_prodcuto_service)
):
    existing_producto = await producto_service.get_producto(id)
    if not existing_producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto with ID {id} not found"
        )

    # Guardar la nueva imagen en disco
    imagen_filename = await save_image_to_disk(imagen)

    # Crear el DTO para el producto
    producto_dto = ProductoDTO(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        descuento=descuento,
        imagen=imagen_filename,
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
    
    # Eliminar la imagen del disco si existe
    imagen_path = os.path.join(IMAGES_DIR, existing_producto.imagen)
    if os.path.exists(imagen_path):
        os.remove(imagen_path)
    
    await producto_service.delete_producto(id)
    return {"message": f"Producto with ID {id} successfully deleted"}
