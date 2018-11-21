#!/usr/bin/python
#-*-encoding:UTF-8-*-

import socket

def socket_client():
    s = socket.socket()

    # 获取本地主机名
    host = socket.gethostname()
    port = 9999

    # 建立连接
    s.connect((host, port))

    # 接收欢迎消息
    print(s.recv(1024).decode('utf-8'))
    for data in ['xiaomeng', 'xiaozhi', 'xiaoqiang']:
        # 发送数据
        s.send(data.encode('utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

def main():
    socket_client()

if __name__ == "__main__":
    main()