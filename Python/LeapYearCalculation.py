#Check leap year

#A leap year is exactly divisible by 4 except for
#century years(years ending with 00). The century
#year is a leap year only if it is perfectly
#divisible by 400.

year = int(raw_input("Enter a year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print (" {} is a leap year".format(year))
    else:
      print (" {} is not a leap year".format(year))
  else:
    print (" {} is not a leap year".format(year))
else:
  print (" {} is not a leap year".format(year))
