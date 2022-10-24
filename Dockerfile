FROM python

RUN  pip install --upgrade pip


COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]