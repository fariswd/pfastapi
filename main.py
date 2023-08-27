from fastapi import FastAPI
from routes import root, todo

app = FastAPI()
app.include_router(root.router)
app.include_router(todo.router, prefix="/todo")