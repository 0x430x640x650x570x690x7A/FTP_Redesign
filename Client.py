# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:53:56 2020

@author: evans

Socket example: https://realpython.com/python-sockets/
"""

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
#Fill in start
serverIP = '10.0.0.1' 
serverPort = 80
serverSocket.connect((serverIP,serverPort))
print('Connecting to ', serverPort)
message = ""
outputData = ""
file = "You have created a file"

print("\tCommand Options ")
print("send copy rename delete")
print("\tCommand Rules")
print("send nameOfFile path ")
print("copy nameOfFile path newFileName ")
print("rename nameOfFile path newFileName ")
print("delete nameOfFile path ")

while True:
    message = ""
    try:
        message = input("Enter Command: ")
        if message == 'exit':
            break
        
        if 'send' in message or 'copy' in message or 'rename' in message  or 'delete' in message :
            print(message)
            serverSocket.sendall(message.encode())
            
            print("Command Sent")
            #data = serverSocket.recv(1024)
            #print('Received', repr(data))
        else:
            print("600 Invalid Option")
            
    except:
        print("601 Error")
        serverSocket.close()
        
serverSocket.close()
        
"""
client error codes

500 Valid client send

600 Invalid Option
601 Client Side General Error

"""
