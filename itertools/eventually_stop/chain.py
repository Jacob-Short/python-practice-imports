import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Jacob', 'Raelynn']

# combined = letters + numbers + names
# print(combined)

# combined = itertools.chain(letters, numbers, names)
# for item in combined:
#     print(item)

# result = itertools.islice(range(10), 1, 5, 2)
# for i in result:
#     print(i)

'''files are iterators themselves'''
with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')
