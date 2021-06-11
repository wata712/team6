# -*- coding: utf-8 -*-
import socket
import datetime
import sys


def server(ip, port, ext):
    output_list = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                # dt_now = datetime.datetime.now()
                # fname = dt_now.strftime('%Y%m%d%H%M%S') + "_received." + ext
                fname = '学生リスト.'+ext
                with open(fname, mode="ab") as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        conn.sendall(b'Received done')
                    # exit()

def client(ip, port, fname):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        try:
            with open(fname, mode='rb') as f:
                for line in f:
                    s.sendall(line)
                    data = s.recv(1024)
                print(repr(data.decode()))
        except:
            pass


if __name__ == "__main__":
    if (sys.argv[1] == "s"):
        server((sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    if (sys.argv[1] == "c"):
        client((sys.argv[2]), int(sys.argv[3]), sys.argv[4])