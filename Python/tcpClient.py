import socket

def Main():
	host = "192.168.1.130"
	port = 5000

	s = socket.socket()
	s.connect((host, port))

	message = raw_input("-> ")

	while message != "q":
		s.send(message.encode())
		data = s.recv(1024).decode()
		print("Received from server: " + str(data))
		message = input("-> ")

	s.close()

if __name__ == "__main__":
	Main()