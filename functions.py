def text(a):
    '''
    alv puedo explicar la funcion
    '''
    print(a)

def sf(*args):
    print(*args)
    return sum(args)

sf(1,2,3,4,5)
    
# *args and **kwargs

def kwargsbs(**kwargs):
    total=0
    for item in kwargs.values():
        total+=item
    return total

print(kwargsbs(name=90,jum=8))