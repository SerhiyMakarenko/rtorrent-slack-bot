# The MIT License
#
# Copyright (c) 2020, Serhiy Makarenko

FROM debian:10-slim

LABEL maintainer="serhiy.makarenko@me.com"

WORKDIR /var/lib/app

RUN mkdir /var/lib/app/lib && \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    python3 python3-multidict python3-idna python3-yarl python3-chardet python3-async-timeout python3-aiohttp

COPY src .

RUN pip install -r requirements.txt; rm requirements.txt && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3", "-u", "slack_bot.py"]
