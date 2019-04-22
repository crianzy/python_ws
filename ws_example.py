# -*- coding: utf-8 -*-

import time

from simple_ws import WebSocket


# import socket
#
# def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
#     """Set TCP keepalive on an open socket.
#
#     It activates after 1 second (after_idle_sec) of idleness,
#     then sends a keepalive ping once every 3 seconds (interval_sec),
#     and closes the connection after 5 failed ping (max_fails), or 15 seconds
#     """
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
#     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)
#
#
# def set_keepalive_osx(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
#     """Set TCP keepalive on an open socket.
#
#     sends a keepalive ping once every 3 seconds (interval_sec)
#     """
#     # scraped from /usr/include, not exported by python's socket module
#     TCP_KEEPALIVE = 0x10
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#     sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, interval_sec)

class WSHandler(WebSocket):
    def on_message(self, msg, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for client in self.clients:
            if client.is_open():
                print("Client on_message!", msg, "  time", cur_date)
                # client.write_message(msg)

    def on_open(self, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Client connected!time = ", cur_date)

    def on_close(self, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Client left...time = ", cur_date)

    def on_ping(self, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Recieved ping! time = ", cur_date)

    def on_pong(self, client):
        cur_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Recieved pong! time = ", cur_date)


host = ''
port = 80

ws = WSHandler(host, port, compression=True, ping=True, ping_interval=360)
