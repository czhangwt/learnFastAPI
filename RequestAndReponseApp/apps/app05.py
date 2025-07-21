from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List
from fastapi import Form, File, UploadFile
import os

app05 = APIRouter()

# example of uploading a file
@app05.post("/file")
async def file(file: bytes = File()):
    print(f"File uploaded: {file}")
    # it works for small files, for larger files consider using StreamingResponse
    # or other methods to handle large files
    return {
        "file": len(file),
    }

# upload multiple files
@app05.post("/multiplefiles")
async def multiple_files(files: List[bytes] = File()):
    return {
        "number_of_files": len(files),
    }

# example of uploading and saving a file with UploadFile
@app05.post("/uploadfile")
async def upload_file(upload_file: UploadFile = File()):
    path = os.path.join("files", upload_file.filename)  # path of the file to save
    print(f"File uploaded: {upload_file.filename}, Content Type: {upload_file.content_type}")

    # save the file to the path
    with open(path, "wb") as f:
        for line in upload_file.file:
            f.write(line)

    return {
        "filename": upload_file.filename,
        "content_type": upload_file.content_type,
    }

# example of uploading and saving multiple files with UploadFile
@app05.post("/uploadmultiplefiles")
async def upload_multiple_files(upload_files: List[UploadFile]):
    for upload_file in upload_files:
        path = os.path.join("files", upload_file.filename)  # path of the file to save
        print(f"File uploaded: {upload_file.filename}, Content Type: {upload_file.content_type}")

        # save the file to the path
        with open(path, "wb") as f:
            for line in upload_file.file:
                f.write(line)

    return {
        "filenames": [upload_file.filename for upload_file in upload_files],
        "content_types": [upload_file.content_type for upload_file in upload_files],
    }