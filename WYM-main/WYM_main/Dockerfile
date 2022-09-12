FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN pip install Flask

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "myflask.py" ]
