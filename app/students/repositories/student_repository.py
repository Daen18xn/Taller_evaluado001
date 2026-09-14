from datetime import datetime
from uuid import uuid4
from schemas.student_schema import CreateStudentDto, Student, UpdateStudentDto

class StudentRepository:
    def __init__(self) -> None:
        self._store: dict[str, Student] = {}

    def find_all(self) -> list[Student]:
        return list(self._store.values())

    def find_by_id(self, student_id: str) -> Student | None:
        return self._store.get(student_id)

    def save(self, data: CreateStudentDto) -> Student:
        now = datetime.now()
        student = Student(
            id=str(uuid4()),
            name=data.name,
            email=data.email,
            age=data.age,
            createdAt=now,
            updatedAt=now,
        )
        self._store[student.id] = student
        return student

    def update(self, existing: Student, data: UpdateStudentDto) -> Student:
        updated = existing.model_copy(
            update={
                **data.model_dump(exclude_none=True),
                "updatedAt": datetime.now(),
            }
        )
        self._store[existing.id] = updated
        return updated

    def delete(self, student_id: str) -> None:
        if student_id in self._store:
            del self._store[student_id]