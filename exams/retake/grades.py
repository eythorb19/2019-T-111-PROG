def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None
    
def read_grades(file_object):
    ''' Reads grades from file stream and returns them as a list of floats '''
    grade_list = []
    for grade_str in file_object:
        grade_str = grade_str.strip()
        try:
            grade = float(grade_str)
        except ValueError:
            continue
        grade_list.append(grade)
    return grade_list

def get_average(a_list):
    ''' Returns the average of the numbers in the given list '''
    return sum(a_list) / len(a_list)

def get_median(a_list):
    ''' Returns the median of the given list, a_list.
        Assumes that a_list is sorted in a ascending order '''
    length = len(a_list)
    middle_idx = length // 2
    if length % 2 != 0:    # The length of the list is odd
        median = a_list[middle_idx]
    else:
        median = (a_list[middle_idx] + a_list[middle_idx - 1]) / 2
    return median

def print_results(average, median):
    print("Average: {:.2f}".format(average))
    print("Median: {:.2f}".format(median))

# Main program starts here
file_name = input("Enter file name: ")
file_object = open_file(file_name)
if file_object:
    grade_list = read_grades(file_object)
    average = get_average(grade_list)
    median = get_median(sorted(grade_list))
    print_results(average, median)
else:
    print("File {} not found!".format(file_name))
