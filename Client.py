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
print("send fileDirectory ")
print("copy nameOfFile newFileName ")
print("rename nameOfFile newFileName ")
print("delete nameOfFile ")

while True:
    message = ""
    try:
        message = input("Enter Command: ")
        if message == 'exit':
            break
        
        if 'send' in message or 'copy' in message or 'rename' in message  or 'delete' in message :
            #print(message)
            serverSocket.sendall(message.encode())
            print("Command sent to server")
            if 'send' in message:
                print("Received directory list: ")
                data = serverSocket.recv(1024)
                tempString = data.decode()
                print(tempString)

        else:
            print("600 Invalid Option")
            
    except:
        print("601 Error")
        #serverSocket.close()
        
serverSocket.close()
        
"""
client error codes


600 Invalid Option
601 Client Side General Error

"""
