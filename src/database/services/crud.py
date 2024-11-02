from sqlalchemy import select

from src.database.services.db import DatabaseSessionService
from src.database.models.base import Base


class ORMService(DatabaseSessionService):
    def __init__(self, model: Base) -> None:
        super().__init__()
        self._model = model
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(self._model.metadata.drop_all)
            await connection.run_sync(self._model.metadata.create_all)

    async def create(self, item: Base) -> Base:
        async with self.session() as session:
            ...