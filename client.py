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
            message = input("[You]: ")
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
            break
def main():
  host = input("Enter the server IP address: ")
  port = int(input("Enter the server port: "))
  client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  try:
    client_socket.connect((host, port))
    print("Connected to the server.")
  except Exception as e:
    print(f"Unable to connect to the server: {e}")
    return
    
  receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

  
