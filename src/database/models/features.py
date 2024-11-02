from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.data_services.database.models.base import Base
from src.data_services.database.types import str_uniq


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = "features"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class FeaturesModel(AbstractModel):
    features: Mapped[str_uniq]
