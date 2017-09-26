class Pet:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method")

class Cat(Pet):

	def __init__(self, name, age):
		super().__init__(name, age) #you can run super class methords 

	def talk(self):
		return "Meowww"

class Dog(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)

	def talk(self):
		return "Wooff"

def Main():

	pets = [Cat("Jess", 3), Dog("Jack", 2), Cat("Fred", 7), Pet("thePet", 5)]

	for pet in pets:
		print("Name: " + pet.name + ", Age: " + str(pet.age) + ", Says: " + pet.talk())

if __name__ == "__main__":
	Main()