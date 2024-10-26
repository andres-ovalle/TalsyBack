from ...app.services.user_service import UserService
from ...app.models.user_model import User

class UserController:
    def __init__(self):
        self.service = UserService()

    async def get_all_users(self):
        return await self.service.get_all_users()

    async def get_user(self, user_id: str):
        return await self.service.get_user_by_id(user_id)

    async def create_user(self, user: User):
        return await self.service.create_user(user)

    async def update_user(self, user_id: str, user: User):
        return await self.service.update_user(user_id, user)

    async def delete_user(self, user_id: str):
        return await self.service.delete_user(user_id)
