python -m venv venv
cd venv
cd Scripts
activate & cd ../.. & pip install -r requirements.txt  & echo SECRET_KEY=YOUR_SECRET_KEY ^

PASSWORD=YOUR_PASSWORD_FOR_PgDB > .env & ^
python manage.py makemigrations & python manage.py migrate & python manage.py runserver