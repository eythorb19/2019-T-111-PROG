def open_file():
    '''
    Prompts the user for a file name.
    Returns the corresponding file stream or None if file not found
    '''
    try:
        file_name = input("Enter file name: ")
        file_stream = open(file_name)
        return file_stream
    except FileNotFoundError:
        return None

def read_sales_data(file_stream):
    ''' Reads sales data from the given file stream.
        Returns a list of lists, in which each inner list contains 
        the sales found in the corresponding line/department
    '''
    all_sales_data = []
    for line in file_stream:
        line_sales = line.split()
        line_sales_ints = [int(i) for i in line_sales]
        all_sales_data.append(line_sales_ints)
    return all_sales_data

def print_averages_sales(sales_data):
    ''' Prints the averages sales for each department '''
    print("Average sales:")
    for index, data in enumerate(sales_data):
        sum_sales = sum(data)
        count_sales = len(data)
        print("Department no. {}: {:.1f}".format(index+1, sum_sales/count_sales))

def main():
    file_stream = open_file()
    if file_stream:
        sales_data = read_sales_data(file_stream)
        file_stream.close()
        print_averages_sales(sales_data)
    else:
        print("File not found!")

main()