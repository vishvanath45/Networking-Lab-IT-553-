#!/usr/bin/env python 
import socket

HOST='localhost'
PORT=9114
ss= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(100)
print ss
print '=== server is ready ==='
while (1):
	conn, addr = ss.accept()
	print '== connected to ', addr, conn
	arr2 = conn.recv(20)
	arr3 = arr2.split("#")
	operator = arr3[0]
	if not operator: break
	no1 = int(arr3[1])
	no2 = int(arr3[2])
	if(operator=='+'):
		ans = no1+no2
		ans = str(ans)
		conn.send(ans)
	elif(operator=='-'):
		ans = no1-no2
		print ans
		ans = str(ans)
		conn.send(ans)
	elif(operator=='*'):
		ans = no1*no2
		ans = str(ans)
		conn.send(ans)
	else:
		ans = float(no1)/float(no2)
		ans = str(ans)
		conn.send(ans)
	conn.close()
ss.close()

