from fastapi import FastAPI

from apps.app01 import app01
from apps.app02 import app02

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["App01 Endpoints Request Parameter"])
app.include_router(app02, prefix="/app02", tags=["App02 Endpoints Query Parameter"])
