FROM ubuntu:16.04

MAINTAINER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./pip-requirements.txt /app/pip-requirements.txt

WORKDIR /app

RUN pip install -r pip-requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]