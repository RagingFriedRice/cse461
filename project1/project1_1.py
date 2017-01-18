import sys
import socket
import numpy as py

#np.uint32()

std_id = 412

def construct_header(payload_len, psecret, step, last_digit):
	header = []

	for x in range (0, 2):
		header.append(last_digit % 255)
		last_digit = last_digit // 255

	for x in range (0, 2):
		header.append(step // 255)
		step = step % 255

	for x in range (0, 4):
		header.append(psecret % 255)
		psecret = psecret // 255

	for x in range (0, 4):
		header.append(payload_len % 255)
		payload_len = payload_len // 255

	return header[::-1]

def construct_packet(header, payload):
	return bytes(header) + payload.encode()

def packer(payload):
	pad = 4 - (len(payload) % 4)
	return payload.zfill(pad + len(payload))

HOST = 'attu2.cs.washington.edu'
PORT = 12235

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

print('aligning payload......')
payload = packer('hello world\0')
print('payload aligning done, constructing the header......')
header = construct_header(len(payload), 0, 1, std_id)
print('header construction done, preparing the packet......')
packet = construct_packet(header, payload)
print('packet ready\n')
print(packet)

s.sendall(packet)
print ('packet sent')
data = s.recv(1024)
print ('packet received')
s.close()

#stage a
# print ('stage a1')
# payload = packer('hello world')
# print ('the payload is: ', payload)
	
# header = construct_header(str(sys.getsizeof(payload)),
# 						  numpy.uint32(0),
# 						  numpy.uint16(1),
# 						  numpy.uint16(std_id))
# packet = construct_packet(header, payload, str(sys.getsizeof(payload)))

# print ('finished packing')
# print (packet.encode())
# s.sendall(packet.encode())
# print ('packet sent')
# data = s.recv(1024)
# print ('packet received')
# s.close()

#stage b
#print 'stage b1'
#stage c
#print 'stage c1'
#stage d
#print 'stage d1'