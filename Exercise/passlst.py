def countlst(lst):

	even=0
	odd=0
	for i in lst:
		if i%2==0:
			even+=1
		else:
			odd+=1

	return even,odd

lst={19,24,36,10,56,17,3,65,84}
even,odd=countlst(lst)
#print(even,odd)
print("Even:{} and Odd:{}".format(even,odd))

