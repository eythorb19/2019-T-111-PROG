from distribution_student import Distribution

def open_file(filename):
        ''' Returns a file stream if filename found, otherwise None '''
        try:
            file_stream = open(filename, "r")
            return file_stream
        except FileNotFoundError:
            return None


dist1 = Distribution()
assert str(dist1) == ''
assert dist1.average() == 0

dist1 = Distribution()
dist1.set_distribution({1:4, 2:5, 3:3, 4:5, 5:7, 6:2})
#print(dist1)
assert str(dist1) == "1: 4\n2: 5\n3: 3\n4: 5\n5: 7\n6: 2\n"

dist1 = Distribution()
dist1.set_distribution({1:4, 2:5, 3:3, 4:5, 5:7, 6:2})
assert dist1.average() == 3.4615384615384617

dist2 = Distribution()
dist2.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4, 7:2})
assert str(dist2) == "1: 5\n2: 3\n3: 7\n4: 4\n5: 6\n6: 4\n7: 2\n"
assert  dist2.average() == 3.7419354838709675

assert dist2 >= dist1

# try:
#     dist3 = dist1 + dist2
# except TypeError:
#     assert True == False

dist3 = dist1 + dist2
assert str(dist3) == "1: 9\n2: 8\n3: 10\n4: 9\n5: 13\n6: 6\n7: 2\n"
assert str(dist1) == "1: 4\n2: 5\n3: 3\n4: 5\n5: 7\n6: 2\n"
assert str(dist2) == "1: 5\n2: 3\n3: 7\n4: 4\n5: 6\n6: 4\n7: 2\n"

file_stream = open_file("data2.txt")
dist4 = Distribution(file_stream)
assert str(dist4) == "1: 7\n2: 7\n3: 8\n4: 5\n5: 6\n6: 5\n7: 4\n8: 4\n"

