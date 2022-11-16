python -m venv venv
cd venv
cd Scripts
activate && cd ../.. && pip install -r requirements.txt  && python manage.py makemigrations ^
&& python manage.py migrate && python manage.py runserver