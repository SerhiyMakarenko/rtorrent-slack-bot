# The MIT License
#
# Copyright (c) 2020, Serhiy Makarenko

FROM python:slim-buster

LABEL maintainer="serhiy.makarenko@me.com"

WORKDIR /var/lib/app

RUN mkdir /var/lib/app/lib && \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests build-essential

COPY src .

RUN pip install -r requirements.txt; rm requirements.txt && \
    apt-get purge -y --auto-remove build-essential  && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3", "-u", "slack_bot.py"]
