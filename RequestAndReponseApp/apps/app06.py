from fastapi import APIRouter
from typing import Union, Optional
from fastapi import Request

app06 = APIRouter()


# Example of a request object

@app06.get("/item")
async def items(request: Request):
    print("URL Path:", request.url.path)
    print("IP Address:", request.client.host)
    print("Method:", request.method)
    print("Headers:", request.headers)
    print("User-Agent:", request.headers.get("user-agent"))
    print("Query Parameters:", request.query_params)
    print("cookies:", request.cookies)
    return {
        "url_path": request.url.path,
        "client_host": request.client.host,
        "method": request.method,
        "headers": request.headers,
        "user_agent": request.headers.get("user-agent"),
        "query_params": request.query_params,
    }