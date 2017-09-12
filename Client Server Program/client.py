#!/usr/bin/env python 
import socket

HOST='localhost'
PORT=9114

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect((HOST,PORT))
while 1:
    s = ""
    a = str(raw_input("input operator or 0 to close"))
    if(a=='0'): break 
    print "enter numbers"
    b = str(raw_input())
    c = str(raw_input())
    xx = a+'#'+b+'#'+c+'#'
    ss.send(xx)
    answer = ss.recv(12)
    print 'answer is ', int(answer)
ss.close()
    

