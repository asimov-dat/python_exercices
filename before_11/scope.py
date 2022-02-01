# scope what variables do i have access to?

def smf():
    total = 100 # new universe 

a=10
def confusion():
    a = 5
    return a

print(a)
print(confusion())

#1 - start with local
#2 - parent local?

def parent():
    a=1
    def child():
        return a
    return child()

#3 - Global python file
#4 - biuld in pyhton functions
# ------------

total = 100

def count():
    global total 
    total += 1
    return total

count()
print(total)