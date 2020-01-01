import socket
import thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen(5)
def s1(a,c):
	w=c.recv(10)
	w=int(w)
	print("window size:",w)
	k=0
	for i in range(0,w):
		k=k%w
		while True:
			ans=c.recv(2048)
			print("data message and sequence number",ans)
			a1,a2=ans.split(",")
			a2=int(a2)
			print("sequence number expected",k)
			print("sequence number got",a2)
			if(a2==k):
				c.send("0"+str(k))
				print("0"+str(k),"send1")
				k=k+1
				break
			else:
				z=k-1
				if(z<0):
					print("z",z)
					z=str(z)
					c.send(z)	
					print(k-1,"send2")
					
				else:
					print("z",z)
					z="0"+str(z)
					c.send(z)	
					print("0"+str(k-1),"send2")
				continue
while True:
	conn,addr=s.accept()
	t1=thread.start_new_thread(s1,(0,conn))
