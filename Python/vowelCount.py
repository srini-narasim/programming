#Count how many vowels there are in a word.

vowels = 'aeiou'

input_string = raw_input("Enter a string:")

#create a dictionary with each vowel as a key, with each value as zero
count = {}.fromkeys(vowels, 0)

for char in input_string:
  if char in count:
    count[char] += 1

print count
