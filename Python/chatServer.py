import socket
import time

host = "127.0.0.1"
port = 2222

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print("Server started...")

while not quitting:
	try:
		data, addr = s.recvfrom(1024)
		if("Quit") in str(data.decode()):
			quitting = True
		if addr not in clients:
			clients.append(addr)

		print(time.ctime(time.time()) + str(addr) + ": :" + str(data.decode()))

		for client in clients:
			s.sendto(data.encode(), client)

	except:
		pass

s.close()
