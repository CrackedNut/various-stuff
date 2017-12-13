class MyClass:
	friendsLi = []
	ages = []

	def add(self, name, age):
		self.friendsLi.append(name + "-> " + str(age))

def Main():

	friends = MyClass()

	friends.add("Amy", 23)
	friends.add("Eddy", 21)
	print(friends.friendsLi)
	friends.add("Ivy", 32)
	friends.add("Owen", 27)
	print(friends.friendsLi)


if __name__ == "__main__":
	Main() 