from fastapi import FastAPI, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api

app = FastAPI()

# Include the student API router
app.include_router(student_api, prefix="/student", tags=["Student API"])

# run the ORM models in database
register_tortoise(
    app = app,
    config = TORTOISE_ORM,
)


