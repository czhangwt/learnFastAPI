# Course Registration System Example

from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="Full Name of the student")
    password = fields.CharField(max_length=50, description="Password of the student")
    student_id = fields.IntField(max_length=20, unique=True, description="Student ID")

    # one-to-many relationship with Course
    # related_name allows reverse access from Course to Student
    clas = fields.ForeignKeyField('models.Clas', related_name='class_students', description="Class the student belongs to")

    # many-to-many relationship
    courses = fields.ManyToManyField(
        'models.Course',
        related_name='courses_students',
        description="Courses the student is enrolled in"
    )


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="Name of the course")
    teacher = fields.ForeignKeyField('models.Teacher', related_name='teacher_courses', description="Teacher who teaches the course")
    address = fields.CharField(max_length=200, description="Address of the course", default="Unknown")

class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="Name of the class")

class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="Full Name of the teacher")
    password = fields.CharField(max_length=50, description="Password of the teacher")
    teacher_id = fields.IntField(max_length=20, unique=True, description="Teacher ID")

    