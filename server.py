import socket
import threading
def handle_client(client_socket,client_address):
  print(f"Connected with {client_address}")
