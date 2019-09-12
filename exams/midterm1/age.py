age = int(input("Enter your age: "))

if age >= 70:
    print("Old")
elif age >= 51:
    print("Middle-aged")
elif age >= 35:
    print("Mature")
elif age >= 0:
    print("Young")
else:
    print("Invalid age")