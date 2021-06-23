import itertools
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [1,2,3, 2, 1, 0]
names = ['Jacob', 'Raelynn']


'''keeps a running total of values it has seen so far'''
'''can add operator to do diff ops'''
result = itertools.accumulate(numbers, operator.mul)

for item in result:
    print(item)