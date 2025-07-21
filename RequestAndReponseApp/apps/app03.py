from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List

app03 = APIRouter()

# define an Address model for nested data in User model
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int 
    name: str = Field(pattern=r"^[a-zA-Z\s]+$")  # name must be a string with only letters and spaces
    nickname: Optional[str] = None  # nickname is optional and can be a string or None
    age: int = Field(default=0, ge=0, le=120)  # ge=0 means age must be greater than or equal to 0, le=120 means age must be less than or equal to 120
    birth: Union[date, None] = None  # birth can be a date or None
    friends: List[int] = []  # friends is a list of integers, default is an empty list
    description: Optional[str] = None  # description is optional and can be a string or None
    address: Optional[Address] = None  # embedded model for address, can be None

    @field_validator("nickname") # custom validation for nickname field
    def validate_nickname(cls, value):
        # nickname must contain only letters
        # assert keyword is used to raise an error if the condition is not met
        assert value.isalpha() or value is None, "Nickname must contain only letters"
        return value
        
class Date(BaseModel):
    data: List[User]

# example about request content

@app03.post("/user")
async def user(user_data: User): 
    print(user_data, "Type:", type(user_data))
    return {
        # model_dump is used to convert the Pydantic model to a dictionary
        # exclude_unset=True means only include fields that were set in the request
        "user_data": user_data.model_dump(exclude_unset=True),
    }

# embedded model example: data is a list of User models, and each User can have an Address model
@app03.post("/data")
async def data(data: Date): 
    return data