stars = int(input("Number of stars: ")) # Do not change this line

for i in range(0, stars):
    for j in range(0, i+1):
        print('*', end='')
    print()
