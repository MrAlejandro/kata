FROM python:3

RUN mkdir /app
WORKDIR /app

VOLUME ["/app"]

CMD bash
