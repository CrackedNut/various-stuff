class Hangman:

	def __init__(self, tries, word):
		self.word = word
		self.tries = tries
		self.lenght = len(self.word)

	def gameLoop(self):

		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


		while self.tries != 0:

			self.left = self.tries
			print("\nLives: [" + str(self.left) +  "]")

			self.guess = str(input("Guess a word: "))
			
			if self.guess == self.word:
				break

			else:
				for char in self.guess:

					print("\n\n\n\n YOU WON!")
					self.inWord = 0

					if char in self.word:
						self.inWord +=1

					print(char + " appears " + str(self.inWord) + " times.")

				self.











				tries -=1

		print("You lost! Correct answer: " + self.word)

def Main():
	game = Hangman(input("Lives: "), input("Word: "))
	game.gameLoop()

if __name__ =="__main__":
	Main()