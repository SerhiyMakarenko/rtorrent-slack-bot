import os
import time
import sched
import slack
import xmlrpc.client
from lib.rtorrent_xmlrpc import SCGIServerProxy

socket_path = os.environ["SOCKET_PATH"]
slack_bot_user_token = os.environ["SLACK_BOT_USER_TOKEN"]
slack_channel = os.environ["SLACK_CHANNEL"]
rtorrent = SCGIServerProxy('scgi://' + socket_path)
client = slack.WebClient(token=slack_bot_user_token)
execution_scheduler = sched.scheduler(time.time, time.sleep)


def send_slack_message(torrent_name):
    client.chat_postMessage(method='chat.postMessage', channel=slack_channel,
                            text='Torrent "{}" successfully downloaded. :eyes:'.format(torrent_name))


def get_pending_torrents():
    downloading_torrents = rtorrent.download_list("", "incomplete")
    if downloading_torrents:
        for torrent in downloading_torrents:
            if torrent not in pending_torrents:
                pending_torrents.append(torrent)


def scheduler(execution_scheduler):
    get_pending_torrents()
    print("Pending torrents: " + str(pending_torrents))
    if pending_torrents:
        for torrent in pending_torrents:
            try:
                if rtorrent.d.complete(torrent) == 1:
                    torrent_name = rtorrent.d.name(torrent)
                    send_slack_message(torrent_name)
                    pending_torrents.remove(torrent)
            except xmlrpc.client.Fault:
                print("Removing torrent with hash " + torrent + "from pending list, probably it was removed manually "
                                                                "from rtorrent.")
                pending_torrents.remove(torrent)
    execution_scheduler.enter(10, 1, scheduler, (execution_scheduler,))


if __name__ == "__main__":
    pending_torrents = []
    execution_scheduler.enter(10, 1, scheduler, (execution_scheduler,))
    execution_scheduler.run()
