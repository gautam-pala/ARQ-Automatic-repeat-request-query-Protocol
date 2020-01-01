# ARQ-Automatic-repeat-request-query-Protocol
Automatic repeat request (ARQ), also known as automatic repeat query, is an error-control method for data transmission that uses acknowledgements (messages sent by the receiver indicating that it has correctly received a packet) and timeouts (specified periods of time allowed to elapse before an acknowledgment is to be received) to achieve reliable data transmission over an unreliable service. If the sender does not receive an acknowledgment before the timeout, it usually re-transmits the packet until the sender receives an acknowledgment or exceeds a predefined number of retransmissions.  The types of ARQ protocols include Stop-and-wait ARQ, Go-Back-N ARQ, and Selective Repeat ARQ/Selective Reject ARQ. All three protocols usually use some form of sliding window protocol to tell the transmitter to determine which (if any) packets need to be retransmitted. These protocols reside in the data link or transport layers (layers 2 and 4) of the OSI model.

The repository contain

1) Stop and Wait Client and Server python code files

2) Go back N  Client and Server python code files

3) Selective Repeat Client and Server python code files

Implementation of Stop and Wait, Go Back n, and Selective Repeat

Client Program acts as a Sender
Server Program acts as a Receiver
The messages being communicated are of the form <D, i> i.e. data message with sequence number i; and <A,i> i.e acknowledgement message with sequence number i
Assume that packets are never corrupted (no checksum required) or delayed (no timer required)
The client program will take <D, i> as input from the user and send it to the server
The server will automatically respond as per the protocol with acknowledgement
Things to check:
What if client sends data messages out of sequence, validate the response from the server based on the protocol being used
