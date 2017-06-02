import scrabble
import string


# print all letters that never appear doubled.

#for word in scrabble.wordlist:
#	if "uu" in word:
#		print(word)

for letter in string.ascii_lowercase:
	exists = False
	for word in scrabble.wordlist:
		if letter * 2 in word:
			exists = True
			break
	if not exists:
		print("There are no English words with a double " + letter)

			
