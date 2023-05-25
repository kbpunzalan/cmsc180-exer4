#!/usr/bin/python

import socket
import threading

def on_new_client(clientsocket, addr):
    global clients
    clients.append(clientsocket)
    print('New client connected:', addr)
    
    if len(clients) == n:
        for c in clients:
            c.send('Server reached maximum capacity. Cannot accept new clients.'.encode())
        return
    
    while True:
        try:
            msg = clientsocket.recv(1024)
        except:
            break
        if not msg:
            break
        print(addr, '>>', msg.decode())
        for c in clients:
            if c != clientsocket:
                c.send(msg)
    
    clients.remove(clientsocket)
    print('Client disconnected:', addr)
    clientsocket.close()

host = socket.gethostname()
port = 50000
n = 5
clients = []

s = socket.socket()
s.bind((host, port))
s.listen()

print('Server started!')
print('Waiting for clients...')

while True:
    c, addr = s.accept()
    thread = threading.Thread(target=on_new_client, args=(c, addr))
    thread.start()
