#! /usr/bin/env python3

from hackchat import HackChat
from sys import argv, stdout, stderr, exit

def usage():
    print("Usage: hc-bot <channel> [nick]");

def message_got(chat, message, sender):
    line = '{:>10} {:>15}: {}'.format(channel, sender, message)
    print(line)
    stdout.flush()

channel = None
nick = "awrkdiakglqu23"

if len(argv) > 1:
    channel = argv[1]
else:
    usage()
    exit(1)

if len(argv) > 2:
    nick = argv[2]

print("Trying to conect channel", channel, file=stderr)

chat = HackChat(nick, channel)
chat.on_message.append(message_got)

print("starting bot", file=stderr)
stderr.flush()
chat.run()
print("shutting down", file=stderr)
