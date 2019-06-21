#!/usr/bin/python
import socket
import sys
s=socket.socket()
s.bind(("0.0.0.0",int(sys.argv[1])))
s.listen(5)
q,c = s.accept()
z = ""
try:
	while True:
		k = s.recv(1024)
		z += k
		if k == "":
			raise ValueError
except:
	print(z)