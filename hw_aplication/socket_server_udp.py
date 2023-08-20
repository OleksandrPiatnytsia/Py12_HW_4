import json
import logging
import pickle
import socket

from config import UDP_PORT, UDP_HOST

logging.basicConfig(level=logging.DEBUG)

JSON_PATH = "storage/data.json"


def run_udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = UDP_HOST, UDP_PORT
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)

            incoming_dict = pickle.loads(data)

            logging.debug(f'Received data: {pickle.loads(data)} from: {address}')

            with open(JSON_PATH, "r") as fdr:
                try:
                    data_dict: dict = json.load(fdr)
                except json.JSONDecodeError:
                    data_dict = {}

            data_dict.update(incoming_dict)

            with open(JSON_PATH, "w") as fdw:
                json.dump(data_dict, fdw)

            # sock.sendto(data, address)
            # logging.debug(f'Send data: {data.decode()} to: {address}')

    except KeyboardInterrupt:
        logging.info(f'Destroy server')
    finally:
        sock.close()


if __name__ == '__main__':
    run_udp_server()
