import socket

def start_server():
    host = '127.0.0.1'
    port = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is ready to connect at {host}:{port}")

    conn,addr = server_socket.accept()
    print(f"connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"client: {data}")
        if data.lower() == 'exit':
            print("client diconnected")
            break
    conn.close()
    server_socket.close()
    print("Server shutdow")

if __name__ == "__main__":
    start_server()
    