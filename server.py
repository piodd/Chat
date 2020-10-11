import socket
import select

HEADER_LENGHT = 10
IP = "127.0.0.1"
PORT = 1234

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sever_socket.bind((IP, PORT))

sever_socket.listen()

sockets_list = [sever_socket]

clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)

        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == sever_socket:
            client_socket, client_address = sever_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connection from{client_address[0]}:{client_address[1]}")
        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print("Recived message from")

            for client_socket in clients:
                print("wysłąno==",user['header'] + user['data'] + message['header'] + message['data'])
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
