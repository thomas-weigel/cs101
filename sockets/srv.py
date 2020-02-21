#!/usr/bin/env python3

import socket


def serve_echo():
    CONN = ('127.0.0.1', 9997)

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(CONN)
    srv.listen(5)

    while True:
        conn, addr = srv.accept()
        print(f'srv connection from: {addr}')
        data = 'Beginning Connection! '
        while data:
            print(data)
            conn.send(b'Received: ' + data.encode())
            data = conn.recv(1024).decode()
        conn.close()


if __name__=='__main__':
    serve_echo()
