from fastapi import APIRouter
import controllers

router = APIRouter()

@router.get('/')
async def get_root():
  return controllers.get_root()
