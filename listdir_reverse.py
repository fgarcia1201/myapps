#will list dir in path in reverse order
import os

mydir = os.listdir('/')[::-1]

for item in mydir:
	print item
