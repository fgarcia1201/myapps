f = open('poem.txt')
x = 0
for line in iter(f):
        x=x+1	
	print line 
print ("There are "), x, (" lines in the file") 
f.close()
