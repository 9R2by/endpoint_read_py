import re


class Endpoints:
    def __init__(self, id, ip, port):
        self.id = id
        self.ip = ip
        self.port = port


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
