<h1>📍How to install: </h1>

<details><summary><h2>🧾Automatic command execution for the first run</h2></summary><br>
<ul>
  <li>🔧for Windows:     <b>first_start.bat</b></li>
  <li>⚙for Linux/MacOS: <b>sh first_start.sh</b></li>
</ul>
</details>
<details><summary><h2>⬇Manual start</h2></summary><br>
<h4>1 - Connect venv:</h4> 
<pre>python -m venv venv</pre>
<h4>2 - Activate it:</h4> 
<pre>.\venv\Scripts\activate</pre>
<h4>3 - Install libraries:</h4>
<pre>pip install -r requirements.txt</pre>
<h4>4 - Run the migration:</h4> 
<pre>python manage.py makemigrations</pre>
<h4>5 - Apply migration:</h4> 
<pre>python manage.py migrate</pre>
<h4>6 - Run server:</h4> 
<pre>python manage.py runserver</pre>
</details>

<details><summary><h1>📮How to connect Postman:</h1></summary><br/>
<h4>1 - Import Postman_Client folder into Postman</h4> 
<h4>2 - The environment settings are called User Data</h4>
<h4>3 - The Client_API collection contains requests</h4>
</details>

<details><summary><h1>🐳How to connect Docker Compose:</h1></summary><br/>
<h4>UP Docker-compose:</h4>
<pre>docker-compose up -d</pre>
</details>
