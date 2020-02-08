#Modify the program so that it computes and prints Celsius temperatures and the Fahrenheit equivalents
#every 10 degrees from 0 degrees to 100 degrees Celsius. 

def calculate_temperature_every_10_degrees():

	for i in range(0,100,10):
		
		fahrenheit = 9/5 * i + 32
		print "The celsius temperature is: ", i, "degrees."
		print "The temperature is", fahrenheit, "degrees Fahrenheit."

calculate_temperature_every_10_degrees()