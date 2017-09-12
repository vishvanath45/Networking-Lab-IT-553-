# !usr/env/bin/ python
import socket
import os

HOST ='localhost'
PORT = 8059

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.bind((HOST,PORT))
ss.listen(100)
print ss
print ' < === server is ready === > '
while (1):
	conn, addr = ss.accept()
	print "connected to ",addr , conn

	with open('./to_receive.jpg','wb') as f:
		print 'file open successfull'
		while(1):
			print ('downloading ....')
			data = conn.recv(512)
			if(data =='sleep'):
				print ("i am going to sleep ")
				ss.close()
			print ('segment recv ')
			print data
			if not data:
				break
			f.write(data)
	f.close()
	print('download complete')
ss.close()
