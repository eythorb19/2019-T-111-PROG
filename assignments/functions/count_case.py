def count_case(s):
    '''Returns the count of upper case and lower case characters in the given string''' 
    upper_count, lower_count = 0,0
    for ch in s:
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1
    return upper_count, lower_count

user_input = input("Enter a string: ")
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)