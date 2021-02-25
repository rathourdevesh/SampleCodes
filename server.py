import socket

port = 9999       
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print ("Socket successfully created")
s.bind(('', port))
print ("socket binded to %s" %(port)) 

s.listen(5)   
print ("socket is listening")  
while True:  
	c, addr = s.accept()      
	print ('Got connection from', addr )
	t=c.recv(1024)
	print("Data Received",t)
	#t="GET / HTTP/1.1\\r\\nHost: example.com\\r\\nAccept: text-html"
	#c.sendall(t.encode('utf-8'))
	#print(t)
	d="hello"
	c.sendall(d.encode('utf-8'))
	c.close()


# baddr = '3C:A0:67:FE:2C:A0'
# channel = 4
# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
# s.connect((baddr,channel))
# while True:
# 	s_sock = s.accept()
# 	print ("Accepted connection from "+ address)

# 	data = s_sock.recv(1024)
# 	print ("received [%s]" % data)

# 	s.listen(1)