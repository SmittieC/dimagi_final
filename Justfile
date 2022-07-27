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
    uvicorn app.server:app --reload
