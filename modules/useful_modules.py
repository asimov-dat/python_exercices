from collections import Counter, defaultdict, OrderedDict
from array import array
import pdb

li = [1,2,3,4,5,6,7,7]
sentence = 'letter ocurring blah blah'
dictio = defaultdict(lambda:'no existe',{'a':1,'b':2})

d = OrderedDict() # dict organized, not necessarie us default from 3.7
d['a'] = 1
d['b'] = 2

arr = array('i',[1,2,3,4]) # list optimized
pdb.set_trace()

print(arr)
print(Counter(li))
print(Counter(sentence))
print(dictio['h'])