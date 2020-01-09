from height import Height

h1 = Height(5,9)    # 5 feet, 9 inches
print(h1)
h2 = Height(5,11)   # 5 feet, 11 inhces
print(h2)

c1 = h1.cm()        # converts h1 to centimeters
print(c1,"cm")

c2 = h2.cm()        # converts h2 to centimeters
print(c2,"cm")

print(h2 > h1)      
print(h1 > h2)

h3 = h1 + h2        # adds to heights
print(h3)
c3 = h3.cm()
print(c3,"cm")

h4 = Height(5,12)
print(h4)
c4 = h4.cm()
print(c4,"cm")

print(h4>h3)
