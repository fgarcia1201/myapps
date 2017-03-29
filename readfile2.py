#Open the file with read only permit.
f = open('poem.txt', "r")

#use readlines to  read all lines in teh file
#The variable "lines" is the list containing all lines

#lines = f.readline()
print f.readlines()
#Close the file after reading the lines.
f.close()
