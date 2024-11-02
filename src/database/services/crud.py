from sqlalchemy import select, Row, RowMapping

from typing import Sequence, Any

from src.database.services.db import DatabaseSessionService
from src.database.models.base import Base


class CRUDService(DatabaseSessionService):
    def __init__(self, model: Base) -> None:
        super().__init__()
        self._model = model
        self.init()

    async def create_table(self) -> None:
        async with self.connect() as connection:
            await connection.run_sync(self._model.metadata.drop_all)
            await connection.run_sync(self._model.metadata.create_all)

    async def create_item(self, item: Base) -> Base | None:
        async with self.session() as session:
            session.add(item)
            await session.commit()
            await session.refresh(item)
        return item

    async def create_items(self, items: Sequence[Base]) -> Sequence[Base] | None:
        async with self.session() as session:
            session.add_all(items)
            await session.commit()
            for item in items:
                await session.refresh(item)
        return items

    async def get_items(self) -> Sequence[Row[Any] | RowMapping | Any]:
        async with self.session() as session:
            items = await session.execute(
                select(self._model)
            )
            return items.scalars().all()
