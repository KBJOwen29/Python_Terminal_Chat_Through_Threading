from socket import *
from threading import Thread

#Bognalbal, Jim Owen
#Oribiana, Kerby

#Creates the socket object
Client = socket(AF_INET, SOCK_STREAM)
#Connects us to the server
Client.connect(("10.56.28.58", 12345))
print("Connected to the Server: ")

#This lets us to receive data to the client        
def receive_messages():
    while True: 
        data = Client.recv(1024)
        if not data:
            break
        print("Server: ",data.decode())
        
#This lets us to send data to the send                    
def send_messages():
    while(True):
        message = input()
        Client.send(message.encode())

#Uses a separate thread for both function without interfering with the main system                
Thread(target = receive_messages).start()
Thread(target=send_messages).start()
