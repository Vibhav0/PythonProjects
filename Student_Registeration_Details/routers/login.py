from fastapi import APIRouter, Request, Form, Depends, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from .templates_ import templates
from hashing import get_password_hash, verify_password
import models
from database import get_db, SessionLocal
from sqlalchemy.orm import Session
from hashing import verify_password
from jwt import create_access_token


router = APIRouter(
    prefix="/login",
    tags=["Login"]
)


@router.get("/", response_class=HTMLResponse)
async def user_login(request: Request):
    return templates.TemplateResponse("login.html", context={"request": request})


@router.post("/user", response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def authenticateUser(request: Request, response: Response, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == username).first()
    if not user:
        return templates.TemplateResponse("login.html", context={"request": request, "message": "User does not exist", "tag": "warning"})
    isCorrect = await verify_password(password, user.password)
    if not isCorrect:
        return templates.TemplateResponse("login.html", context={"request": request, "message": "Invalid Credentials", "tag": "danger"})
    token = await create_access_token(data={"sub": username})
    response.set_cookie("session", token)
    return ("/me")
