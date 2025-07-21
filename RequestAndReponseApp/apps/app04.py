from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List
from fastapi import Form

app04 = APIRouter()

# example of a request with Form data
@app04.post("/register")
async def register_user(username: str = Form(), password: str = Form()):
    """
    Register a new user with the provided details.
    """
    print(f"Username: {username}, Password: {password}")
    return {
        "username": username,
        "password": password,
    }
