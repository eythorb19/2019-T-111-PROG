from bug import Bug

print("Bug 1:")
bug1 = Bug(10)  # creates an instance of a bug whose initial position is at 10
print(bug1)

for i in range(1,3):
    bug1.move()
    print(bug1)

bug1.turn()

for i in range(1,5):
    bug1.move()
    print(bug1)

print("Bug 2:")
bug2 = Bug(5)   # creates an instance of a bug whose initial position is at 5
bug2.turn()
bug2.move()
print(bug2)

assert not bug2 > bug1
if bug1 > bug2:
    print("Bug1 has travelled further than bug2")

print("Bug 3:")
# creates an instance of a bug whose initial position is the sum of the position of bug1 and bug2
bug3 = bug1 + bug2  
print(bug3)
bug3.move()
bug3.move()
print(bug3)
if bug3 > bug1:
    print("Bug3 has travelled further than bug1")

bug4 = Bug(25)
print(bug4)

bug5 = Bug(-5)
print(bug5)