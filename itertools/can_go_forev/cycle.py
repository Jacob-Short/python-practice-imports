import itertools

counter = itertools.cycle(('On', 'Off'))

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


'''returns an iterator that goes on forever
take itertable as arg-cycles through values over and over'''

