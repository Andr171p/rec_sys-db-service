from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.data_services.database.models.base import Base
from src.data_services.database.types import (
    int_null_true,
    int_nullable,
    str_nullable
)


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class UserInfoModel:
    full_name: Mapped[str_nullable]
    gender: Mapped[int]
    age: Mapped[int]
    sport: Mapped[int_nullable]
    is_foreign: Mapped[int_nullable]


class UserEducationModel:
    education_bac_degree: Mapped[int_null_true]
    education_school: Mapped[int_null_true]
    education_collage: Mapped[int_null_true]


class UserStudyFormModel:
    study_form_full: Mapped[int_null_true]
    study_form_ext: Mapped[int_null_true]
    study_form_full_ext: Mapped[int_null_true]


class UserPointsModel:
    gpa: Mapped[float]
    total_points: Mapped[int]
    bonus_total_points: Mapped[int]
    is_enrolled: Mapped[int_null_true]


class UserExamModel:
    drawing_exam: Mapped[int_null_true]
    math_exam: Mapped[int_null_true]
    russian_exam: Mapped[int_null_true]
    social_exam: Mapped[int_null_true]
    physic_exam: Mapped[int_null_true]
    history_exam: Mapped[int_null_true]
    composition_architecture_exam: Mapped[int_null_true]
    composition_design_exam: Mapped[int_null_true]
    informatics_exam: Mapped[int_null_true]
    chemistry_exam: Mapped[int_null_true]
    composition_exam: Mapped[int_null_true]


class UserModel(
    AbstractModel, UserInfoModel, UserEducationModel, UserPointsModel, UserStudyFormModel, UserExamModel
):
    pass
