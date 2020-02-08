#Finding the average of 3 numbers

def find_average_of_three_numbers():
	
	print("This program calculates the average of three exam scores.")
	score1 = input("Enter the first score: ")
	score2 = input("Enter the second score: ")
	score3 = input("Enter the third score: ")
	average = (score1 + score2 + score3) / 3
	print "The average of three scores is:", average

find_average_of_three_numbers()
