import socket

def Start_client():
    host = '127.0.0.1'
    port = 8000
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Connected to server. Type message (type 'exit' to quit).")
    while True:
        message = input()
        socket_client.sendto(message.encode(), (host,port))

        if message.lower() == 'exit':
            break
    socket_client.close()
    print("Connection closed")


if __name__ == '__main__':
    Start_client()