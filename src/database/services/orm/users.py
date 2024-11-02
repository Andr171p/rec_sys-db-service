from sqlalchemy import select

from typing import Sequence

from src.database.services.crud import CRUDService
from src.database.models.users import UserModel


class UsersORMService(CRUDService):
    async def build_table(self):
        await self.create_table()

    async def create_user(self, user: UserModel) -> UserModel:
        users = await self.create_item(user)
        return user

    async def create_users(self, users: Sequence[UserModel]) -> Sequence[UserModel]:
        users = await self.create_items(users)
        return users