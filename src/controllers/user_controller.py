from src.models.user_model import User

async def create_user(name: str, email: str, department: str, cc: str, phone: str, active: bool):
    print("2",name, email, department, cc, phone, active)
    user = await User.create(name=name,email=email, department=department, cc=cc, phone=phone, active=active)
    #print(user)
    return user

async def get_user(user_id: int):
    user = await User.get(id=user_id)
    return user

async def get_users():
    users = await User.all()
    return users

async def delete_user(user_id: int):
    user = await User.get(id=user_id)
    await user.delete()
    return user