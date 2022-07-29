requirements:
    pip install --quiet pip-tools
    pip-compile --output-file=requirements.txt requirements.in

setup-dev:
    @just requirements
    pip install -r requirements.txt -r requirements.in -r dev-requirements.in

fmt:
    isort .
    black .

lint:
    flake8 .
    black . --diff --check
    isort --diff --check .
    mypy .

run-server:
    uvicorn app.server:app --host=127.0.0.1 --port=8000 --reload

default_revision := "head"
default_downgrade_revision := "-1"

migrate revision=default_revision:
    alembic upgrade {{revision}}

makemigrations +ARGS='':
    alembic revision --autogenerate -m "{{ARGS}}"

test +ARGS='':
    python -m pytest {{ARGS}}

db-up:
    docker run -d --name dimagi_app_db -e POSTGRES_PASSWORD=dev -e POSTGRES_USER=dimagi -e POSTGRES_DB=backend -p 5432:5432 postgres:14-alpine    

db-down:
    docker stop dimagi_app_db
    docker rm dimagi_app_db --volumes
