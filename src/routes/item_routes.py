from fastapi import APIRouter
from src.controllers import item_controller

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return item_controller.get_item(item_id, q)