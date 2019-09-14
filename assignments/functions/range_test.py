def range_test(n):
    '''Returns True if the given number is within the range 1 to 555 (not inclusive)'''
    if n in range(2,555):
        print("{} is in range.".format(str(n)))
    else :
        print("{} is outside the range!".format(str(n)))

num = int(input("Enter a number: "))
range_test(num)