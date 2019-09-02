# King’s Island needs a program for its admission booths. When visitors to the park come up to the booth to
# purchase their tickets, the worker uses this program to figure out how much to charge them.

# Each ticket cost $30. Senior citizens (age >= 65) are given a 50% discount.  Children under (or equal to) the age of 5 get a free admission.
# Write a program that prompts for the visitor's age and computes the ticket price (should be a float)

age = int(input("Input age: ")) # Do not change this line
price = 30.0

if age >= 65:
    price = price * 0.5
elif age <= 5:
    price = 0.0

print(price)