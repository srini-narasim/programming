#Modify the program so that the number of years of the investment is also a user input. 

def num_years_of_investment():
	num_years = input("Enter the number of years as an investment: ")
	principal = input("Enter the initial principal: ")
	apr = input("Enter the annual interest rate: ")

	for i in range(num_years):
		principal = principal * (1 + apr)

	print "The value in", num_years, "years is:", principal

num_years_of_investment()