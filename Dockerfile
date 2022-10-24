FROM python

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update   && \
    apt-get -y upgrade  && \
    apt-get -y install requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]