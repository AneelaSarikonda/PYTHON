import re
fp= open("manifest.xml","r")
for line in fp:
	result=re.search("fetch.*$",line)
#	result=re.search(r"fetch^.*(?=(\()))",line)
#	r=re.match("fetch",line)
	if result:
		break
#sr = result.partition("fetch=")[1]
st=str(result)
print(type(st))
print st.split("fetch",1)[0]
print(st[1:6])
#spt=st.split('"')
#print(spt)
print(result.group())
#print(r.group())
#fp.close()
