import models

todo = []

def get_todo():
  return {"status": 200, "data": todo} 

# https://fastapi.tiangolo.com/tutorial/body/#declare-it-as-a-parameter
def post_todo(item: models.Todo):
  todo.append(item)
  return {"status": 200, "data": todo}

# https://fastapi.tiangolo.com/tutorial/body/#request-body-path-parameters
def put_todo(item_id: int, item: models.Todo):
  todo[item_id] = item
  return {"status": 200, "data": todo}

def delete_todo(item_id: int):
  todo.pop(item_id)
  return {"status": 200, "data": todo}