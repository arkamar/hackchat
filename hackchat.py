import json
import websocket

class HackChat:
    def __init__(self, nick, channel="programming"):
        self.nick = nick
        self.channel = channel

        self.on_message = []
        self.on_join = []

        self.ws = websocket.create_connection("wss://hack.chat/chat-ws")
        self.ws.send(json.dumps({"cmd": "join", "channel": channel, "nick": nick}))

    def run(self):
        result = json.loads(self.ws.recv())
        if result["cmd"] == "chat" and not result["nick"] == self.nick:
            for handler in list(self.on_message):
                handler(self, result["text"], result["nick"])
        elif result["cmd"] == "onlineAdd":
            for handler in list(self.on_join):
                handler(self, result["nick"])
        return result

    def run_loop(self):
        while True:
            self.run()

    def send_message(self, msg):
        self.ws.send(json.dumps({"cmd": "chat", "text": msg}))