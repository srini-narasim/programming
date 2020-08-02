#Implementing the Mastermind game

#Using the cgi module to access passed information

import cgi
import random

print 'Content-type: text/html'
print ''

form = cgi.FieldStorage()

#Red pins mean that you have a colored ball located
#in the correct position
#White pins mean that you have a correct colored ball,
#but it is located in the wrong position.

reds = 0
whites = 0



if "answer" in form:
    answer = form.getvalue("answer")
else:
    answer = ""
    for i in range(4):
        answer += str(random.randint(0,9))

if "guess" in form:
    guess = form.getvalue("guess")
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                break

else:
    guess = ""

if "numberOfGuesses" in form:
    numberOfGuesses = int(form.getvalue("numberOfGuesses")) + 1
else:
    numberOfGuesses = 0

if numberOfGuesses == 0:
    message = "I have chosen a 4 digit number. Can you guess it?"
elif reds == 4:
    message = "Well done! You got it in " + str(numberOfGuesses) + " guesses. <a href=''>Play Again!</a>"
else:
    message = "You have " + str(reds) + " correct digit(s) in the right place, and "
    + str(whites) + " correct digits in the wrong place. You have had " + str(numberOfGuesses) + " guess(es)."


print answer

print '<h1>Mastermind</h1>'
print "<p>" + message + "</p>"
print '<form method="post">'
print '<input type="text" name="guess" value=" ' + guess + '">'
print '<input type="hidden" name="answer" value=" ' + answer + '">'
print '<input type="hidden" name="numberOfGuesses" value="' + str(numberOfGuesses) + '">'
print '<input type="submit" value="Guess!">'
print '</form>'
