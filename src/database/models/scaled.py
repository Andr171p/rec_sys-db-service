from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models.base import BaseModel


class AbstractModel(AsyncAttrs, BaseModel):
    __tablename__ = "scaled"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class ScaledUserModel(AbstractModel):
    full_name: Mapped[str]