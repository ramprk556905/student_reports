from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException

def create_student(db: Session, student: schemas.StudentsCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_roll_num(db: Session, roll_num: str):
    return db.query(models.Student).filter(models.Student.roll_num == roll_num).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def update_students(db: Session, roll_num: str, student_data: schemas.StudentsUpdate):
    db_student = db.query(models.Student).filter(models.Student.roll_num == roll_num).first()
    
    if db_student:
        # Update fields with the data from student_data
        if student_data.name is not None:
            db_student.name = student_data.name
        if student_data.dept is not None:
            db_student.dept = student_data.dept
        if student_data.email is not None:
            db_student.email = student_data.email
        if student_data.regn_num is not None:
            db_student.regn_num = student_data.regn_num
        if student_data.dob is not None:
            db_student.dob = student_data.dob

        # Commit the transaction
        db.commit()
        db.refresh(db_student)

        return db_student
    return None

def get_student_internal_by_student_id(db:Session,student_id:int):
    db_student = db.query(models.Internals).filter(models.Internals.student_id == student_id).first()
    return db_student

def enter_students_marks(db: Session, roll_num: str, students_mark: schemas.InternalsBase):
    # Query the student ID based on the roll number
    db_student = db.query(models.Student.id).filter(models.Student.roll_num == roll_num).first()

    # Ensure db_student is found
    if db_student:
        # Extract the student ID from the tuple (db_student[0])
        db_student_mark = models.Internals(
            student_id=db_student[0],  # Extract the ID
            subject1=students_mark.subject1,
            subject2=students_mark.subject2,
            subject3=students_mark.subject3,
            subject4=students_mark.subject4,
            subject5=students_mark.subject5,
            subject6=students_mark.subject6
        )
        db.add(db_student_mark)
        db.commit()
        db.refresh(db_student_mark)
        return db_student_mark
    

def update_student_marks(db: Session, roll_num: str, internals_data: schemas.InternalsUpdate):
    db_student = db.query(models.Student).filter(models.Student.roll_num == roll_num).first()
    db_student_id = db.query(models.Internals).filter(models.Internals.student_id == db_student.id).first()

    if db_student_id:
        if internals_data.subject1 is not None:
            db_student_id.subject1 = internals_data.subject1
        if internals_data.subject2 is not None:
            db_student_id.subject2 = internals_data.subject2
        if internals_data.subject3 is not None:
            db_student_id.subject3 = internals_data.subject3
        if internals_data.subject4 is not None:
            db_student_id.subject4 = internals_data.subject4
        if internals_data.subject5 is not None:
            db_student_id.subject5 = internals_data.subject5
        if internals_data.subject6 is not None:
            db_student_id.subject6 = internals_data.subject6

        db.commit()
        db.refresh(db_student_id)
        return db_student_id
    return None

def get_students_id(db:Session,roll_num:str):
    students_id = db.query(models.Student.id).filter(models.Student.roll_num == roll_num).first()
    return students_id

def get_students_report(db:Session,roll_num:str):
    result=db.query(
        models.Student.id,
        models.Student.name,
        models.Student.dept,
        models.Student.roll_num,
        models.Internals.subject1,
        models.Internals.subject2,
        models.Internals.subject3,
        models.Internals.subject4,
        models.Internals.subject5,
        models.Internals.subject6
    ).join(models.Internals, models.Student.id == models.Internals.student_id
    ).filter(models.Student.roll_num == roll_num).first()

    return result