n = int(input("Input a natural number: "))
count = 2

if n == 1:
    prime = False
else:
    prime = True

while count < n:
    if n % count == 0:
        prime = False
        break
    count += 1

if prime:
    print("Prime")
else:
    print("Not prime")