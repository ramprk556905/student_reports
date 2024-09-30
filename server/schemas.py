from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List,Optional

# Internals schema
class InternalsBase(BaseModel):
    subject1: int
    subject2: int
    subject3: int
    subject4: int
    subject5: int
    subject6: int

class InternalsUpdate(BaseModel):
    subject1: Optional[int] = None
    subject2: Optional[int] = None
    subject3: Optional[int] = None
    subject4: Optional[int] = None
    subject5: Optional[int] = None
    subject6: Optional[int] = None

class InternalsCreate(InternalsBase):
    student_id:Optional[int] = None
    pass

class InternalsUpdates(InternalsUpdate):
    student_id:Optional[int] = None
    pass

class Internals(InternalsBase):
    id: int
    student_id:int
    class Config:
        from_attributes = True  


# Students schema
class StudentsBase(BaseModel):
    roll_num: str  

class StudentsUpdate(BaseModel):
    roll_num: Optional[str]  = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    dept: Optional[str] = None
    regn_num: Optional[int] = None
    dob: Optional[date] = None

class StudentsCreate(BaseModel):
    roll_num:str
    name: str
    email: EmailStr
    dept: str
    regn_num: int
    dob: date

class Students(StudentsBase):
    id: int

    class Config:
        from_attributes = True  

class StudentInternalsResponse(BaseModel):
    id: int
    name: str
    dept: str
    roll_num: str
    subject1: int
    subject2: int
    subject3: int
    subject4: int
    subject5: int
    subject6: int

    class Config:
        from_attributes = True