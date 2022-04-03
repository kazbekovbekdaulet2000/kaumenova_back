FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN mkdir /app

COPY . /app

WORKDIR /app
COPY ./requirements.txt /requirements.txt
COPY ./.env ./.env
COPY ./scripts /scripts

RUN pip install -r requirements.txt
RUN chmod +x /scripts/*

CMD ["entrypoint.sh"]
