from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from routers import signup, student_details, login, show_details, logout
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


models.Base.metadata.create_all(bind=engine)

app.include_router(signup.router)
app.include_router(student_details.router)
app.include_router(login.router)
app.include_router(show_details.router)
app.include_router(logout.router)

# redirect to login page
@app.get("/", status_code=status.HTTP_308_PERMANENT_REDIRECT)
async def redirect_user():
    return RedirectResponse("/login/")
