'''
filter => determine whether true or flase
compress => values are passed as a iterable
'''

import itertools


letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Jacob', 'Raelynn']

'''filter'''
# def lt_2(n):
#     if n < 2:
#         return True
#     return False

# result = filter(lt_2, numbers)

'''compress'''
selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)
# result = itertools.filterfalse(lt_2, numbers)

for i in result:
    print(i)