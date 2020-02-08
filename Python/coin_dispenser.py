#Write a program that will be used in a stamp dispenser. 

#This dispenser only gives out 74, 32 and 6 cent stamps.
#It takes only dollar bills.
#It gives change only in coins and does not use half dollars or anything larger than dollar coins.

STAMP_74 = .74
STAMP_32 = .32
STAMP_6 = .06
DOLLAR_CENTS = 100
QUARTER_CENTS = 25
NICKEL_CENTS = 5
PENNY_CENTS = 1




def show_welcome_screen():
	print " --------------------------------------------"
	print "|     Welcome to the snakeStamp Machine!     |"
	print "| We dispense only 74, 32 and 6 cent stamps. |"
	print "| We give only coins in change - (no bills). |"
 	print " -------------------------------------------- "

def get_name_calculate_change():
	first_raw_input = raw_input("What is your first name? ")
	last_raw_input = raw_input("What is your last name? ")


	num_74_cent_stamps = int(raw_input("How many 74 cent stamps would you like? "))
	num_32_cent_stamps = int(raw_input("How many 32 cent stamps would you like? "))
	num_6_cent_stamps = int(raw_input("How many 6 cent stamps would you like? "))

	total_cost = (num_74_cent_stamps * STAMP_74) + (num_32_cent_stamps * STAMP_32) + (num_6_cent_stamps * STAMP_6)
	total_stamps = num_74_cent_stamps + num_32_cent_stamps + num_6_cent_stamps

	print
	print "The price of your", str(total_stamps) + " stamps is $" + str(round(float(str(total_cost)), 2))
	print
	num_dollars = raw_input("How many dollars wil you be giving us? ")
	print 
	print "Thank you. Just a moment please. "

	change = float(num_dollars) - float(total_cost)

	formatted_change = round(change, 2)

	cents = formatted_change * DOLLAR_CENTS

	dollars = int(cents / DOLLAR_CENTS)

	remaining_cents = cents % DOLLAR_CENTS

	quarters = int(remaining_cents / QUARTER_CENTS)

	another_remaining_cents = remaining_cents - (quarters * QUARTER_CENTS)

	nickels = int(another_remaining_cents / NICKEL_CENTS) 

	after_nickels_remaining_cents = another_remaining_cents - (nickels * NICKEL_CENTS)

	pennies = int(after_nickels_remaining_cents / PENNY_CENTS)
	
	print
	print "Thanks " + first_raw_input + " " + last_raw_input, "your change is:"
	print dollars, "dollar coin(s)"
	print quarters, "quarter(s)"
	print nickels, "nickels"
	print pennies, "penny(ies)"





show_welcome_screen()
get_name_calculate_change()
