from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "clas" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL /* Name of the class */
);
CREATE TABLE IF NOT EXISTS "student" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL /* Full Name of the student */,
    "password" VARCHAR(50) NOT NULL /* Password of the student */,
    "student_id" INT NOT NULL UNIQUE /* Student ID */,
    "clas_id" INT NOT NULL REFERENCES "clas" ("id") ON DELETE CASCADE /* Class the student belongs to */
);
CREATE TABLE IF NOT EXISTS "teacher" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL /* Full Name of the teacher */,
    "password" VARCHAR(50) NOT NULL /* Password of the teacher */,
    "teacher_id" INT NOT NULL UNIQUE /* Teacher ID */
);
CREATE TABLE IF NOT EXISTS "course" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL /* Name of the course */,
    "address" VARCHAR(200) NOT NULL DEFAULT 'Unknown' /* Address of the course */,
    "teacher_id" INT NOT NULL REFERENCES "teacher" ("id") ON DELETE CASCADE /* Teacher who teaches the course */
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "student_course" (
    "student_id" INT NOT NULL REFERENCES "student" ("id") ON DELETE CASCADE,
    "course_id" INT NOT NULL REFERENCES "course" ("id") ON DELETE CASCADE
) /* Courses the student is enrolled in */;
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_student_cou_student_0d222b" ON "student_course" ("student_id", "course_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
