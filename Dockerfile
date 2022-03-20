FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY requirements /app/requirements.txt

COPY colorbrains_api /app/colorbrains_api/

RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "--host=0.0.0.0", "--port=80", "colorbrains_api.rest:app" ]