"""
    # Restful API for Student Management
    This API allows for CRUD operations on student records.
    - get("/student"): Retrieve all students
    - post("/student"): Add a new student
    - get("/student/{student_id}"): Retrieve a specific student
    - put("/student/{student_id}"): Update a specific student
    - delete("/student/{student_id}"): Delete a specific student

"""

from fastapi import APIRouter
from models import Student

from pydantic import BaseModel
from typing import List, Union
from fastapi.templating import Jinja2Templates
from fastapi import Request

student_api = APIRouter()


# ORM responses can also be rendered in HTML templates
# need to put this router before / to avoid conflict with the root path
@student_api.get("/index.html")
async def index(request: Request):
    templates = Jinja2Templates(directory="templates")
    students = await Student.all()
    for student in students:
        print(student.student_id, student.name, student.clas_id)

    return templates.TemplateResponse(
        "index.html", {
            "request": request, 
            "students": students
         }
    )



# must add async and await for Tortoise ORM to work properly
# async means that the function can be paused and resumed later, allowing other tasks to run in the meantime
@student_api.get("/")
async def getAllStudents():
    # # 1. Retrieve all students, return a list of Student objects Queryset
    # students = await Student.all() ## [Student1, Student2, ...]
    # for student in students:
    #     print(student.name, student.student_id)

    # return {
    #     "message": "List of all students"
    # }


    # # 2. Query specific student objects by filter(), return a list of Student objects Queryset
    # students = await Student.filter(name='Stu 1')

    # # 3. Query specific student objects by get(), return ONE single Student object
    # stu = await Student.get(student_id=2001)
    # print(stu.name, stu.student_id)

    # # 4. Query student objects with ambiguous fields
    students = await Student.filter(student_id__gte=2000)  # student id greater than or equal to 2000
    # # __gte means "greater than or equal to"
    # # __lte means "less than or equal to"
    # # __contains means "contains" (for string fields)
    # # __in means "in" (for list fields), e.g., student_id__in=[2001, 2002]
    # # __range means "range" (for date fields), e.g., created_at__range=["2023-01-01", "2023-12-31"]
    
    # # 5. Query values of specific fields, return a list of Dictionaries
    # stu_ids = await Student.all().values('student_id', 'name')
    # print(stu_ids)  # [{'student_id': 2001, 'name': 'Stu 1'}, {'student_id': 2002, 'name': 'Stu 2'}]
    return students


@student_api.post("/")
async def addStudent():
    return {
        "message": "Add a student"
    }

@student_api.get("/{student_id}")
async def getStudent(student_id: int):
    return {
        "message": f"Details of student {student_id}"
    }

@student_api.put("/{student_id}")
async def updateStudent(student_id: int):
    return {
        "message": f"Update student {student_id}"
    }

@student_api.delete("/{student_id}")
async def deleteStudent(student_id: int):
    return {
        "message": f"Delete student {student_id}"
    }



