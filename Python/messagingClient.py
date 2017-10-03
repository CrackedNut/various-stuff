import socket

class Client:

	def __init__(self, host, port):
		self.host = host
		self.port = port

	def connection(self):
		s = socket.socket()
		s.connect((self.host, self.port))

	def sendRecv(self, message):
		self.message = message
		s.send(self.message.encode())
		data = s.recv(1024).decode()
		print("Received from server: " + str(data))

def Main():
	#set hostname and port to connect to
	host = "127.0.0.1"
	port = 5000

	#open connection to server
	sockt = Client(host, port)
 	sockt.connection()
 	
 	message = str(input("\n-> "))
 	
 	while message != "q":
  	
  		sockt.sendRecv(message)
  	
  		message = input("\n-> ")
 	
 	sockt.s.close()