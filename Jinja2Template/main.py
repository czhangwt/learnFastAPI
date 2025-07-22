from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index")
def read_index(request: Request):
    name = "root"
    age = 30
    books = ["Book One", "Book Two", "Book Three"]
    education = {"school": "ABC University", "degree": "Bachelor of Science"}
    pi = 3.14159

    return templates.TemplateResponse(
        "index.html", # template file name
        {
            "request": request, # request object is required by Jinja2
            "user": name,
            "age": age,
            "books": books,
            "education": education,
            "pi": pi,
        }, # context to pass to the template
    )