FROM python:alpine3.20
WORKDIR /app

RUN pip install django
COPY . /app/
EXPOSE 800

CMD ["python" , "manage.py", "runserver" , "0.0.0.0:8000"]
