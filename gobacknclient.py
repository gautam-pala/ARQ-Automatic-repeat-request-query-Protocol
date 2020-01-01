import socket
import time
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('',1234))
c.settimeout(5)
count=0
w=raw_input("enter window size")
c.send(w)
k=int(w)
p=0
while True:
	print(p,"p")
	for i in range(p,k):
		D=raw_input("enter data message")
		i=raw_input("enter sequence number")
	
		s1=D+","+i
		c.send(s1)
		print(s1)
	try:		
		for j in range(p,k):
			ans=c.recv(2)
			print(ans,"recv")
		if(int(ans)==(int(w)-1)):
			break
		else:
			p=int(ans)+1
			print("No ack for packet",p)
			raise socket.timeout
	except socket.timeout:
		print("time out")
		continue	
c.close()
'''
output>>
enter window size4
(0, 'p')
enter data messagedata
enter sequence number0
data,0
enter data messagedata1
enter sequence number1
data1,1
enter data messagedata
enter sequence number2
data,2
enter data messagedata
enter sequence number3
data,3
('00', 'recv')
('01', 'recv')
('02', 'recv')
('03', 'recv')
output2>>
enter window size4
(0, 'p')
enter data message1
enter sequence number1
1,1
enter data message1
enter sequence number2
1,2
enter data message1
enter sequence number3
1,3
enter data message1
enter sequence number1
1,1
('-1', 'recv')
('-1', 'recv')
('-1', 'recv')
('-1', 'recv')
('No ack for packet', 0)
time out
(0, 'p')
enter data message1   
enter sequence number0
1,0
enter data message1
enter sequence number2
1,2
enter data message1
enter sequence number1
1,1
enter data message1
enter sequence number2
1,2
('00', 'recv')
('00', 'recv')
('01', 'recv')
('02', 'recv')
('No ack for packet', 3)
time out
(3, 'p')
enter data messagedata
enter sequence number3
data,3
('03', 'recv')
'''
