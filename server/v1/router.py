from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from databases import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_student", response_model=schemas.Students)
def create_student(student: schemas.StudentsCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_roll_num(db, roll_num=student.roll_num)
    if db_student:
        raise HTTPException(status_code=400, detail=f"Student with roll number {student.roll_num} already exists")
    return crud.create_student(db=db, student=student)


@router.get("/get_students")
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_students(db, skip=skip, limit=limit)


@router.get("/students/{roll_num}", response_model=schemas.StudentsCreate)
def get_student_by_roll_num(roll_num: str, db: Session = Depends(get_db)):
    student = crud.get_student_by_roll_num(db, roll_num=roll_num)
    if student is None:
        raise HTTPException(status_code=404, detail=f"Student with roll number {roll_num} does not exist")
    return student

@router.put("/student/{roll_num}", response_model=schemas.StudentsCreate)
def update_student_by_roll_num(roll_num: str, student_data: schemas.StudentsUpdate, db: Session = Depends(get_db)):
    student_check = crud.get_student_by_roll_num(db, roll_num=roll_num)
    if student_check is None:
        raise HTTPException(status_code=404, detail=f"Student with roll number {roll_num} does not exist")
    
    updated_student = crud.update_students(db, roll_num, student_data)
    
    if updated_student:
        return updated_student
    else:
        raise HTTPException(status_code=404, detail=f"Failed to update student with roll number {roll_num}")
    
@router.post("/student_internal/{roll_num}",response_model=schemas.InternalsCreate)
def enter_student_marks_by_roll_num(roll_num: str, students_marks: schemas.InternalsCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_roll_num(db,roll_num=roll_num)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student with roll number {roll_num} does not exist")
    
    student_check = crud.get_student_internal_by_student_id(db, student_id=db_student.id)
    
    if student_check:
        raise HTTPException(status_code=400, detail=f"Student with roll number {roll_num} already exists")
    
    # Call the crud function with consistent parameter names
    enter_marks = crud.enter_students_marks(db=db, roll_num=roll_num, students_mark=students_marks)
    return enter_marks

@router.put("/edit_student_internal/{roll_num}",response_model=schemas.InternalsUpdate)
def update_student_marks(roll_num: str, students_marks: schemas.InternalsUpdates, db:Session = Depends(get_db)):
    db_student = crud.get_student_by_roll_num(db,roll_num=roll_num)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f'Student with roll number {roll_num} does not exist')
    
    internals_check = crud.get_student_internal_by_student_id(db,student_id=db_student.id)

    if internals_check is None:
        raise HTTPException(status_code=404, detail=f'Internal Mark of the Student with roll number {roll_num} does not exist')
    
    update_marks = crud.update_student_marks(db=db,roll_num=roll_num,internals_data=students_marks)
    return update_marks

@router.get("/get_student_marks_by_roll_num/{roll_num}",response_model=schemas.InternalsCreate)
def get_student_marks(roll_num:str,db:Session=Depends(get_db)):
    db_student = crud.get_student_by_roll_num(db,roll_num=roll_num)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f'Student with roll number {roll_num} does not exist')
    
    internals_check = crud.get_student_internal_by_student_id(db,student_id=db_student.id)

    if internals_check is None:
        raise HTTPException(status_code=404, detail=f'Internal Mark of the Student with roll number {roll_num} does not exist')
    
    return internals_check

@router.get("/get_students_report/{roll_num}",response_model=schemas.StudentInternalsResponse)
def get_students_data(roll_num:str,db:Session=Depends(get_db)):
    db_student=crud.get_student_by_roll_num(db,roll_num=roll_num)
    if db_student is None:
        raise HTTPException(status_code=404, detail=f'Student with roll number {roll_num} does not exist')
    
    internals_check = crud.get_student_internal_by_student_id(db,student_id=db_student.id)

    if internals_check is None:
        raise HTTPException(status_code=404, detail=f'Internal Mark of the Student with roll number {roll_num} does not exist')
    
    students_report = crud.get_students_report(db,roll_num=roll_num)

    return students_report
