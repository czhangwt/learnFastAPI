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
from models import *

from pydantic import BaseModel, field_validator
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
    
    # # 6. one-to-many relationship query: student finds their class
    # # get one student and their class
    # stu = await Student.get(name="Alice")
    # print(stu.name)
    # print(await stu.clas.values("name"))
    # # # get all students and their classes
    # students = await Student.all().values("name", "clas__name")

    # # 7. many-to-many relationship query: student finds their courses
    # # get one student and their courses
    # stu = await Student.get(name="Cathy")
    # print(await stu.courses.all().values("name", "teacher__name")) # get all courses and their teachers for the student
    
    # # get all students and their courses
    students = await Student.all().values("name", "clas__name", "courses__name", "courses__teacher__name")
    return students



class StudentIn(BaseModel):
    name: str
    password: str
    student_id: int
    clas_id: int  # Foreign key to Clas model
    courses_ids: List[int] = []  # List of course IDs for many-to-many relationship

    @field_validator('name')
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'Name must contain only alphabetic characters'
        return value
    
    @field_validator('student_id')
    def student_id_validate(cls, value):
        assert value > 2000 and value < 10000, 'Student ID must be 2000-9999'
        return value
    

@student_api.post("/")
async def addStudent(student_in: StudentIn):
    # Insert a new student into the database
    # Method 1: .save()
    # student = Student(name = student_in.name,
    #         password = student_in.password,
    #         student_id = student_in.student_id,
    #         clas_id = student_in.clas_id)
    # await student.save()
    # Method 2: .create()
    student = await Student.create(
        name=student_in.name,
        password=student_in.password,
        student_id=student_in.student_id,
        clas_id=student_in.clas_id
    )

    # many-to-many relationship adding (insert)
    choose_courses = await Course.filter(id__in=student_in.courses_ids) 
    await student.courses.add(*choose_courses) # * means unpacking the list of courses

    return {
        "message": "Add a student",
        "student": student

    }


# get one student
@student_api.get("/{student_id}")
async def getStudent(student_id: int):
    # Retrieve a specific student by ID
    student = await Student.get(student_id=student_id)
    return {
        "message": f"Details of student {student_id}",
        "student": student
    }

# update a student
# Note: In a real application, you would typically use a Pydantic model StudentIn for the request body
@student_api.put("/{student_id}")
async def updateStudent(student_id: int, student_in: StudentIn):
    data = student_in.model_dump()
    print(data)
    courses = data.pop("courses_ids")
    # update() can change one-to-one and one-to-many relationships
    # but cannot change many-to-many relationships, which need to be handled separately
    await Student.filter(student_id=student_id).update(**data)

    edit_stu = await Student.get(student_id=student_id)
    choose_courses = await Course.filter(id__in=courses)
    await edit_stu.courses.clear()  # clear existing courses
    await edit_stu.courses.add(*choose_courses)


    return edit_stu


from fastapi import HTTPException
# delete a student
@student_api.delete("/{student_id}")
async def deleteStudent(student_id: int):
    deleteCount = await Student.filter(student_id=student_id).delete()
    if deleteCount == 0:
        raise HTTPException(status_code=404, detail=f"Student ID {student_id} not found")
    return {
        "message": f"Delete student {student_id}"
    }



