from http import HTTPStatus
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.base import session_scope
from app.db.models.user import User

templates = Jinja2Templates(directory="app/templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "create_user.html",
        {"request": request, "create_user_url": "http://localhost:8000"},
        status_code=HTTPStatus.OK
    )


@app.get("/users", response_class=HTMLResponse)
async def view_users(request: Request):
    users = get_users()
    return templates.TemplateResponse(
        "view_users.html",
        {"request": request, "users": users},
        status_code=HTTPStatus.OK,
    )


def create_user(name: str, email: str) -> None:
    with session_scope() as session:
        user = User(name=name, email=email)
        session.add(user)


def get_users():
    users = []
    with session_scope() as session:
        for user in session.query(User).all():
            users.append({"name": user.name, "email": user.email})
    return users
