FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y sqlite3 libsqlite3-dev

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt .
RUN  apk add -U --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install -U pip setuptools && pip install --no-cache-dir -r requirements.txt

COPY . .