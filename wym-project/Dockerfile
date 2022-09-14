FROM python:3.10.6

COPY ./dist/*.whl /tmp

RUN pip install /tmp/*.whl

WORKDIR /app

CMD start-server

