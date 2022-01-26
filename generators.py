# def make_list(num):
#     temp_list = []
#     for i in range(num):
#         temp_list.append(i)
#     return temp_list

# my_list = make_list(122)

# print(my_list)

from performance import performance

def generate_f(num):
    for i in range(num):
        yield i # this creates the generator

# g = generate_f(100)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

@performance
def long_time():
    print('1')
    for i in range(10000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(10000)):
        i*5

# long_time()
# long_time2()

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
    
print(special_for([1,2,3,4]))