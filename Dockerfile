# The MIT License
#
# Copyright (c) 2019, Serhiy Makarenko

FROM python:slim-buster

LABEL maintainer="serhiy@makarenko.me"

WORKDIR /var/lib/app

RUN mkdir /var/lib/app/lib

COPY src .

RUN pip install -r requirements.txt; rm requirements.txt

ENTRYPOINT ["python3", "-u", "slack_bot.py"]