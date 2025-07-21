from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List


app07 = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    # remove password from the response model to return only safe data
    
# response_model is used to specify the response model for the endpoint
@app07.post("/user_create", response_model=UserOut)
def create_user(user: UserIn):
    return user

# response_model_exclude_unset=True is used to exclude unset fields from the response
class Item(BaseModel):
    item_id: int
    name: str
    description: Optional[str] = None

items = {
    1: {"item_id": 1, "name": "Item One"},
    2: {"item_id": 2, "name": "Item Two", "description": "This is item two"},
}
@app07.get("/items_exclude_unset/{item_id}", response_model=Item, response_model_exclude_unset=True)
def get_item(item_id: int):
    return items[item_id]

@app07.get("/items_include_exclude{item_id}", response_model=Item, response_model_include={"name"}, response_model_exclude={"description"})
def get_items(item_id: int):
    return items[item_id]

# other response_model options include
# response_model_exclude_defaults
# response_model_exclude_none
# response_model_include
# response_model_exclude...
