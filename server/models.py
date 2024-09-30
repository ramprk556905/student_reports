from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Date
from sqlalchemy.orm import relationship
from databases import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))  
    roll_num = Column(String(50), unique=True, nullable=False)  
    dept = Column(String(100), nullable=False)  
    email = Column(String(150), unique=True, index=True, nullable=False)
    regn_num = Column(BigInteger, unique=True, nullable=False)
    dob = Column(Date, nullable=False)

    internals = relationship("Internals", back_populates="student")

class Internals(Base):
    __tablename__ = "internals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject1 = Column(Integer, index=True, nullable=False)
    subject2 = Column(Integer, index=True, nullable=False)
    subject3 = Column(Integer, index=True, nullable=False)
    subject4 = Column(Integer, index=True, nullable=False)
    subject5 = Column(Integer, index=True, nullable=False)
    subject6 = Column(Integer, index=True, nullable=False)

    student = relationship("Student", back_populates="internals")
