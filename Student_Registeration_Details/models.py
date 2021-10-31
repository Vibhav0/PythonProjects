from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):
    __tablename__ = "tbl_student"
    s_id = Column(Integer, primary_key=True, index=True)
    u_id = Column(Integer, ForeignKey("tbl_user.u_id"))
    student_name = Column(String)
    college_name = Column(String)
    specialization = Column(String)
    degree_name = Column(String)
    internship_applied=Column(String)
    phone_no=Column(Integer,unique=True)
    email=Column(String,unique=True)
    location=Column(String)
    gender=Column(String)
    notes=Column(String)
    user = relationship("User", back_populates="student")


class User(Base):
    __tablename__ = "tbl_user"
    u_id = Column(Integer, primary_key=True, index=True)
    username=Column(String,unique=True)
    password=Column(String)
    is_active = Column(Boolean, default=False)
    student = relationship("Student", back_populates="user")
