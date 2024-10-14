FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
