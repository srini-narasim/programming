#Finding factors of a number

def print_factors(x):
    list_of_factors = []
    for i in range(1,x+1):
        if x % i == 0:
            list_of_factors.append(i)
    print list_of_factors

print_factors(6)
