
word = "hippopotamus"
lenght = len(word)
print("\n\n" + ("_ " * lenght) + "  " + str(lenght) + " Letters")
tries = 5   
            
while tries != 0:
	left = "* "*tries
	print("\nLives: [" + str(left) +  "]")
	guessed = str(input("\nGuess a word: \n."))
	if guessed == word:
		print("\n\n\n\n YOU WON!")
		break
	else:   
		for char in guessed:
			inWord = 0
			if char in word:
				inWord +=1
			print("Letter: " + char + " appers " + str(inWord) + " times\n")
	tries -= 1



