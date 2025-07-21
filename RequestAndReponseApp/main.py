from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05  
from apps.app06 import app06  
from apps.app07 import app07

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static_files"))

app.include_router(app01, prefix="/app01", tags=["App01 Endpoints Request Parameter"])
app.include_router(app02, prefix="/app02", tags=["App02 Endpoints Query Parameter"])
app.include_router(app03, prefix="/app03", tags=["App03 Endpoints Request Content"])
app.include_router(app04, prefix="/app04", tags=["App04 Endpoints Form Data"])
app.include_router(app05, prefix="/app05", tags=["App05 Endpoints File Upload"])
app.include_router(app06, prefix="/app06", tags=["App06 Endpoints Request Object"])
app.include_router(app07, prefix="/app07", tags=["App07 Endpoints Response Model"])