a_str = input("Input a string: ")
buffer = ""
for letter in a_str:
    if letter.isdigit():
        buffer += letter

print(buffer)