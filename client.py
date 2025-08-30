import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disconnect"
SERVER = "192.168.1.9"  # Replace with your server's IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            if msg:
                print(msg)
        except:
            break

def send():
    while True:
        msg = input("")
        message = msg.encode(FORMAT)
        msg_length = str(len(message)).encode(FORMAT)
        msg_length += b' ' * (HEADER - len(msg_length))
        client.send(msg_length)
        client.send(message)

        if msg == DISCONNECT_MESSAGE:
            client.close()
            break

threading.Thread(target=receive, daemon=True).start()
send()