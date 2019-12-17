import re
str="This is new File"
x=re.finditer(r"F\w+",str)
for i in x:
	print(i)
	s=i.start()
	so=i.end()
	k=str[s:so]
	print(k)
#print(x.span())
