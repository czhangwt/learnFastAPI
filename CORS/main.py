from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS means Cross-Origin Resource Sharing, which allows your API to be accessed from different origins.
# Cross-Origin Resource Sharing (CORS) is a security feature implemented by web browsers to prevent malicious websites from making requests to a different domain than the one that served the web page.
# It allows servers to specify who can access their resources and how they can be accessed.

@app.get("/user")
async def get_user():
    print("get_user called")
    return {"message": "User data retrieved successfully"}

# # sample CORS middleware 
# @app.middleware("http")
# async def MyCORSMiddleware(request: Request, call_next):
#     response = await call_next(request)
#     # Adding CORS headers to the response, allowing any origin to access the resource specified by *
#     # We can use CORS to limit access to specific resources or origins (like from partner websites)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  # Allows all origins, you can specify a list of allowed origins
    allow_credentials=True, # Allows cookies to be included in cross-origin requests
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)