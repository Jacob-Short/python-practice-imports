import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3, 2, 1, 0]
names = ['Jacob', 'Raelynn']

def lt_2(n):
    if n < 2:
        return True
    return False

selectors = [True, True, False, True]
'''just drops first few ones then returns the rest'''
result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)