from fastapi import APIRouter

shop = APIRouter()

@shop.get("/food")
async def shop_food():
    return {"item": "food"}

@shop.get("/clothing")
async def shop_clothing():
    return {"item": "clothing"}