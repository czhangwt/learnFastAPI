import time
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import time
app = FastAPI()


# priority of middleware is determined by the order of definition
# the earlier a middleware is called, the lower its position in the code

# implement second middleware m2
@app.middleware("http") 
async def m2(request: Request, call_next):
    # request code
    print("m2 request")
    response = await call_next(request)
    response.headers["author"] = "M2 Middleware"  # Adding a custom header to the response
    
    # response code
    print("m2 response")

    return response


# implement first middleware m1
@app.middleware("http") 
async def m1(request: Request, call_next):
    # request code
    print("m1 request")
    # # blocking unauthorized IPs
    # if request.client.host in ["127.0.0.1"]:
    #     response = await call_next(request)
    # else:
    #     response = JSONResponse(content={"detail": "Unauthorized IP " + request.client.host}, status_code=401)

    # blocking specific endpoint in this middleware request
    if request.url.path == "/user":
        return JSONResponse(content={"message": "User endpoint is not available"}, status_code=403)

    start_time = time.time()
        # 
    response = await call_next(request)
    end_time = time.time()
    response.headers["X-Processing-Time"] = str(end_time - start_time)  #
    print("m1 response")

    return response



@app.get("/user")
def get_user():
    print("get_user called")
    return {"message": "User data retrieved successfully"}

@app.get("/item/{item_id}")
def get_item(item_id: int):
    time.sleep(2)
    print("get_item called with item_id:", item_id)
    return {"message": f"Item {item_id} data retrieved successfully"}
