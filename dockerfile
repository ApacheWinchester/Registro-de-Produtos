 FROM python:3.9.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code
 
ADD requirements.txt /code/
 
COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt
 
EXPOSE 8081
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

COPY . /code/
