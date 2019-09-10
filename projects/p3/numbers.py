# This for loop finds all two digit positive numbers 
# whose square of the sum of its digits is equal to the number
for i in range(10,100):
    first = i % 10
    second = i // 10
    digit_sum_squared = (first+second)**2
    if i == digit_sum_squared:
        print(i)

# This for loop finds all positive numbers below 100 with 10 divisors
for i in range(1,100):
    divisors = 0
    for j in range(1,i+1):
        if i%j == 0:
            divisors += 1
    if divisors == 10:
        print(i)

