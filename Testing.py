# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:17:25 2020

@author: evans
"""

    
message = 'delete: myFileName: myLocation: newFIleName'

newMessage = message.split(': ')

print(newMessage)
print(newMessage[0])
print(newMessage[1])
print(newMessage[2])
print(newMessage[3])


def send():
    print('send') 
def copy():
    print('copy')
def rename():
    print('rename')
def delete():
    print('delete')

mySwitch = {'send' : send,
           'copy' : copy,
           'rename' : rename,
           'delete' : delete,
}

mySwitch[newMessage[0]]()


"""
switch(newMessage[0])
    case copy
    call copy function
"""