#ATM Pin Code Validation

#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
#anything but exactly 4 digits or exactly 6 digits. Your task is to create a
#function that takes a string and returns True if the PIN is valid and False if
#not.

def is_valid_PIN(s):
  return ((len(s) == 4 or len(s) == 6)) and s.isdigit()

print is_valid_PIN("1234") #True
print is_valid_PIN("12345") #False
print is_valid_PIN("123456") #True
print is_valid_PIN("a2345") #False
