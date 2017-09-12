#!/usr/bin/env python
import socket
import os

HOST ='localhost'
PORT = 8059

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect((HOST,PORT))

while(1):
	fileadd='./to_send.jpg'
	size = os.path.getsize(fileadd)
	f = open(fileadd,'rb')
	counter=1
	data_batch = f.read(1024)
	while(data_batch):
		ss.send(data_batch)
		print('part sending ')
		data_batch = f.read(1024)
		counter=counter+1024
		print "counter size ", counter,size
		if(counter >= size):
			break
	f.close()
	print("complete file sent !!!")
	break
ss.send("sleep")
ss.close()



