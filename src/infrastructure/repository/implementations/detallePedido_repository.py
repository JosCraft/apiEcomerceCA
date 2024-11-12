from src.core.abstractions.infrastructure.repository.detallePedido_repository_abstract import IDetallePedidoRepository
from src.core.models.detallePedido_domain import DetallePedidoDomain


class DetallePedidoRepository(IDetallePedidoRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get(self, id: int) -> DetallePedidoDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM detallepedido WHERE idDetalle=%s", (id,))
                result = cursor.fetchone()
                if result:
                    return DetallePedidoDomain(
                        idDetalle=result['idDetalle'],
                        idPedido=result['idPedido'],
                        idProducto=result['idProducto'],
                        cantidad=result['cantidad'],
                        subtotal=result['subtotal'],
                    )
        except Exception as error:
            print(f"Error al obtener detalle de pedido: {error}")
        return None

    async def create(self, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO detallepedido (idPedido, idProducto, cantidad, subtotal)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        detalle_pedido.idPedido,
                        detalle_pedido.idProducto,
                        detalle_pedido.cantidad,
                        detalle_pedido.subtotal
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]

                # Recupera el detalle de pedido creado
                return await self.get(last_id)
        except Exception as error:
            print(f"Error al crear detalle de pedido: {error}")
            return None

    async def update(self, id_detalle: int, detalle_pedido: DetallePedidoDomain) -> DetallePedidoDomain:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE detallepedido
                    SET idPedido = %s, idProducto = %s, cantidad = %s, subtotal = %s
                    WHERE idDetalle = %s
                    """,
                    (
                        detalle_pedido.idPedido,
                        detalle_pedido.idProducto,
                        detalle_pedido.cantidad,
                        detalle_pedido.subtotal,
                        id_detalle
                    )
                )
                self.connection.commit()

                # Verifica si se actualizó el registro
                if cursor.rowcount > 0:
                    return await self.get(id_detalle)
                return None
        except Exception as error:
            print(f"Error al actualizar detalle de pedido: {error}")
            return None

    async def delete(self, id: int) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM detallepedido WHERE idDetalle = %s", (id,))
                self.connection.commit()
                if cursor.rowcount > 0:
                    return True
            return False
        except Exception as error:
            print(f"Error al eliminar detalle de pedido: {error}")
            return False

    async def get_all(self) -> list[DetallePedidoDomain]:
        lista_detalle_pedido = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM detallepedido")
                result = cursor.fetchall()
                for row in result:
                    detalle_pedido = DetallePedidoDomain(
                        idDetalle=row['idDetalle'],
                        idPedido=row['idPedido'],
                        idProducto=row['idProducto'],
                        cantidad=row['cantidad'],
                        subtotal=row['subtotal']
                    )
                    lista_detalle_pedido.append(detalle_pedido)
            return lista_detalle_pedido
        except Exception as error:
            print(f"Error al obtener todos los detalles de pedido: {error}")
            return []