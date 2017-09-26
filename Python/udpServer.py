#!/usr/bin/env python3

import socket

def Main():
	host = "127.0.0.1"
	port = 5555

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print("Server started\nListening for connection...")
	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode()
		print("\nMessage from: ", str(addr))
		print("From connected user: "+str(data))
		data = data.upper
		print("Sending: " + str(data))
		data = data.encode()
		s.sendto(data, addr)
	s.close()

if __name__ == "__main__":
	Main()