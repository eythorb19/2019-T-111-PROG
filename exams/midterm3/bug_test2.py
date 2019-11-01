from bug import Bug

print("Bug 1:")
bug1 = Bug(18)  # creates an instance of a bug whose initial position is at 18
print(bug1)

for i in range(1,5):
    bug1.move()
    print(bug1)
