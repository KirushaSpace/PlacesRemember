FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY req.txt /code/
RUN pip install -r req.txt

COPY . /code/

CMD python manage.py runserver 0.0.0.0:8000