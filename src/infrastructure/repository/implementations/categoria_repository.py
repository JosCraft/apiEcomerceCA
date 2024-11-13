from src.core.abstractions.infrastructure.repository.categoria_repository_abstract import ICategoriaRepository
from src.core.models.categoria_domain import CategoriaDomain

class CategoriaRepository(ICategoriaRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get(self, id: int) -> CategoriaDomain:
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM categoria WHERE idCategoria=%s", (id,))
                result = cursor.fetchone()
                if result:
                    return CategoriaDomain(
                        idCategoria=result['idCategoria'],
                        nombreCategoria=result['nombreCategoria'],
                    )
        except Exception as error:
            print(f"Error en 'get': {error}")
        return None

    async def create(self, categoria: CategoriaDomain) -> int:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO categoria (nombreCategoria)
                    VALUES (%s, %s)
                    """,
                    (
                        categoria.nombreCategoria,
                    )
                )
                self.connection.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                last_id = cursor.fetchone()[0]
                return last_id
        except Exception as err:
            print(f"Error en 'create': {err}")
            return None

    async def update(self, idCategoria: int, categoria: CategoriaDomain):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE categoria 
                    SET nombreCategoria=%s
                    WHERE idCategoria=%s
                    """,
                    (
                        categoria.nombreCategoria,
                        idCategoria
                    )
                )
                self.connection.commit()
                return True
        except Exception as err:
            print(f"Error en 'update': {err}")
            return False

    async def delete(self, id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM categoria WHERE idCategoria=%s", (id,))
                self.connection.commit()
                return True
        except Exception as err:
            print(f"Error en 'delete': {err}")
            return False

    async def get_all(self) -> list[CategoriaDomain]:
        lista_categoria = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM categoria")
                result = cursor.fetchall()
                for row in result:
                    categoria = CategoriaDomain(
                        idCategoria=row['idCategoria'],
                        nombreCategoria=row['nombreCategoria'],
                    )
                    lista_categoria.append(categoria)
            return lista_categoria
        except Exception as err:
            print(f"Error en 'get_all': {err}")
            return []
