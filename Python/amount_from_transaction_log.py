#Write a program that computes the net amount of a bank account based on a transaction log from console input. 
#The transaction log format is shown as following:

#D 100
#W 200
#D means deposit
#W means withdrawal

#Suppose the following input is supplied to the program:
#D 300
#D 300
#W 200
#D 100
#Then, the output should be: 
#500d

netAmount = 0
while True: 
	log = raw_input()
	if not log:
		break
	values = log.split(" ")
	operation = values[0]
	amount = int(values[1])
	if operation == 'D':
		netAmount += amount
	if operation == 'W':
		netAmount -= amount

print "Total amount is: ", netAmount