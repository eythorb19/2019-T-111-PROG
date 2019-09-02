top_num = int(input("Upper number for the range: ")) # Do not change this line

for number in range(2,top_num+1):
    sum_of_divisiors = 0
    for divisior in range(1, number):
        if number % divisior == 0:
            sum_of_divisiors += divisior
    if number == sum_of_divisiors:
        print(number)

    
