from fastapi import APIRouter

app01 = APIRouter()

# route parameter example

# there is an excution order for the routes
# the first route that matches the request will be executed
# if you have a route with a path parameter that matches the request
# it will be executed first, even if there is a more specific route later
@app01.get("/user/1")
async def get_user():
    return {
        "user_role": "admin",
    }

@app01.get("/user/{id}")
async def get_user(id):
    print(f"Received request for user with id: {id}")
    return {
        "user_id": id
    }

@app01.get("/items/{item_id}")
def get_item(item_id: int):
    print(f"Received request for item with id: {item_id}")
    return {
        "item_id": item_id,
        "item_id_type": type(item_id).__name__
    }