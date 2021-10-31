from fastapi import APIRouter,Request,Form,Depends,status,Response
from fastapi.responses import HTMLResponse
from .templates_ import templates
from hashing import get_password_hash,verify_password
import models
from database import get_db,SessionLocal
from sqlalchemy.orm import Session
from schemas import     User
from jwt import get_current_user
from database import get_db

router=APIRouter(
    prefix="/me",
    tags=["Details"]
)

@router.post("/")
async def user_details(request:Request,user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    student_details=db.query(models.Student).filter(models.Student.u_id==user.u_id).first()
    print(student_details)
    return templates.TemplateResponse("me.html", context={"request":request,"student":student_details})
