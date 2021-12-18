FROM python:3.9.0

WORKDIR /home/

RUN echo "testing9"

RUN git clone https://github.com/flightcheck77/pragmatic2.git

WORKDIR /home/pragmatic2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic2.settings.deploy && python manage.py migrate --settings=pragmatic2.settings.deploy && gunicorn pragmatic2.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic2.settings.deploy --bind 0.0.0.0:8000"]

