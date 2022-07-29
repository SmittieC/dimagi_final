from http import HTTPStatus

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import Config
from app.controllers import employee_controller
from app.datastructures import EmployeeForm
from app.db.base import session_generator

templates = Jinja2Templates(directory="app/templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "basic_form.html",
        {"request": request, "server_url": Config.SERVER_URL + "/update_location"},
        status_code=HTTPStatus.OK,
    )


@app.post("/update_location", response_class=HTMLResponse)
async def update_location(
    request: Request,
    session: Session = Depends(session_generator),
):
    form_data = await request.form()
    employee_data = EmployeeForm(city=form_data["city"], email=form_data["email"])
    employee_controller.update_employee_location(employee_data, db_session=session)

    view_args = {"updated": True}  # TODO: Finish off
    return templates.TemplateResponse(
        "basic_form.html",
        {"request": request, **view_args},
        status_code=HTTPStatus.OK,
    )
