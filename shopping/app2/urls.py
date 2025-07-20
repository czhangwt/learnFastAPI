from fastapi import APIRouter

user= APIRouter()


@user.post("/create")
async def create_user(user: dict):
    return {"user_id": 1001, "user": user}

@user.post("/login")
async def login_user(user: dict):
    return {"message": "User logged in", "user": user}

