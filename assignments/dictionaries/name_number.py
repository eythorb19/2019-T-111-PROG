def enter_data(the_dict):
    ''' Enters data input by user into the_dict '''
    name = input("Name: ")
    number = input("Number: ")
    the_dict[name] = number

def dict_to_tuple(the_dict):
    ''' Returns a list of tuples contains the key-value pairs in the_dict'''
    dictlist = []
    for key, value in the_dict.items():
        temp = (key,value)
        dictlist.append(temp)  
    return dictlist

def more_data():
    more = input('More data (y/n)? ')
    return more.lower() == 'y'

# Main program starts here
the_dict = {}

go_again = True
while go_again:
    enter_data(the_dict)
    go_again = more_data()

dictlist = dict_to_tuple(the_dict)     
print(sorted(dictlist))