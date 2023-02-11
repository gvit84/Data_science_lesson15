import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("Enter your name: ")
sock.connect(('localhost', 4000))
sock.send(name.encode())
socket_name = sock.recv(1024)
sock_name = socket_name.decode()
print(f"{sock_name} connected")

while True:
    message = (sock.recv(1024)).decode()
    print(f"{sock_name}: {message}")
    message = input("Me: ")
    sock.send(message.encode())
