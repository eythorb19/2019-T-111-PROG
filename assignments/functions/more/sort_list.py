def sort_list(a_list):
    a_list.sort()

def get_list():
    a_list = []
    while True:
        try:
            num = int(input())
            a_list.append(num)
        except:
            break
    return a_list

def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()