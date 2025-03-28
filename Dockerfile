FROM python:3.13-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
