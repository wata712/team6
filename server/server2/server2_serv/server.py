# server.py
import socket

ip_address = '127.0.0.1'
port = 7010
buffer_size = 4092

# Socketの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IP Adress とPort番号をソケット割り当てる
    s.bind((ip_address, port))
    # Socketの待機状態
    s.listen(5)
    # while Trueでクライアントからの要求を待つ
    while True:
        # 要求があれば接続の確立とアドレス、アドレスを代入
        conn, addr = s.accept()
        # データを受信する
        data = conn.recv(buffer_size)
        print('data-> {}, addr->{}'.format(data, addr))
        # データを送信する
        conn.sendall(b'I received the data correctly.')
        