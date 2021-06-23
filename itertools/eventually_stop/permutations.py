import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Jacob', 'Raelynn']

result = itertools.permutations(letters, 2)

for item in result:
    print(item)