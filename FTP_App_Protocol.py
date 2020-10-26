# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:25:39 2020

@author: evans
"""
from socket import *

# enum (COPY,)

#open control socket
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 1
serverSocket.bind(('',serverPort))
serverSocket.listen(True)
print('Server up on Port ', serverPort)
#running main socket read messages through control socket

def send():
    print('send') 
    
def copy():
    print('copy')
    
def rename():
    print('rename')
    
def delete():
    print('delete')
    
    
mySwitch = {'send' : send(),
       'copy' : copy,
       'rename' : rename,
       'delete' : delete,
}

while True:
    #global newMessage = ''
    #Establish the connection     
    print('Ready to serve...')    
    connectionSocket, addr = serverSocket.accept()  
    try:    
        #read messagetype
        controlMessage = connectionSocket.recv(1024)
        #messageType nameOfFile path newFileName
        #parsedControlMessage[0] parsedControlMessage[1] parsedControlMessage[2] parsedControlMessage[3]
        newMessage = controlMessage.split(' ')
        #print out the new message 
        print(newMessage) 
        print(newMessage[0], end = ' ')
        print(newMessage[1], end = ' ')
        print(newMessage[2], end = ' ')
        print(newMessage[3], end = ' ')
        print(newMessage[4])
        
        mySwitch[newMessage[0]]()

    except IOError as error:
        print(error) 
        print("IO error: 123") 
    except OSError as error: 
        print(error) 
        print('%s error: 501' %newMessage[0])  

    connectionSocket.close()

#close control socket


"""
pseudo code for switch logic
switch(parsedControlMessage[0])
    case send
        call send function
        mySendFunction(name, location)
        status code for successful send
        break
    case copy
        call copy function
        myCopyFunction(name, location)
        status code for successful copy
        break
    case RNME
        call rename function
        myRenameFunction(name, location, newName)
        status code for successful rename
        break
    case DLTE
        call delete function 
        myDeleteFunction(name, location)
        status code for successful delete
        break
    case default
        status code for invalid message type
        break
"""
