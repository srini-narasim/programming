#Modify the program with a loop so that it executes 5 times before quitting

def calculate_temperature_five_times():

	for i in range(0,5):
		celsius = input("What is the Celsius temperature? ")
		fahrenheit = 9/5 * celsius + 32
		print"The temperature is", fahrenheit, "degrees Fahrenheit."

calculate_temperature_five_times()

