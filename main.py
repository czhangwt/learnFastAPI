# to run the application: fastapi dev main.py
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def home():
#     return {"user_id": 1001}

# @app.get("/shop")
# async def shop():
#     return {"item_id": 2001}


'''
    practice router decorators
    - tags: used to group endpoints in the documentation
    - summary: a brief description of the endpoint
    - description: a detailed description of the endpoint
    - response_description: description of the response returned by the endpoint
    - deprecated: whether the endpoint is deprecated
'''
# @app.post("/items", tags=["API for adding items"],
#           summary="Create an item",
#           description="This endpoint allows you to create a new item in the inventory.",
#           response_description="The ID of the created item",
#           deprecated=False,
#           )
# async def create_item(item: dict):
#     return {"item_id": 3001, "item": item}


'''
    include_router example
    - used to modularize the application by separating routes into different files
    - allows for better organization and maintainability of the codebase
'''
from shopping.app1.urls import shop
from shopping.app2.urls import user

app.include_router(shop, prefix="/shop", tags=["Shop Endpoints"])
app.include_router(user, prefix="/user", tags=["User Endpoints"])
 