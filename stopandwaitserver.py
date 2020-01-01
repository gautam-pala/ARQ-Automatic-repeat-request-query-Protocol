import socket
import thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',12345))
s.listen(5)
def s1(a,c):
	l=c.recv(10)
	l=int(l)
	k=1
	for i in range(0,l):
		k=k-(-1)
		k=k%2
		while True:
			ans=c.recv(2048)
			print(ans)
			a1,a2=ans.split(",")
			a2=int(a2)
			if(a2==k):
				c.send(str(k))
				break
			else:
				continue
while True:
	conn,addr=s.accept()
	t1=thread.start_new_thread(s1,(0,conn))
