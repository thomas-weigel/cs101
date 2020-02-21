#!/usr/bin/env python3

import socket
import time


def comm():
    CONN = ('127.0.0.1', 9997)
    PROMPT = '> '

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(CONN)

    try:
        while True:
            msg = input(PROMPT).encode()
            client.send(msg)
            time.sleep(0.1)
            data = client.recv(1024).decode()
            print(data)
    except:
        print("Goodbye")

    client.close()


if __name__=='__main__':
    print('hello')
    comm()
