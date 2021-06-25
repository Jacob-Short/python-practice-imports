import subprocess

# p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# print(p1.stdout)

# p1 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)

# print(p1.stdout)

'''writing the output to a file'''
# with open('output.txt', 'w') as wf:
#     p1 = subprocess.run(['ls', '-la'], stdout=wf, text=True)

# p1 = subprocess.run(['ls', '-la', 'dne'], capture_output=True, text=True)

# print(p1.stderr)

# p1 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)

# print(p1.stderr)

# p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)

# print(p1.stdout)
'''grab ouput from p1'''
# p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)

# print(p2.stdout)
'''doing the same as above'''
# p1 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)

# print(p1.stdout)
