import clipboard as c
try:
    with open('/home/dat/code/token.txt',mode = 'r') as my_file:
        token = my_file.readline()
        c.copy(token)
except FileNotFoundError as err:
    print('file does not exist')
    raise