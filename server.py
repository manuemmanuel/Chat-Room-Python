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
      print(f"[{client_address[0]}:{client_address[1]}]: {message}")
      broadcast(message, client_socket)
    except:
      print(f"Connection closed by {client_address}")
      break
