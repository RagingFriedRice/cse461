import sys
import socket
import numpy

#np.uint32()

std_id = 412

def construct_header(payload_len, psecret, step, last_digit):
	return str(payload_len) + str(psecret) + str(step) + str(last_digit)

def construct_packet(header, payload, payload_len):
	return str(header) + str(payload)

def packer(payload):
	pad = 4 - (sys.getsizeof(payload) % 4)
	return "\0" * pad + payload

HOST = 'attu2.cs.washington.edu'
PORT = 12235

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

#stage a
print ('stage a1')
payload = packer('hello world')
print ('the payload is: ', payload)
	
header = construct_header(str(sys.getsizeof(payload)),
						  numpy.uint32(0),
						  numpy.uint16(1),
						  numpy.uint16(std_id))
packet = construct_packet(header, payload, str(sys.getsizeof(payload)))

print ('finished packing')
print (packet.encode())
s.sendall(packet.encode())
data = s.recv(1024)
s.close()

#stage b
#print 'stage b1'
#stage c
#print 'stage c1'
#stage d
#print 'stage d1'