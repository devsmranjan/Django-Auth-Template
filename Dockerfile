FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /djangoapp
WORKDIR /djangoapp

COPY requirements.txt /djangoapp/
RUN pip install -r requirements.txt
COPY . /djangoapp/