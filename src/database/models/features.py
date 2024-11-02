from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models.base import BaseModel
from src.database.types import str_uniq


class AbstractModel(AsyncAttrs, BaseModel):
    __tablename__ = "features"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class FeaturesModel(AbstractModel):
    features: Mapped[str_uniq]
