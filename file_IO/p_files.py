with open('text.txt', mode='a') as my_file:
    text = my_file.write('Hey it\'s me :)')
    print(my_file.readlines())