import socket
import logging

logging.basicConfig(level=logging.INFO, filename='server.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4000))
sock.listen()
print("Server is running...")
logger.info("Server successfully works")
name = input("Enter your name: ")
conn, addr = sock.accept()

client = (conn.recv(1024)).decode()
print(f"{client} connected")
logger.warning("Someone connected to the server")
conn.send(name.encode())

while True:
    logger.error("the server has not written anything")
    message = input("Me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"{client}: {message}")
