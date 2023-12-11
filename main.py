import re, socket


class Endpoints:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port


def do_things(id, ip, port, endpoints_array):
    print(f"Doing things with endpoint {id}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)

    print(f"Server is listening on port {port}")

    while True:
        connection, address = server_socket.accept()
        print(f"Connection from {address}")
        data = connection.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}")
        connection.sendall(b"Hello, client! I received your message.")
        connection.close()


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
