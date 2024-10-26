from fastapi import APIRouter, HTTPException
from ...app.controllers.user_controller import UserController
from ...app.models.user_model import User

router = APIRouter()
controller = UserController()

@router.get("/users")
async def get_users():
    return await controller.get_all_users()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
async def create_user(user: User):
    user_id = await controller.create_user(user)
    return {"id": user_id}

@router.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    updated = await controller.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    deleted = await controller.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
