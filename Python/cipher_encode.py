#Write a program that can encode Caesar ciphers. 

def encode():
	key_value = raw_input("What is your key value: ")
	word_to_encode = raw_input("What is the word you would like to encode: ")

	all_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
					"R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	#find index of letter in word
	#add the key_value to the 
	#get the letter of the new index

	new_word = " "

	for i in word_to_encode:
		current_index = all_letters.index(i)
		print current_index
		new_index = current_index + int(key_value)
		new_word += all_letters[new_index]
	print new_word

encode()



