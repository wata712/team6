# -*- coding: utf-8 -*-
import socket
import sys

def client():
    ip = "127.0.0.1"
    port = 50001
    fname = "学生リスト.csv"
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

client()