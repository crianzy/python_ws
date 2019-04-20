import time

from simple_ws import WebSocket


class WSHandler(WebSocket):
    def on_message(self, msg, client):
        for client in self.clients:
            if client.is_open():
                print("Client on_message!", msg)
                # client.write_message(msg)

    def on_open(self, client):
        print("Client connected!")

    def on_close(self, client):
        print("Client left...")

    def on_ping(self, client):
        print("Recieved ping!")

    def on_pong(self, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Recieved pong! time = ", cur_date)


host = ''
port = 8080

ws = WSHandler(host, port, compression=True, ping=True, ping_interval=5)

