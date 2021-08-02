
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',1234))

s.listen(3)

c,address = s.accept()
print("connection recieved from {} ".format(address))

#On kali linux machine

msg = input("Enter command :")
c.send(msg.encode())

while msg!='quit':
    msg = c.recv(2048).decode()
    print(msg)
    
    msg = input("Enter command :")
    c.send(msg.encode())

c.close()

s.close()
