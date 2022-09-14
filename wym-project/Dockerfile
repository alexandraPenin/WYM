FROM python:3.10.6

#RUN apt-get update && apt-get install -y \

#   python3-pip python3-dev git

#RUN pip3 install --upgrade pip

#RUN pip3 install Flask

#RUN pip install -r requirements.txt

COPY dist /wheel

RUN pip install wheel/*.whl

WORKDIR /app

COPY . /app


