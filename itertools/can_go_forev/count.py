import itertools

# returns an iterator that counts
# counter = itertools.count(start=5,step=-2.5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100,200,300,400]

daily_data = list(zip(itertools.count(), data))

print(daily_data)


#*** zip will cut off remaining values if list is longer
#*** zip longest will give value None for remaining 'keys'