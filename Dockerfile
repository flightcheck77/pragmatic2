FROM python:3.8.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/flightcheck77/pragmatic2.git

WORKDIR /home/pragmatic2/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-s%!o)1%co5fzyriok6e^ct)y9*a%w+dqy4le()62s)a^+b1+1_" > .env

RUN export DJANGO_SETTINGS_MODULE=pragmatic2.settings

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic2.settings.deploy && gunicorn pragmatic2.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic2.settings.deploy --bind 0.0.0.0:8000"]