FROM python

RUN  pip install --upgrade pip

#it will be copied in /code/
COPY requirements.txt .

####WORKDIR /tmp
#we want to make sure that each of our dependencies are going to be installed in our container
RUN pip install -r requirements.txt
#RUN pip install --requirements requirements.txt

#copy the entire project to the directory that we have created
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]