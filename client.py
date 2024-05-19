import socket
import threading

def receive_messages(client_socket):
  while True:
    try:
      message = client_socket.recv(1024).decode('utf-8')
      if not message:
        print("Connection to the server closed.")
        break

def send_messages(client_socket):
  while True:
    try:

    except:

      break
