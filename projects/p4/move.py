
MAX = 10
MIN = 1

def read_position():
    pos = int(input("Input a position between " + str(MIN) + " and " + str(MAX) + ": "))
    return pos

def display_position(pos):
    for i in range(1, MAX+1):
        if i == pos:
            print('o', end='')
        else:
            print('x', end='')
    print()

def display_instructions():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def read_choice():
    choice = input("Input your choice: ")
    return choice

def new_position(pos, choice):
    if choice == 'l':
        if pos > MIN:
            pos -= 1
    elif choice == 'r':
        if pos < MAX:
            pos += 1
    return pos

# The main program starts here
choice = 'l'
pos = read_position()
display_position(pos)
display_instructions()

while choice == 'l' or choice == 'r':
    choice = read_choice()
    pos = new_position(pos, choice)
    display_position(pos)