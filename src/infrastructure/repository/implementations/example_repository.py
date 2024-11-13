from src.core.abstractions.infrastructure.repository.example_repository_abstract import IExampleRepository
from src.core.models.example_domain import ExampleDomain


class ExampleRepository(IExampleRepository):

    def __init__(self, connection):
        self.connection = connection

    async def get_all_pedidos(self):
        colors = []
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM tabla1")
                result = cursor.fetchall()

                for row in result:
                    color = ExampleDomain(
                        id=row["id_cl"],
                        nombre=row["nombre_cl"],
                        codigoHex=row["codigo_hx"]
                    )
                    colors.append(color)

                return colors
        except Exception as e:
            print(e)
        return colors


