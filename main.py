from fastapi import FastAPI,HTTPException
from models import User,Gender,Role
from typing import List
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("96a3391c-dd0e-43ba-b622-2931fcc2d938"),
        first_name="Jamila",
        last_name ="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("c092a66e-fc58-4cd8-8b27-fbb66a418d03"),
        first_name="Alex",
        last_name ="Ahmed",
        gender=Gender.male,
        roles=[Role.admin,Role.user]
    )
]

@app.get("/")
async def root():
    return{"Hello":"Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code = 404,
        detail =f"user with id: {user_id} does not exists"
    )
        