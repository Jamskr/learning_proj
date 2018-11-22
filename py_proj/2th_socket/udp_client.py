#!/usr/bin/python
#-*-encoding:UTF-8-*-

import socket

def udp_socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for data in ['xiaomeng', 'xiaozhi']:
        host = socket.gethostname()
        port = 9999
        s.sendto(data.encode('utf-8'), (host, port))
        print(s.recv(1024).decode('utf-8'))
    s.close()

def main():
    udp_socket_client()

if __name__ == "__main__":
    main()