import socket

def start_client():
    host = '127.0.0.1'
    port = 8000
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((host, port))

    print("Connected to server. Type message (type 'exit' to quit).")
    while True:
        message = input()
        socket_client.send(message.encode())
        if message.lower() == 'exit':
            break

    socket_client.close()
    print("connection closed")

if __name__ == '__main__':
    start_client()