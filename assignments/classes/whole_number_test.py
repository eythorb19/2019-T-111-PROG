from whole_number import WholeNumber

num1 = WholeNumber(4.5)
print(num1)

num2 = WholeNumber("4")
print(num2)

num3 = num1 * num2
print(num3)

num1 = WholeNumber(3)
num2 = WholeNumber(4)
num3 = num1 + num2
print(num3)

num3 = num2 - num1
print(num3)

num3 = num1 - num2
print(num3)