#Шаги установки: 

####1 - Подключить venv командой: 
`python -m venv venv`

####2 - Активировать его, командой:
- `cd venv`
- `cd Scripts`
- `activate`

####3 - В Консоле прейти в папку рут, командой:
`cd ../..`

####4 - Установить библиотеки командой:
`pip install -r requirements.txt`

####5 - Выполнить мигрцию, командой:
`python manage.py makemigrations`

####6 - Применить мигрцию, командой:
`python manage.py migrate`

####7 - Создать суперюзера, командой:
`python manage.py createsuperuser`

####8 - Запустить сервер, командой:
`python manage.py runserver`