import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3, 2, 1, 0]
names = ['Jacob', 'Raelynn']

def lt_2(n):
    if n < 2:
        return True
    return False

selectors = [True, True, False, True]
'''opposite of dropwhile taking the values that returns true,
once false it just returns value it had up until that point'''
result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)