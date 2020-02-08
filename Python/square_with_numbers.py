#Print a square that will contain input that fills the dimensions of the square
#Ex. For 2x2 square, * * 
#					 * *  
#Ex. for 3x3 square, * * * 
#					 * * *
#					 * * *

response = int(raw_input("What is the size of the square? "))
for i in range(response):
	print("*" * response)