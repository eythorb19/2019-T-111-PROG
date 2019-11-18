from isbn import valid_format

assert not valid_format('123')
assert not valid_format('1234567890123')
assert not valid_format('12345678901234')
assert valid_format('0-321-88991-6')
assert not valid_format('00-321-88991-6')
assert valid_format('9-987-12345-0')
assert not valid_format('A-321-88991-6')
assert not valid_format('0-321-88991-66')