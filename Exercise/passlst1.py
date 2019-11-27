def countstr(lst):
	count=0
	for i in range(len(lst)) :
		
		if len(lst[i])>5:
			count+=1
			print(lst[i])
	return count
lst=["Anee","Anilraj","charan","Sireesha","pavan","bhanu","Neha","sai"]
res=countstr(lst)
print(res)
#print(lst)
