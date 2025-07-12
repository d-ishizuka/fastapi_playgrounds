from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    is_active: bool = True

users = [
    User(username="太郎", is_active=True),
    User(username="二郎", is_active=False),
    User(username="花子", is_active=True)
]

def get_active_users():
    active_users = [user for user in users if user.is_active]
    return active_users

@app.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
    return active_users