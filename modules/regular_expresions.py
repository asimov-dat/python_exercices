import re

pattern = re.compile(r"this")
string = 'search inside this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a,b,c,d)