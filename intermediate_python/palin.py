import scrabble


longest = ""
for word in scrabble.wordlist:	
	if list(word) == list(revesed(word)) and len(word) > len(longest):
		longest = word

print(word)



