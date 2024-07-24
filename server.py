import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET means that the first argument in the socket is the ipv4(different from ipv6)
# socket.SOCK_STREAM means that the second argument in the socket is TCP connection.

ip_address = "127.0.0.1"
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []
nicknames = []

def remove_nickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

def broadcast(message, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(conn):
    if conn in clients:
        clients.remove(conn)



def client_thread(conn, nickname):
    conn.send("Welcome to this chat room".encode("utf-8"))
    while True:
        try:
            message = conn.recv(1024).decode("utf-8")
            if not message:
                remove(conn)
                remove_nickname(nickname)

                break
            print(f"[{nickname}] : {message}")
            message_to_send = "<"+ addr[0] + ">" + message
            broadcast(message, conn)
        except:
            continue

#python --version
print("server is running")
while True:
    conn, addr = server.accept()
    conn.send("NICKNAME".encode("utf-8"))
    nickname = conn.recv(2048).decode("utf-8")
    clients.append(conn)
    nicknames.append(nickname)
    message = f"{nickname} joined"
    print(message)
    broadcast(message, conn)
    print(f"Connected with {nickname}") 
#threading = all client requests run in parallel
    new_thread = Thread(target=client_thread, args=(conn, nickname))
    new_thread.start()

print("server is running")