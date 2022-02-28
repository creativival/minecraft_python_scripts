# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1235))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# msg = s.recv(1024)
# print(msg.decode("utf-8"))

# coding: utf-8

# ソケット通信(クライアント側)
import socket
import select
import sys

ip1 = 'localhost'
port1 = 4711
server1 = (ip1, port1)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(server1)

line = ''
while line != 'bye':
    # 標準入力からデータを取得
    print('偶数の数値を入力して下さい')
    line = input('>>>')
    print(line)

    # readable, _, _ = select.select([socket1], [], [], 0.0)
    # if not readable:
    #     break
    # data = socket1.recv(1500)
    # if not data:
    #     socket1.close()
    #     raise ValueError('Socket got closed')
    # e =  "Drained Data: <%s>\n"%data.strip()
    # # e += "Last Message: <%s>\n"%self.lastSent.strip()
    # sys.stderr.write(e)

    # サーバに送信
    socket1.sendall(line.encode("utf-8"))
    print('send')

    # # サーバから受信
    # data1 = socket1.recv(4096).decode()
    # print('receive')
    #
    # # サーバから受信したデータを出力
    # print('サーバーからの回答: ' + str(data1))

socket1.close()
print('クライアント側終了です')