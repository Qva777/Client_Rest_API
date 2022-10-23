FROM python

WORKDIR /app

RUN pip install django

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]