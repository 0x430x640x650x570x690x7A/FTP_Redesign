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
    try:
        message = input("Enter Command: ")
        if message == 'exit':
            break
        
        outputData = message.split(' ')
        print(outputData)
        
        if outputData[0] == 'send' or outputData[0] == 'copy' or outputData[0] == 'rename' or outputData[0] == 'delete':
                
            for i in range(0, len(outputData)):                         
                serverSocket.send((outputData[i] + ' ').encode()) 
            #serverSocket.close()
            #serverSocket.sendall(b"Test") #
            #serverSocket.sendall(outputData[0].encode())
            print("Command Sent")
            data = serverSocket.recv(1024)
            print('Received', repr(data))
            
            #if outputData[0] == 'send' :
             #   serverSocket.sendall(file)
        else:
            print("600 Invalid Option")
            
    except:
        print("601 Error")
        
serverSocket.close()
        
"""
client error codes

600 Invalid Option
601 Client Side General Error

"""
