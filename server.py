import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection closed by {client_address}")
                break
            print(f"[{client_address[0]}:{client_address[1]}]: {message}")
            broadcast(message, client_socket)
        except ConnectionResetError:
            print(f"Connection reset by {client_address}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    remove_client(client_socket)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                remove_client(client)

def remove_client(client):
    with clients_lock:
        if client in clients:
            clients.remove(client)

def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening for incoming connections on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            with clients_lock:
                clients.append(client_socket)

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down the server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    clients = []
    clients_lock = threading.Lock()
    main()
