<h1>📍How to install: </h1>

<details><summary><h2>🧾Automatic command execution for the first run</h2></summary><br>
<ul>
  <li>🔧for Windows:     <b>first_start.bat</b></li>
  <li>⚙for Linux/MacOS: <b>first_start.sh</b></li>
</ul>
</details>
<details><summary><h2>⬇Manual start</h2></summary><br>
<h4>1 - Connect venv:</h4> 
<i>python -m venv venv</i>
<h4>2 - Activate it:</h4> 
<i>.\venv\Scripts\activate</i>
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
</details>

<details><summary><h1>📮How to connect Postman:</h1></summary><br/>
<h4>1 - Import Postman_Client folder into Postman</h4> 
<h4>2 - The environment settings are called User Data</h4>
<h4>3 - The Client_API collection contains requests</h4>
</details>

<details><summary><h1>🐳How to connect Docker Compose:</h1></summary><br/>
<h4>UP Docker-compose:</h4>
<i>docker-compose up -d</i>
</details>