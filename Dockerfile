
FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
