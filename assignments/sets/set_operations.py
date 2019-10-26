def get_list():
    a_list = input("Input a list of integers separated with a comma: ").strip().split(",")
    a_list = [int(elem) for elem in a_list]
    return a_list

def get_operation():
    def print_menu():
        print("1. Intersection")
        print("2. Union")
        print("3. Difference")
        print("4. Quit")
    
    print_menu()
    operation = input("Set operation: ")
    return operation

def set_operations():
    oper = get_operation()
    
    while  oper in {'1','2','3'}:
        if oper == '1':
            new_set = set1 & set2
        elif oper == '2':
            new_set = set1 | set2
        else:
            new_set = set1 - set2
        print(new_set)
        oper = get_operation()


# The main program starts here

list1 = get_list()
list2 = get_list()
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
set_operations()



