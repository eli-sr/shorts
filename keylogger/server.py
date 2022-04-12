#!/usr/bin/env python3
import socket

LHOST = str(socket.INADDR_ANY)
LPORT = 9000

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((LHOST,LPORT))
    s.listen()
    print(f"[*] Listening at {LHOST}:{LPORT}")
    while True:
        conn,addr = s.accept()
        print(f"[+] New connection:",addr)
        data_list = []
        packet = conn.recv(4096)
        while packet != b'':
            data_list.append(packet)
            packet = conn.recv(4096)
        conn.close()
        data = b''.join(data_list)
        f = open(addr[0]+".txt","wb")
        f.write(data)
        f.close()

