grade = float(input("Input a grade: ")) # Do not change this line

if grade < 0.0 or grade > 10.0:
    print("Invalid grade!") # Do not change this line
elif grade >= 5.0 and grade <= 10:
    print("Passing grade!") # Do not change this line
else:
    print("Failing grade!") # Do not change this line