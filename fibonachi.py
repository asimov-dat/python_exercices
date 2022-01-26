def fibonachi(iterations=0):
    incase = 0
    con_case = 1
    for times in range(iterations):
        yield incase
        temp = incase+con_case
        incase = con_case
        con_case = temp
    

def fibonachi2(iterations=0):
    incase = 0
    con_case = 1
    result = []
    for times in range(iterations):
        result.append(incase)
        temp = incase+con_case
        incase = con_case
        con_case = temp
    return result

def call_fib(n,times):
    if n == 1:
        for i in fibonachi(times):
            print(i)
    elif n == 2:
        for i in fibonachi2(times):
            print(i)
    else:
        print('solo se admite 1, 2')

def fib_list(num):
    fiblist = []
    for i in fibonachi(num):
        fiblist.append(i)
    return fiblist

call_fib(2,20)
print(fibonachi2(20))



