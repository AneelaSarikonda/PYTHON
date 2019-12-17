import re
s=r"Now, let see what happens 123if you remove '\' from s. There i057s no 's' alphabet in the output, this is because 83we have removed '\' from the string, and it evaluates 's' as a 16regular character and thus @5split the words wherever it finds 's' in the string."
x=re.findall(r"[a-z]{1}",s)
#y=re.findall(r"\d",s)
#z=re.findall(r".",s)
print(x)
#print(y)
#print(z)
print(type(x))


