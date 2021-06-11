# client.py
import socket

ip_address = '127.0.0.1'
port = 7010
buffer_size = 4092

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーに接続を要求する
    s.connect((ip_address, port))
    # データを送信する
    s.sendall(b'I sent a message.')
    # サーバーからのデータを受信
    data = s.recv(buffer_size)

    print(data.decode())