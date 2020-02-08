
#Steps of Collatz's hypothesis:

#1) Take any non-negative and non-zero
#integer number and name it c0;
#2) If c0 is even, evaluate a new c0 as c0 / 2;
#3) Otherwise, if odd, evaluate a new c0 as 3 * c0 + 1;
#4) If c0 is not equal to 1, skip to point 2.

#Write a program which reads one natural number
#and executes the above steps as long as c0 remains
#different from 1. We also want to count the
#steps needed to achieve the goal.
#Your code should ouput all the intermediate
#values of c0, too. (includng 1)


c0 = int(input())

steps = 0
while (c0 != 1):
    print(c0)
    # If n is odd
    if c0 % 2 != 0:
        c0 = 3 * c0 + 1
    # If even
    else:
        c0 = c0 // 2
    steps += 1
print(c0)
print("steps =", steps)
