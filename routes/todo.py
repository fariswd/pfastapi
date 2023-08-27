from fastapi import APIRouter, Body
import controllers
import models

router = APIRouter()

@router.get('/')
async def route_get_todo():
  return controllers.get_todo()

@router.post('/')
async def route_post_todo(item: models.Todo):
  return controllers.post_todo(item)

@router.put('/{item_id}')
async def route_put_todo(item_id: int, item: models.Todo):
  return controllers.put_todo(item_id, item)

@router.delete('/{item_id}')
async def route_put_todo(item_id: int):
  return controllers.delete_todo(item_id)