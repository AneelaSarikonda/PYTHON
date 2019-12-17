import re

str="This is a regualr expression"
x=re.search("is",str)
y=re.search("hii",str)
print(x.start())
print(x.end())
print(y)


