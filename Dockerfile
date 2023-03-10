FROM python:3.10.0-slim-buster

WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "app.eindproject:app", "--host", "0.0.0.0", "--port", "8000"]
