from fastapi import APIRouter, HTTPException
from src.controllers import user_controller
from pydantic import BaseModel
from typing import Optional
router = APIRouter()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    department: str
    cc: str
    active: bool

class UserCreateRequest(BaseModel):
    name: str
    email: str
    department: str
    cc: str
    phone: str
    active: Optional[str] = None


@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreateRequest):
    print("1" ,user.name, user.email, user.department, user.cc, user.phone, user.active)
    active = True if user.active == "on" else False
    user = await user_controller.create_user(user.name, user.email, user.department, user.cc, user.phone, active)
    return user

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    user = await user_controller.get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/users", response_model= list[UserResponse])
async def read_users():
    users = await user_controller.get_users()
    return users

@router.delete("/delete/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    user = await user_controller.delete_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")