my_list = [num for num in range(0,100) if num%2 ==0]

print(my_list)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)