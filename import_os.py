import os

os.chdir('/home/jacob/Desktop/')

'''create directory'''
# os.mkdir('Math')
# os.makedirs('Math/Sub-Math')

'''delete directory'''
# os.rmdir('Math')
# os.removedirs('Math/Sub-Math')

'''rename a file'''
# os.rename('test.txt', 'demo.txt')

'''loop at contents'''
# os.stat('demo.txt')

'''to find time stamp in readable way'''
# from datetime import datetime
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.frontimestamp(mod_time))

'''generator that yeilds tuple of 3 values'''
# for dirpath, dirnames, filenames in os.walk('/home/jacob/Desktop/'):
#     print(f'Current Path: {dirpath}')
#     print(f'Directories: {dirnames}')
#     print(f'Files: {filenames}')
#     print()


'''get env vars and creating paths'''
# print(os.environ.get('HOME'))
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)
'''teaser'''
# with open(file_path, 'w') as f:
#     f.write()
# print(os.listdir())