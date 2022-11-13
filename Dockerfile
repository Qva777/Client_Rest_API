FROM python:3.8
LABEL "name"="I'm author prod"
#RUN  pip install --upgrade pip
#ENV PYTHONDONTWRITEBYTECODE 1
# Main directory
WORKDIR /app
# Run install pip and libraries
RUN pip install pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
