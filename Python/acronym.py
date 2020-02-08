#Write a program that would take the first letter of the words in a phrase and making a word from
#them. 

def create_acronym():
	acronym = " "
	phrase = raw_input("Enter your phrase that would be converted to an acronym: ")
	sp_phrase = phrase.split(" ")
	for i in sp_phrase:
		acronym += i[0]
	print acronym

create_acronym()
