import itertools

counter = itertools.repeat(2, times=3)


# squares = map(pow, range(10), itertools.repeat(2))
squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])

print(list(squares))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))









