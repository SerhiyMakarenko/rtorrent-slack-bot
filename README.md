Simple Slack Bot for rtorrent
=========================
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat)](https://github.com/SerhiyMakarenko/rakshasa-rtorrent-dockerized/blob/rakshasa-rtorrent-client/stable/LICENSE)

Slack Bot communicate with rtorrent directly over SCGI wrapped to UNIX socket using `xmlrpc.client` from the standard Python library.
Interface for SCGI communication over UNIX socket was originally written by [Roger Que](https://gist.github.com/query/899683).

# Details
Currently, the image supports the following CPU architectures:
 - x86_64 (amd64);
 - armhf (arm32v6);
 - arm7l (arm32v6);
 - aarch6 (arm64v8).

This means that the image can be used on regular PC's with Intel CPU as well as on single-board computers like Raspberry Pi with ARM CPU.

# Usage
To run container you need to execute command listed below:
```
docker run -d --name rtorrent-slack-bot --net=host \
    -e SOCKET_PATH=/tmp/rtorrent.sock \
    -e SLACK_BOT_USER_TOKEN=xoxb-XXXXXXXXXXXX-XXXXXXXXXXXX-XXXxxXxXXXXxxxXXXXxxxxxx \
    -e SLACK_CHANNEL=XXXXXXXXX \
    -v /path/to/rtorrent.sock:/tmp/rtorrent.sock \
    serhiymakarenko/rtorrent-slack-bot:latest
```
Please, keep in mind that you need running container with rtorrent. You can achieve this using [rakshasa-rtorrent-dockerized](https://github.com/SerhiyMakarenko/rakshasa-rtorrent-dockerized) image.
