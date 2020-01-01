import socket
import thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen(5)
def s1(a,c):
	l=[]
	w=c.recv(10)
	w=int(w)
	print("window size:",w)
	k=0
	for i in range(0,w):
		k=w-1
		while True:
			ans=c.recv(2048)
			print("data message and sequence number",ans)
			a1,a2=ans.split(",")
			a2=int(a2)
			if(a2<=k):
				if a2 not in l:
					l.append(a2)
				else:
					continue
				c.send(str(a2))
				print(str(a2),"send1")
				break
				
	l.sort()
	print(l)
			
while True:
	conn,addr=s.accept()
	t1=thread.start_new_thread(s1,(0,conn))
