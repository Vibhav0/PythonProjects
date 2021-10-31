from fastapi import APIRouter, Request, Form, Depends, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from .templates_ import templates
from hashing import get_password_hash, verify_password
import models
from database import get_db, SessionLocal
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/signup",
    tags=["Signup"]
)


@router.get("/", response_class=HTMLResponse)
async def user_signup(request: Request):
    return templates.TemplateResponse("signup.html", context={"request": request, "main_text": "Register", "text1": "Enter your details to register", "text2": "We don't share your data", "button": "Continue", "link": "/signup/details","title":"Register"})


@router.post("/details", response_class=RedirectResponse,status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def signup(request: Request, response: Response, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    old_user = db.query(models.User).filter(
        models.User.username == username).first()
    if not old_user:
        hashed_password = await get_password_hash(password)
        new_user = models.User(username=username, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        response.set_cookie(key="uid", value=str(new_user.u_id))
        return ("/details")
    else:
        return templates.TemplateResponse("signup.html", context={"request": request, "main_text": "Register", "text1": "Enter your details to register", "text2": "We don't share your data", "button": "Continue", "link": "/signup/details", "message": "Username already exits", "tag": "warning","title":"Register"})
