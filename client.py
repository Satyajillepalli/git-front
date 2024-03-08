# client.py   -- client side of the system!! websockets

    
import socket
import time

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    attempts = 0
    while attempts < 3:
        try:
            client_socket.connect(("localhost", 12345))
            client_socket.send(message.encode())
            client_socket.close()
            break
        except ConnectionRefusedError:
            print("Connection refused. Retrying...")
            attempts += 1
            time.sleep(1)

if __name__ == "__main__":
    message_to_send = "Hello, server!"
    send_message(message_to_send)

