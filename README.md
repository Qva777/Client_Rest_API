<h1>📍How to install: </h1>
<h4>1 - Connect venv:</h4> 
<i>python -m venv venv</i>
<h4>2 - Activate it:</h4> 
<ul>
  <li>cd venv</li>
  <li>cd Scripts</li>
  <li>activate</li>
</ul>
<h4>3 - In the Console, go to the root folder:</h4>
<i>cd ../..</i>
<h4>4 - Install libraries:</h4>
<i>pip install -r requirements.txt</i>
<h4>5 - Run the migration:</h4> 
<i>python manage.py makemigrations</i>
<h4>6 - Apply migration:</h4> 
<i>python manage.py migrate</i>
<h4>7 - Run server:</h4> 
<i>python manage.py runserver</i>

<h1>📮How to connect Postman: </h1>
<h4>1 - Import Postman_Client folder into Postman</h4> 
<h4>2 - The environment settings are called User Data</h4>
<h4>3 - The Client_API collection contains requests</h4>