import socket
import threading
def handle_client(client_socket,client_address):
  print(f"Connected with {client_address}")
  while True:
    try:
      message = client_socket.recv(1024).decode('utf-8')
      if not message:
        print(f"Connection closed by {client_address}")
        break
