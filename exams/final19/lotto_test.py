from lotto import *

assert valid_range([1,12,23,27,40])
assert not valid_range([1,12,23,27,41])

assert convert_to_ints(['1','12','23','27','40']) == [1,12,23,27,40]
assert convert_to_ints(['1','12','ab','cd','40']) == None


