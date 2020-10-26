# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:17:25 2020

@author: evans
"""

"""
    message formats
send myFileName myPath $ $
copy myFileName myPath newPath $
rename myFileName myPath newFileName $
delete myFileName myPath $ $
"""

#import os
message = 'send myFileName myPath $ $'

newMessage = message.split(' ')

print(newMessage) 
print(newMessage[0], end = ' ')
print(newMessage[1], end = ' ')
print(newMessage[2], end = ' ')
print(newMessage[3], end = ' ')
print(newMessage[4])

def send():
    #print('%s send' %newMessage[4]) 
    print('send') 
def copy():
    print('copy')
def rename():
    print('rename')
def delete():
    #os.remove(path) 
    #print("% s removed successfully" % path)
    print('delete')

mySwitch = {'send' : send,
           'copy' : copy,
           'rename' : rename,
           'delete' : delete,
}


mySwitch[newMessage[0]]()


"""
IOError: 501 
OSError: 123
SendError: 345
switch(newMessage[0])
    case copy
    call copy function
    
    
    connect to server
    send my message
    find the location -> windows file manager
    location = \home\folder -> search for location and then full file
    
    
"""
