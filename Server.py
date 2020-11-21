# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:16:41 2020

@author: evans
"""

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverIp = "10.0.0.1"
serverPort = 80
serverSocket.bind((serverIp,serverPort))
serverSocket.listen(1)
print('Server up on port', serverPort)
connectionSocket, addr = serverSocket.accept()     
print('Connected by', addr)

def send():
    print('host side send') 
    #open and close new socket
    
def copy():
    print('host side copy')
    
def rename():
    print('host side rename')
    
def delete():
    print('host side delete')


while True: 
    message = ""      
    try:         
        message = connectionSocket.recv(1024)
        print(message)
        tempString = message.decode()
        inputData = tempString.split(' ')
        print(inputData)
        print(inputData[0])

        if inputData[0] == 'send' :
             send()
        elif inputData[0] == 'copy' :
             copy()
        elif inputData[0] == 'rename' :
             rename()
        elif inputData[0] == 'delete':
             delete()
        else:
             print("700 Error")

        if not message:
            break
        connectionSocket.sendall(message)
        
    except IOError:
        print("701 Error")
        serverSocket.close()        
    except FileNotFoundError:
        print("702 Error")
        serverSocket.close()        
    except OSError:
        print("703 Error")
        break
        serverSocket.close()        
    except:
        print("704 Error")
        break
        serverSocket.close()

serverSocket.close()
        
 
"""
server error codes

501 valid server recieve

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
