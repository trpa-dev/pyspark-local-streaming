#!/usr/bin/env python

from datetime import datetime
import json
from random import choices
import random
import socket
import time


HOST, PORT = 'localhost', 9999


account_regions = [
    'African Free Trade Zone',
    'Eurasia Trade Zone',
    'South Asian Trade Zone',
    'North American Trade Zone',
    'East Asian Trade Zone'
]
account_weight = [0.1, 0.2, 0.05, 0.4, 0.25]


def generate_transaction_data():
    account_id = random.randint(100000, 999999)
    account_region = choices(account_regions, account_weight)[0]
    transaction_value = round(random.uniform(0.01, 10000.0), 2)
    transaction_data = {
        'account_id': account_id,
        'account_region': account_region,
        'transaction_value': transaction_value
    }
    return json.dumps(transaction_data)


def main():
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    main_socket.bind((HOST, PORT))
    print('Bound port', HOST, PORT)

    main_socket.listen(5)

    while True:
        connection, addr = main_socket.accept()
        print('Connection from', str(addr))

        while True:
            data_str = generate_transaction_data() + '\n'
            try:
                print(f"{datetime.now()}, sending to all")
                connection.sendall(data_str.encode())
            except BrokenPipeError:
                print('Closed from', str(addr))
                break
            time.sleep(random.uniform(0.01, 3))
        connection.close()


if __name__ == '__main__':
    main()
