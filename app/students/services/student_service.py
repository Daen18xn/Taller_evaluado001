from fastapi import HTTPException, status
from repositories.student_repository import StudentRepository
from schemas.student_schema import CreateStudentDto, Student, UpdateStudentDto

class StudentService:
    def __init__(self, repository: StudentRepository) -> None:
        self.repository = repository

    def find_all(self) -> list[Student]:
        students = self.repository.find_all()
        return sorted(students, key=lambda s: s.createdAt, reverse=True)

    def find_by_id(self, student_id: str) -> Student:
        student = self.repository.find_by_id(student_id)
        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estudiante no encontrado",
            )
        return student

    def create(self, data: CreateStudentDto) -> Student:
        self.assert_email_available(data.email)
        return self.repository.save(data)

    def update(self, student_id: str, data: UpdateStudentDto) -> Student:
        existing = self.find_by_id(student_id)

        if data.email and data.email != existing.email:
            self.assert_email_available(data.email)

        return self.repository.update(existing, data)

    def delete(self, student_id: str) -> Student:
        existing = self.find_by_id(student_id)
        self.repository.delete(student_id)
        return existing

    def assert_email_available(self, email: str) -> None:
        exists = any(s.email == email for s in self.repository.find_all())
        if exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El correo electrónico ya está en uso",
            )