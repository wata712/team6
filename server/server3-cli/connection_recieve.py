# -*- coding: utf-8 -*-
import socket
import sys

def client(ip, port, fname):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                #dt_now = datetime.datetime.now()
                #fname = dt_now.strftime('%Y%m%d%H%M%S') + "_received." + ext
                fname = '学生リスト.'+ext
                with open(fname, mode="ab") as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        conn.sendall(b'Received done')
                    exit()


