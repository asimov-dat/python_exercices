def highest_even(arrob=[]):
    temp=[]
    for item in arrob:
        if item %2 == 0:
            temp.append(item)
        else:
            pass
    
    temp.sort()
    print(temp[-1])

test=[1,2,3,4,5,6,10,11]
highest_even(test)