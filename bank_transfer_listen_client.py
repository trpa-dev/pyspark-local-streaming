#!/usr/bin/env python

from datetime import datetime
import json
import socket


HOST, PORT = '127.0.0.1', 9999


def main():
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.connect((HOST, PORT))

    while True:
        msg = main_socket.recv(1024)
        if msg:
            received = str(datetime.now())
            received += ', received data:\n'
            received += json.dumps(
                json.loads(msg.decode()), indent=4
            )
            print(received)
            main_socket.close()


if __name__ == '__main__':
    main()
