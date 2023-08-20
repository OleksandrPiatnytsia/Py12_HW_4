from threading import Thread

from http_server import run_http_server
from socket_server_udp import run_udp_server

if __name__ == '__main__':

    threads = []

    thread = Thread(target=run_http_server)
    thread.start()
    threads.append(thread)

    thread = Thread(target=run_udp_server)
    thread.start()
    threads.append(thread)

    [el.join() for el in threads]