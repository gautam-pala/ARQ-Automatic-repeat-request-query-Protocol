import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('',12345))
c.settimeout(0.5)
a1=raw_input("enter number of data message")
c.send(a1)
count=0
while True:
	if(count<int(a1)):
		D=raw_input("enter data message")
		i=raw_input("enter sequence number")
		s1=D+","+i
		c.send(s1)
		print(s1)
		try:
			ans=c.recv(10)
			if(int(ans)==int(i)):
					pass
		except socket.timeout:
			print("time out")
			continue	
		count+=1
	else:
		break
c.close()
'''
output
enter number of data message4
enter data messagedata1
enter sequence number0
data1,0
enter data messagedata2
enter sequence number1
data2,1
enter data messagedata3
enter sequence number0
data3,0
enter data messagedata4
enter sequence number1
data4,1
output2>>
enter number of data message4
enter data messagedata1
enter sequence number0
data1,0
enter data messagedata
enter sequence number2
data,2
time out
enter data messagedata2
enter sequence number1
data2,1
enter data messagedata
enter sequence number3
data,3
time out
enter data messagedata3
enter sequence number0
data3,0
enter data messagedata4
enter sequence number1
data4,1
'''
