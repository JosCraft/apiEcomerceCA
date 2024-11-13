from src.core.abstractions.infrastructure.repository.producto_repository_abstract import IProductoRepository
from src.core.models.producto_domain import ProductoDomain

class ProductoRepository(IProductoRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get(self, id: int) -> ProductoDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM producto WHERE idProducto=%s", (id,))
                result = cursor.fetchone()
                if result:
                    return ProductoDomain(
                        idProducto=result['idProducto'],
                        nombre=result['nombre'],
                        descripcion=result['descripcion'],
                        precio=result['precio'],
                        descuento=result['descuento'],
                        imagen=result['imagen'],
                        stock=result['stock'],
                        idCategoria=result['idCategoria']
                    )
        except Exception as error:
            print(f"Error: {error}")
        return None

    async def create(self, producto: ProductoDomain) -> ProductoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO producto (nombre, descripcion, precio, descuento, imagen, stock,idCategoria)
                    VALUES (%s, %s, %s, %s, %s, %s,%s)
                    """,
                    (
                        producto.nombre,
                        producto.descripcion,
                        producto.precio,
                        producto.descuento,
                        producto.imagen,
                        producto.stock,
                        producto.idCategoria
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
                # Return the newly created ProductoDomain with the ID
                return await self.get(last_id)  # Return the full ProductoDomain object
        except Exception as error:
            print(f"Error: {error}")
            return None

    async def update(self, idProducto: int, producto: ProductoDomain) -> ProductoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE producto
                    SET nombre = %s, descripcion = %s, precio = %s, descuento = %s, imagen = %s, stock = %s
                    WHERE idProducto = %s
                    """,
                    (
                        producto.nombre,
                        producto.descripcion,
                        producto.precio,
                        producto.descuento,
                        producto.imagen,
                        producto.stock,
                        idProducto  # Correct parameter name
                    )
                )
                self.connection.commit()
                # Check if update was successful and return the updated product
                if cursor.rowcount > 0:
                    return await self.get(idProducto)  # Return the updated ProductoDomain
                return None
        except Exception as error:
            print(f"Error: {error}")
            return None

    async def delete(self, id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM producto WHERE idProducto = %s", (id,))
                self.connection.commit()
                return cursor.rowcount > 0
        except Exception as err:
            print(f"Error: {err}")
            return False

    async def get_all(self) -> list[ProductoDomain]:
        try:
            lista_producto = []
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM producto")
                result = cursor.fetchall()
                for row in result:
                    lista_producto.append(
                        ProductoDomain(
                            idProducto=row['idProducto'],
                            nombre=row['nombre'],
                            descripcion=row['descripcion'],
                            precio=row['precio'],
                            descuento=row['descuento'],
                            imagen=row['imagen'],
                            stock=row['stock'],
                            idCategoria=row['idCategoria']
                        )
                    )
            return lista_producto
        except Exception as error:
            print(f"Error: {error}")
            return []
