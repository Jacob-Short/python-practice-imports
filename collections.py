# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


'''Counter'''
# a = 'aaaabbbbbbcccccc'ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['d'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)


# my_counter = Counter(a)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

'''namedtuple'''

# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)

'''OrderedDict'''

# ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['d'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)


'''defaultdict'''

# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a'])

'''deque'''

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.popleft()
# d.clear()
d.extend([4,5,6])
# d.extendleft([4,5,6])
d.rotate(1)
d.rotate(2)
d.rotate(-1)
print(d)
