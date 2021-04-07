import socket

class DBConstants:
    Successful_update = 'UPDATE 1'
    Successful_delete = 'DELETE 1'
    DB_product = 'postgresql://postgres:ds5673@35.193.117.225:5432/product_database'
    DB_customer = 'postgresql://postgres:ds5673@35.232.192.83:5432/customer_database'


class Financial_transactions:
    host_and_port_wsdl = 'http://35.208.176.241:8002/?wsdl'
    success = 'Success'
    failure = 'Failure'

class UDP_constants:
    UDP_IP = "127.0.0.1"


global_sequence_number = 0
local_sequence_number = -1
current_host_number = 0
UDP_PORT = 5005
sequence_messsages = {}
request_messages = {}


class ABP_servers:
    hosts = [('127.0.0.1', 5005), ('127.0.0.1', 5006), ('127.0.0.1', 5007)]
    total_hosts = len(hosts)

class Request_Constants:
    context = 'origin_server'


sock = None

def init_sock():
    global sock
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((UDP_constants.UDP_IP, UDP_PORT))
    sock.settimeout(2)


def init_current_server_number(num):
    global current_host_number
    current_host_number = num


def get_current_server_number():
    return current_host_number


def init_udp_port(port):
    global UDP_PORT
    UDP_PORT = port


def get_current_server_udp_port():
    return UDP_PORT


def get_sequence_number(sequence_type):
    if sequence_type == 'global':
        return global_sequence_number
    else:
        return local_sequence_number


def incr_sequence_number(sequence_type):
    if sequence_type == 'global':
        global global_sequence_number
        global_sequence_number += 1
    else:
        global local_sequence_number
        local_sequence_number += 1

def set_global_sequence_number(num):
    global global_sequence_number
    global_sequence_number = max(global_sequence_number, num)


def insert_into_sequence_messages(key, value):
    global sequence_messsages
    sequence_messsages[key] = value
    print("sequence messages :- ", sequence_messsages)
    print('--------------------------------------------------')


def insert_into_request_messages(key, value):
    global request_messages
    request_messages[key] = value
    print("request messages :- ", request_messages)
    print('--------------------------------------------------')


def get_messages_dict(message_type):
    if message_type == 'global':
        return sequence_messsages
    else:
        return request_messages


def clear_dict(message_type):
    if message_type == 'global':
        global sequence_messsages
        sequence_messsages = {}
    else:
        global request_messages
        request_messages = {}


