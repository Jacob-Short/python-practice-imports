import itertools

'''
****************************************************
zip will cut off remaining values if list is longer
zip longest will give value None for remaining 'keys'
****************************************************
'''
data = [100,200,300,400]

daily_data = list(itertools.zip_longest(range(10), data))

print(daily_data)
