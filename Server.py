# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:16:41 2020

@author: evans

operation nameOfFile newFileName
"""

from socket import *
import os
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverIp = "10.0.0.1"
serverPort = 80
serverSocket.bind((serverIp,serverPort))
serverSocket.listen(1)
print('Server up on port', serverPort)
connectionSocket, addr = serverSocket.accept()     
print('Connected by', addr)
myPath = ""

def send():
    #print('host side send') 
    path = "/home/mininet/mininet/"
    print("File directory list for " + path + inputData[1])
    directoryList = os.listdir(path + inputData[1]);
    print(directoryList)
    temp = ''
    for i in range(0, len(directoryList)):
        temp += (directoryList[i] + "\n")                         
    connectionSocket.sendall(temp.encode()) 
    
def copy():
    #print('host side copy')
    print("Copied " + inputData[1] + " as " + inputData[2])
    oldPath = myPath + inputData[1]
    newPath = myPath + inputData[2] 
    os.popen("cp " + oldPath + " " + newPath)
    
def rename():
    #print('host side rename')
    print("Renamed " + inputData[1] + " to " + inputData[2]) 
    oldPath = myPath + inputData[1]
    newPath = myPath + inputData[2] 
    #print(oldPath)  
    #print(newPath)
    os.rename(oldPath, newPath)
    
def delete():
    #print('host side delete')
    print("Deleted " + inputData[1])
    oldPath = myPath + inputData[1]
    #print(oldPath)  
    #print(newPath)
    os.remove(oldPath)

while True: 
    message = "" 
    myPath = "/home/mininet/mininet/custom/serverFolder/"
    try:         
        message = connectionSocket.recv(1024)
        #print(message)
        tempString = message.decode()
        inputData = tempString.split(' ')
        #print(inputData)
        #print(inputData[0])

        if inputData[0] == 'send' :
             send()
        elif inputData[0] == 'copy' :
             copy()
        elif inputData[0] == 'rename' :
             rename()
        elif inputData[0] == 'delete':
             delete()
        elif inputData[0] == 'exit':
            print("Exiting")
        else:
             print("700 Error")

        if not message:
            serverSocket.close()
            break
        #connectionSocket.sendall(message)
        
    except IOError:
        print("701 Error")
        print("Verify input")
        #serverSocket.close()        
    except FileNotFoundError:
        print("702 Error")
        print("Verify input")
        #serverSocket.close()        
    except OSError:
        print("703 Error")
        print("Closing connection")
        break
    except:
        print("704 Error")
        print("Closing connection")
        break
    
print("Connection closed")
serverSocket.close()
        
 
"""
server error codes

700 invalid option
701 IOError
702 FileNotFoundError
703 OSError
704 general error

"""

"""
import socket

HOST = '10.0.0.1'  # Standard loopback interface address (localhost)
PORT = 80        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(True)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            """
