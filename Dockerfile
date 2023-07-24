# syntax=docker/dockerfile:1.4
FROM --platform=linux/amd64 python:3.10 as fastapi

MAINTAINER reilly@keating.fans
LABEL name="reilly keating" maintainer="reilly@keating.fans"

WORKDIR /usr/src/api
RUN mkdir app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.5.0
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

#enable when no longer need --reload
#COPY app app
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8888", "--reload" ]


FROM --platform=linux/amd64 nginx:latest as proxy

