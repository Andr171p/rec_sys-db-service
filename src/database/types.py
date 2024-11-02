from sqlalchemy import func
from sqlalchemy.orm import mapped_column

from typing import Annotated
from datetime import datetime


created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]

int_null_true = Annotated[int, mapped_column(nullable=True)]
int_nullable = Annotated[int, mapped_column(nullable=False)]

str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]
str_nullable = Annotated[str, mapped_column(nullable=False)]
