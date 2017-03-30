var = open('textfile.txt', "r")


#This will print the entire file.
#print var.read()


def printLine():
	for line in var:
		print line
		print line


printLine()


