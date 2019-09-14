def find_min(a,b):
    '''Takes two numbers as arguments and returns the minimum of the two'''
    if a < b:
        return a
    else:
        return b

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
minimum = find_min(first,second)
print("Minimum: ", minimum)