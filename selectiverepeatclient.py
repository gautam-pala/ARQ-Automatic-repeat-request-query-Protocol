import socket
import time
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('',1234))
c.settimeout(5)
count=0
w=raw_input("enter window size")
c.send(w)
k=int(w)
l=[]
p=0
while True:
	print(p,"p")
	for i1 in range(p,k):
		D=raw_input("enter data message")
		i=raw_input("enter sequence number")
		if k==int(w):
			if i1 not in l:
				l.append(i1)
		s1=D+","+i
		c.send(s1)
		print(s1)
	try:		
		for j in range(p,k):
			ans=c.recv(1)
			ans1=int(ans)
			print(ans1,"ans1")
			print(l)
			if ans1 in l:
				print("true")
				l.remove(ans1)
			print(ans,"recv")
			
		if len(l)==0:
			break
		else:
			
			raise socket.timeout
	except socket.timeout:
		len1=len(l)
		k=len1
		print("please re-enter data and sequence number for given sequence number",l)
		print("time out")
		continue	
c.close()
'''
output>>
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
enter sequence number0
1,0
(1, 'ans1')
[0, 1, 2, 3]
true
('1', 'recv')
(2, 'ans1')
[0, 2, 3]
true
('2', 'recv')
(3, 'ans1')
[0, 3]
true
('3', 'recv')
(0, 'ans1')
[0]
true
('0', 'recv')
output2>>
enter window size4
(0, 'p')
enter data message1
enter sequence number5
1,5
enter data message1
enter sequence number1
1,1
enter data message1
enter sequence number2
1,2
enter data message1
enter sequence number3
1,3
(1, 'ans1')
[0, 1, 2, 3]
true
('1', 'recv')
(2, 'ans1')
[0, 2, 3]
true
('2', 'recv')
(3, 'ans1')
[0, 3]
true
('3', 'recv')
('please re-enter data and sequence number for given sequence number', [0])
time out
(0, 'p')
enter data message1
enter sequence number0
1,0
(0, 'ans1')
[0]
true
('0', 'recv')
'''
