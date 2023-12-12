import multiprocessing
import random
import re
import socket
from time import sleep
import datetime

class Endpoints:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port


def local_node():
    file_path = 'endpoints.txt'
    endpoints_array = read_file_and_create_objects(file_path)
    for endpoint in endpoints_array:
        print(f"{endpoint.id}\t{endpoint.ip}\t{endpoint.port}")


    user_input = input("Enter a unique id: ")
    if len(endpoints_array) < 4:
        print("Not enough endpoints")
    else:
        for endpoint in endpoints_array:
            if endpoint.id == int(user_input):
                do_things(endpoint.id, endpoint.ip, endpoint.port, endpoints_array)


    print(f"Starting local node on port {port}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    while True:
        connection, address = server_socket.accept()
        print(f"Connection from {address}")
        data = connection.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}")
        ct = datetime.datetime.now()
        print("current time:-", ct)
        connection.close()


def neighbor_nodes():
    sleep(5)
    print(f"Starting neighbor nodes")
    file_path = 'endpoints.txt'
    endpoints_array = read_file_and_create_objects(file_path)
    for endpoint in endpoints_array:
        print(f"{endpoint.id}\t{endpoint.ip}\t{endpoint.port}")

    # for ports in x try catch if port is already in use and create new process else abort process

    print(f"Starting node on port {port}")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', int(server_port)))
    message = "test 123"
    client_socket.sendall((message.encode('utf-8')))
    client_socket.close()




def do_things(id, ip, port, endpoints_array):
    print(len(endpoints_array))
    different_endpoints = []
    # create 3 different random numbers
    candidates = [num for num in range(1, len(endpoints_array) + 1) if num != id]
    unique_numbers = random.sample(candidates, 3)
    print(unique_numbers)
    for endpoints in endpoints_array:
        if endpoints.id in unique_numbers:
            different_endpoints.append(endpoints)

    for endpoint in different_endpoints:
        print(f"{endpoint.id}\t{endpoint.ip}\t{endpoint.port}")

    different_ports = []

    for endpoints in different_endpoints:
        different_ports.append((endpoints.ip, endpoints.port))

    workers(port, different_ports)


def read_file_and_create_objects(file_path):
    endpoints_list = []
    with open(file_path, 'r') as file:
        for line in file:
            newlines_removed = line.rstrip("\n")
            regex_result = re.split(r'[:\s]', newlines_removed)
            if len(regex_result) == 3:
                endpoint_id = int(regex_result[0])
                ip_address = regex_result[1]
                port = int(regex_result[2])
                endpoints_list.append(Endpoints(endpoint_id, ip_address, port))
    return endpoints_list


if __name__ == "__main__":
    # start process of local node
    # start process of starting neighbor nodes
    # port occupation check and error handling
    # instead of port removal do stateless check of port occupation
    # and assign only those where not error is on localhost

    print("Starting local and neighboring nodes")
    processes = []

    local_node = multiprocessing.Process(target=local_node)
    processes.append(local_node)
    local_node.start()

    # move this into the neighbor nodes function
    neighbor_nodes = multiprocessing.Process(target=neighbor_nodes)
    # client = multiprocessing.Process(target=client_function, args=(server_port,))
    processes.append(neighbor_nodes)
    neighbor_nodes.start()

    for process in processes:
        process.join()
