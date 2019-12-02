try:
	fp=open("testfile1","r")
	fp.write("This is a testfile")
except IOError:
	print("Error:can't find file or read data")
else:
	print("Written  content into the file successfully")
	fp.close()
