import socket

def Start_server():
    host = '127.0.0.1'
    port = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host,port))
    print(f"Server is ready to connect at {host}:{port}")

    while True:
        data,addr = server_socket.recvfrom(1024)
        message = data.decode()

        print(f"client {addr}: {message}")


        if message.lower() == 'exit':
            print(f"client {addr}: disconnected")
            break

    server_socket.close()
    print("Server shutdown")

if __name__ == "__main__":
    Start_server()