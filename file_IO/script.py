import clipboard as c
try:
    with open('../../../token.txt',mode = 'r') as my_file:
        token = my_file.read()
        c.copy(token)
except FileNotFoundError as err:
    print('file does not exist')
    raise