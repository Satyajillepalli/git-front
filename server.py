# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Server listening on localhost:12345...")

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        print(f"Received from {addr}: {data.decode()}")
        client_socket.close()

except Exception as e:
    print(f"Error: {e}")

finally:
    server_socket.close()
