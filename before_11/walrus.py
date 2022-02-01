a='helooooooooooooo'

if((n:=len(a))>10): #walrus power
    print(f'too long {n} elements')

if (len(a) > 10):
    print(f'too long {len(a)} elements')

while((n:=len(a))>1):
    print(n)
    a=a[:-1]