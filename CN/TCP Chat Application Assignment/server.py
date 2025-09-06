import socket

def Server_start():
    ip = '127.0.0.1'
    port = 8000
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((ip, port))
    socket_server.listen(1)
    print(f"Server is ready to connect at {ip}:{port}")

    conn,addr = socket_server.accept()
    print(f"connected by {addr}")

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        if data.lower() == 'exit':
            print("client disconnected")
            break

        print(f"client : {data}")

        server_msg = input("you (server): ")
        conn.send(server_msg.encode())

    conn.close()
    socket_server.close()
    print("server closed")

if __name__ == "__main__":
    Server_start()



