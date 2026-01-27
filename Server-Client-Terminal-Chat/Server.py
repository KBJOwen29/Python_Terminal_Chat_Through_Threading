from socket import *
from threading import Thread

#Bognalbal, Jim Owen
#Oribiana, Kerby

#Creates a TCP socket
server = socket(AF_INET, SOCK_STREAM)
#Bind to the IP and port
server.bind(("0.0.0.0", 12345))
#Starts listening with a  backlog of 1
server.listen(1)

print("Server waiting for Connection....")
#Accepts a new connection
conn, address = server.accept()
print("Connected to: ",address)

#This lets us to receive data from the client
def receive():
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Client: ",data.decode())
    
#This lets us to send data to the client        
def send():
    while True:
        msg = input()
        conn.send(msg.encode())
#Uses a separate thread for both function without interfering with the main system        
Thread(target=receive).start()
Thread(target=send).start()