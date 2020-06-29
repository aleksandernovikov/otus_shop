FROM python:3.7-slim

WORKDIR /app
ADD . /app/


RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=shop.production_settings SECRET_KEY=O&dfefy@wl7pa5tn!xbr(5_&nd6oh@0t)80sdfhklsfqw
ENV SENTRY_DSN=https://e37ee4e3299a4c1c9c8dfff24e64cee4@o263431.ingest.sentry.io/5300525
RUN python manage.py migrate
RUN python manage.py populate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]