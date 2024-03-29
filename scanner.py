import socket
import sys
import threading
import time


def run_scanner(callback):

    def scanner_thread():
        scanner = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        scanner.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        scanner.bind(('', 1337))

        sel_flag = 'sel-transmitter'

        while True:
            data, (ip, _) = scanner.recvfrom(1024)
            data = data.decode('utf-8')
            if data[0:len(sel_flag)] == sel_flag:
                port = data[len(sel_flag) + 1:]
                callback((ip, port))

    threading.Thread(target=scanner_thread).start()
