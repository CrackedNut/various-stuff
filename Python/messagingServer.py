import socket

class Server:

	def __init__(self, host, port):
		self.host = str(host)
		self.port = port

	def connection(self):
		s = socket.socket()
		s.bind((self.host, self.port))

		print("Listening for a connection...")
		s.listen(1)
		self.c, addr = s.accept()
		print("Connection from: " + str(addr))

	def recive(self):
		self.data = self.c.recv(1024).decode()



	def sends(self, message):
		self.message = message
		self.c.send(self.message.encode())





def Main():
	host = "127.0.0.1"
	port = 5000
	socktSer = Server(host, port)
	socktSer.connection()

	message = "."

	while message != "q":
		socktSer.recive()
		if socktSer.data == "q":
			break

		print("\n<- " + str(socktSer.data))

		message = str(input("-> "))
		socktSer.sends(message)
	socktSer.c.close()
