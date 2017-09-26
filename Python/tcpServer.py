import socket

def Main():
	host = "192.168.1.130"
	port= 5000

	s = socket.socket()
	s.bind((host, port))

	print("Listening for a connection...")
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: " + str(addr)+"\n")

	while True:
		data = c.recv(1024).decode()
		if not data:
			break

		print("From connected user: " + str(data))

		data = str(data).upper()

		print("Sending: " + str(data))

		c.send(data.encode())

	c.close()

if __name__ == "__main__":
	Main()
