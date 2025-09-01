import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

interface = "127.0.0.1"
port = 12345
socket.bind((interface, port))
print((f"socket bound to port: {port}"))

socket.listen()
print("Socket is listening")

conn, addr = sock.accept()
