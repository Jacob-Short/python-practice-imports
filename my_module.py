
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, v in enumerate(to_search):
        if v == target:
            return i

    return -1
