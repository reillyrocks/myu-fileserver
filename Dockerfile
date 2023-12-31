# syntax=docker/dockerfile:1.4
FROM --platform=linux/amd64 python:3.10 as fastapi

MAINTAINER reilly@keating.fans
LABEL name="reilly keating" maintainer="reilly@keating.fans"

WORKDIR /usr/src/api
RUN mkdir fastapp

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.5.0
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

#enable when no longer need --reload (remove mount from docker-compose)
#COPY fastapp fastapp
CMD [ "poetry", "run", "uvicorn", "fastapp.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload" ]


FROM --platform=linux/amd64 nginx:latest as proxy

#FROM --platform=linux/amd64 nginx:alpine as htmlfront
#
#WORKDIR /usr/src/webapp
#COPY frontend/landingpage.html /usr/share/nginx/html/index.html