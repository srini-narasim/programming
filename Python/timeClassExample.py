#Create a Time class and initialize it with hours and minutes.
#1) Make a method addTime which should take two objects and add them.
#   (2 hours and 50 min) + (1 hour and 20 min) = (4 hrs and 10 min)
#2) Make a method displayTime which should print the time.
#3) Make a method displayMinute which should display the total minutes
#   in the time (1 hr and 2 min) = (62 minutes)

class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        t3 = Time(0,0)
        if t1.minutes + t2.minutes > 60:
            t3.hours = (t1.minutes + t2.minutes) / 60
        t3.hours = t1.hours + t2.hours + t3.hours
        t3.minutes = (t1.minutes+t2.minutes)-(((t1.minutes+t2.minutes)/60)*60)
        return t3
    def displayTime(self):
        print "Time is:", self.hours, "hours and ", self.minutes, "minutes"
    def displayMinutes(self):
        print (self.hours * 60) + self.minutes


a = Time(2,40)
b = Time(3,30)
c = Time.addTime(a,b)

print c.hours
print c.minutes
