from http import HTTPStatus

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import Config
from app.controllers import employee_controller
from app.datastructures import EmployeeForm
from app.db.base import session_generator
from app.exceptions import EmployeeException

templates = Jinja2Templates(directory="app/templates")
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

view_args = {
    "update_url": Config.SERVER_URL + "/update_location",
    "error_message": "",
    "updated": False,
    "success": True,
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    view_args["updated"] = False
    return templates.TemplateResponse(
        "basic_form.html",
        {"request": request, **view_args},
        status_code=HTTPStatus.OK,
    )


@app.post("/update_location", response_class=HTMLResponse)
async def update_location(
    request: Request,
    session: Session = Depends(session_generator),
):
    form_data = await request.form()
    employee_data = EmployeeForm(city=form_data["city"], email=form_data["email"])

    try:
        employee_controller.update_employee_location(employee_data, db_session=session)
    except EmployeeException as exception:
        view_args["success"] = False
        view_args["error_message"] = exception.message

    return templates.TemplateResponse(
        "basic_form.html",
        {"request": request, **view_args},
        status_code=HTTPStatus.OK,
    )


@app.post("/locations", response_class=HTMLResponse)
async def employee_locations(
    request: Request,
    session: Session = Depends(session_generator),
):
    form_data = await request.form()
    employee_data = EmployeeForm(city=form_data["city"], email=form_data["email"])

    return templates.TemplateResponse(
        "employees.html",
        {"request": request},
        status_code=HTTPStatus.OK,
    )
