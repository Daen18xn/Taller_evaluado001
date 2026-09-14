from fastapi import APIRouter, status
from schemas.student_schema import CreateStudentDto, Student, UpdateStudentDto
from services.student_service import StudentService
from repositories.student_repository import StudentRepository

# Instanciamos la arquitectura en capas (Repo -> Service -> Router)
repository = StudentRepository()
service = StudentService(repository)

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=list[Student], status_code=status.HTTP_200_OK)
def get_students():
    return service.find_all()


@router.get("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student_by_id(student_id: str):
    return service.find_by_id(student_id)


@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(data: CreateStudentDto):
    return service.create(data)


@router.patch("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: str, data: UpdateStudentDto):
    return service.update(student_id, data)


@router.delete("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def delete_student(student_id: str):
    return service.delete(student_id)