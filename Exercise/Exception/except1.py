try:
	fp=open("example2","r")
	fp.read("This is an exception handling in python")
except NameError:
	print("Error:can't find file or read data")
except Exception as e:
	print("Exception",e)
else:
	print("File is opened and written successfully")
	fp.close()

