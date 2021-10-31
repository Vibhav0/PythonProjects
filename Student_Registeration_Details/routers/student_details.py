from fastapi import APIRouter, Request, Form, Depends, status, Response, Cookie, status
from fastapi.responses import HTMLResponse, RedirectResponse
from .templates_ import templates
from hashing import get_password_hash, verify_password
import models
from database import get_db, SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import APIKeyCookie
from typing import Optional


router = APIRouter(
    prefix="/details",
    tags=["Students Details"]
)
cookie_sec = APIKeyCookie(name="uid")


@router.post("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def details_page(request: Request):
    return templates.TemplateResponse("details.html", context={"request": request, "title": "Details", "text1": "Student Details"})


@router.post("/student", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def student_details(request: Request, response: Response, uid: Optional[str] = Cookie(None), username: str = Form(...), clg_name: str = Form(...), specialization: str = Form(...), d_name: str = Form(...), internships: str = Form(...), p_number: str = Form(...),
                          email: str = Form(...), location: str = Form(...), gender: str = Form(...), notes: str = Form(...), db: Session = Depends(get_db)):
    if uid:
        old_email = db.query(models.Student).filter(
            models.Student.email == email).first()
        old_p_number = db.query(models.Student).filter(
            models.Student.phone_no == p_number).first()
        if old_email:
            return templates.TemplateResponse("details.html", context={"request": request, "title": "Details", "text1": "Student Details", "message": "Email is already taken", "tag": "warning"})
        if old_p_number:
            return templates.TemplateResponse("details.html", context={"request": request, "title": "Details", "text1": "Student Details", "message": "Phone Number is already taken", "tag": "warning"})

        new_student = models.Student(student_name=username, u_id=uid, college_name=clg_name, specialization=specialization, degree_name=d_name,
                                     internship_applied=internships, phone_no=p_number, email=email, location=location, gender=gender, notes=notes)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        template_response=templates.TemplateResponse("login.html", context={"request": request, "message": "Welcome {} Please provide your detalis to login into your account".format(username), "tag": "info", "title": "Login", "text1": "Login", "text2": "Good to see you around {}".format(username), "button": "Login"})
        response.delete_cookie("uid")
        return template_response    
    else:
        return templates.TemplateResponse("details.html", context={"request": request, "message": "Seems you havent created your user account. Try again!", "tag": "danger"})
