import socket
import threading

def receive_messages(client_socket):
  while True:
    try:
      message = client_socket.recv(1024).decode('utf-8')
      print("\n[Server]:",message)
    except:
      print("Connection to the server closed.")

def send_messages(client_socket):
  while True:
    

def main():
