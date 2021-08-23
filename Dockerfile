FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . .
RUN pip3 install -e .
RUN ["chmod", "+x", "./colorbrains_api/scripts/launch-and-populate-data.sh"]
