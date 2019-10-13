def add_to_dict(a_dict, key, value):
    ''' Adds the given key-value pair to a_dict '''
    if key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[key] = value

def remove_from_dict(a_dict, key):
    ''' Remove the given key from a_dict '''
    try:
        a_dict.pop(key)
    except KeyError:
        print("Key not found.")
    return a_dict

def find_key(a_dict, key):
    ''' Prints the value for the given key in a_dict '''
    try:
        print("Value: ", a_dict[key])
    except KeyError:
        print("Key not found.")

def menu_selection():
    ''' Prompts for a menu selection '''
    print("Menu: ")
    choice = input("add(a), remove(r), find(f): ").lower()
    return choice

def dict_to_tuples(the_dict):
    ''' Returns a list of tuples contains the key-value pairs in the_dict'''
    dictlist = []
    for key, value in the_dict.items():
        temp = (key,value)
        dictlist.append(temp)  
    return dictlist

def execute_selection(choice, a_dict):
    ''' Executes an operation on a_dict given the choice ''' 
    if choice == "a":
        key = input("Key: ")
        value = input("Value: ")
        add_to_dict(a_dict, key, value)
    elif choice == "r":
        key = input("key to remove: ")
        remove_from_dict(a_dict,key)
    elif choice == "f":
        key = input("Key to locate: ")
        find_key(a_dict,key)
    else:
        print("Invalid choice.")

def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()