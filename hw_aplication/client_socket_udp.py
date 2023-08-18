import logging
import pickle
import socket

from config import UDP_PORT, UDP_HOST


def send_data_by_udp(dict_data: dict):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        server = UDP_HOST, UDP_PORT

        binary_data = pickle.dumps(dict_data)
        sock.sendto(binary_data, server)

        # response, address = sock.recvfrom(1024)
        # logging.debug(f'Response data: {response.decode()} from address: {address}')

